import math

import kivy
from kivy import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


def show_popup(value):
    show = P(value)  # Create a new instance of the P class

    popupWindow = Popup(title="Winner!", content=show, size_hint=(None, None), size=(400, 400))
    # Create the popup window

    popupWindow.open()


class P(FloatLayout):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        print(value)
        self.something.text = value


class NaCGame:
    def __init__(self):

        self.game = [["", "", ""], ["", "", ""], ["", "", ""]]

    def checkLine(self, line):
        if line[0] == "O" or line[0] == "X":
            if line[0] == line[1] and line[1] == line[2]:
                return True
        return False

    def checkForWin(self):

        for i in (range(len(self.game))):
            win = self.checkLine(self.game[i])
            if win:
                winner = self.game[i][0]
                return winner
            win = self.checkLine([self.game[0][i], self.game[1][i], self.game[2][i]])
            if win:
                winner = self.game[0][i]
                return winner
        win = self.checkLine([self.game[0][0], self.game[1][1], self.game[2][2]])
        if win:
            winner = self.game[0][0]
            return winner
        win = self.checkLine([self.game[0][2], self.game[1][1], self.game[2][0]])
        if win:
            winner = self.game[0][2]
            return winner
        return False

    def move(self, Value, Xcoord, Ycoord):
        print("player moved:", Value, Xcoord, Ycoord)
        self.game[Ycoord][Xcoord] = Value
        print(self.game)
        winner = self.checkForWin()
        if not winner:
            empty = True
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.game[i][j] == "":
                        empty = False
            if empty:
                return "draw"
        return winner

    def reset(self, data):
        self.game = [["", "", ""], ["", "", ""], ["", "", ""]]
        data.upperLeft.text = ""
        data.upperMiddle.text = ""
        data.upperRight.text = ""

        data.middleLeft.text = ""
        data.middleMiddle.text = ""
        data.middleRight.text = ""

        data.lowerLeft.text = ""
        data.lowerMiddle.text = ""
        data.lowerRight.text = ""


class TwoPlayerScreen(Screen):

    def on_enter(self):
        print("Stating 2 Player Mode")
        self.playerOneName.background_color = [0.3, 1, 0.3, 1]
        self.playerTwoName.background_color = [1, 1, 1, 1]
        print(self.playerOneName.background_color)
        self.newGame = NaCGame()

    def play_move(self, buttonClicked):

        Xcoord = round((buttonClicked.x / self.width) * 3)
        Ycoord = 2 - round((buttonClicked.y / self.height) * 4)
        if buttonClicked.text == "":
            if self.playerOneName.background_color[0] == 0.3:

                buttonClicked.text = "X"
                self.playerOneName.background_color = [1, 1, 1, 1]
                self.playerTwoName.background_color = [0.3, 1, 0.3, 1]
                winner = self.newGame.move("X", Xcoord, Ycoord)

            else:
                buttonClicked.text = "O"
                self.playerTwoName.background_color = [1, 1, 1, 1]
                self.playerOneName.background_color = [0.3, 1, 0.3, 1]
                winner = self.newGame.move("O", Xcoord, Ycoord)
            if winner == "X":

                name = "X"
                if self.playerOneName.text != "":
                    name = self.playerOneName.text
                print("The winner is ", name)
                text = "The winner is " + name
                show_popup(text)
                self.newGame.reset(self)
            elif winner == "O":
                name = "O"
                if self.playerOneName.text != "":
                    name = self.playerOneName.text
                print("The winner is ", name)
                text = "The winner is " + name
                show_popup(text)
                self.newGame.reset(self)
            elif winner =="draw":
                print("The game is a draw")
                text = "The game is a draw"
                show_popup(text)
                self.newGame.reset(self)

class HomeScreen(Screen):
    pass


# needed for the gui to load
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("userInterface.kv")


class MyApp(App):
    def build(self):
        self.icon = "NetSSH.png"
        self.title = "Noughts And Crosses"
        return sm


sm = ScreenManager()
screens = [HomeScreen(name="HomeScreen"), TwoPlayerScreen(name="TwoPlayerScreen")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "HomeScreen"

if __name__ == "__main__":
    MyApp().run()
