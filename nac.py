import tkinter as tk
from tkinter import*
import math
personplaying ="O"
b ="b"
master = Tk()
#our 2d array for our grid
twodarray =[[b,b,b],
            [b,b,b],
            [b,b,b]]
winner =""
moves =0

def finish():
    global master
    global winner
    global moves
    moves =0
    output = str(winner)+" is \n the winner"
    winnerb =Label(width =300,height =300)
    winnerb.place(x=10,y=10)
    winner =Label(text=output,width =10,height =5)
    winner.place(x=10,y=10)
    playagain = Button(text ="play again",command =loading)
    playagain.place(x=10,y =70)
    #refreshes the 2d array
    twodarray[0][0] ="b"
    twodarray[0][1] ="b"
    twodarray[0][2] ="b"
    
    twodarray[1][0] ="b"
    twodarray[1][1] ="b"
    twodarray[1][2] ="b"
    
    twodarray[2][0] ="b"
    twodarray[2][1] ="b"
    twodarray[2][2] ="b"
    personplaying ="O"


def a1move():
    global x
    global y
    x =0
    y =0
    move()
def a2move():
    global x
    global y
    x =1
    y =0
    move()
def a3move():
    global x
    global y
    x =2
    y =0
    move()
def b1move():
    global x
    global y
    x =0
    y =1
    move()
def b2move():
    global x
    global y
    x =1
    y =1
    move()
def b3move():
    global x
    global y
    x =2
    y =1
    move()
def c1move():
    global x
    global y
    x =0
    y =2
    move()
def c2move():
    global x
    global y
    x =1
    y =2
    move()
def c3move():
    global x
    global y
    x =2
    y =2
    move()







def move():
    global personplaying
    global twodarrary
    global winner
    global moves
    print(x,y)
    moves =moves +1
    #picks the symbol to draw on the grid
    if personplaying =="X":
        personplaying ="O"
    else:
        personplaying ="X"
    twodarray[y][x] =personplaying
    print(twodarray[0])
    print(twodarray[1])
    print(twodarray[2])
    oso = Label(text =personplaying,height =1,width =2)
    oso.config(font=('Comic Sans MS', 45, 'bold italic'))


    #deciding who has won
    if twodarray[0][0] ==twodarray[0][1] and twodarray[0][1] == twodarray[0][2]:
        if twodarray[0][0] != "b":
            print(twodarray[0][0] ,"is the winner")
            winner = twodarray[0][0]
            finish()
    elif twodarray[1][0] ==twodarray[1][1] and twodarray[1][1] == twodarray[1][2]:
        if twodarray[1][0] != "b":
            winner = twodarray[1][0]
            print(twodarray[1][0] ,"is the winner")
            finish()
    elif twodarray[2][0] ==twodarray[2][1] and twodarray[2][1] == twodarray[2][2]:
        if twodarray[2][0] != "b":
            winner =twodarray[2][0]
            print(twodarray[2][0] ,"is the winner")
            finish()
        
    elif twodarray[0][0] ==twodarray[1][0] and twodarray[1][0] == twodarray[2][0]:
        if twodarray[0][0] != "b":
            winner = twodarray[0][0]
            print(twodarray[0][0] ,"is the winner")
            finish()
    elif twodarray[0][1] ==twodarray[1][1] and twodarray[1][1] == twodarray[2][1]:
        if twodarray[0][1] != "b":
            winner = twodarray[0][1]
            print(twodarray[0][1] ,"is the winner")
            finish()
    elif twodarray[0][2] ==twodarray[1][2] and twodarray[1][2] == twodarray[2][2]:
        if twodarray[0][2] != "b":
            winner = twodarray[0][2]
            print(twodarray[0][2] ,"is the winner")
            finish()
        
    elif twodarray[0][0] ==twodarray[1][1] and twodarray[1][1] == twodarray[2][2]:
        if twodarray[0][0] != "b":
            winner = twodarray[0][0]
            print(twodarray[0][0] ,"is the winner")
            finish()
    elif twodarray[0][2] ==twodarray[1][1] and twodarray[1][1] == twodarray[2][0]:
        if twodarray[0][2] != "b":
            winner = twodarray[0][2]
            print(twodarray[0][2] ,"is the winner")
            finish()
    if moves ==9:
        winner ="nobody"
        print("nobody is the winner")
        finish()

    oso.place(x=10+(x*80),y=10+(y*85))

def startup():
    global master
    twodarray =[[b,b,b],
            [b,b,b],
            [b,b,b]]
    winnerb =Label(width =300,height =300)
    winnerb.place(x=10,y=10)
    #draws the buttons
    a1 = Button(text=" ",height = 5,width =10,command = a1move)
    a1.place( x=10,y=10)
    
    a2 = Button(text=" ",height = 5,width =10,command = a2move)
    a2.place(x=90,y=10)
    
    a3 = Button(text=" ",height = 5,width =10,command = a3move)
    a3.place(x=170,y=10)
    
    b1 = Button(text=" ",height = 5,width =10,command = b1move)
    b1.place( x=10,y=95)
    
    b2 = Button(text=" ",height = 5,width =10,command = b2move)
    b2.place(x=90,y=95)
    
    b3 = Button(text=" ",height = 5,width =10,command = b3move)
    b3.place(x=170,y=95)
    
    c1 = Button(text=" ",height = 5,width =10,command = c1move)
    c1.place(x=10,y=180)
    
    c2 = Button(text=" ",height = 5,width =10,command = c2move)
    c2.place( x=90,y=180)
    
    c3 = Button(text=" ",height = 5,width =10,command = c3move)
    c3.place(x=170,y=180)
    


    


def loading():
    global master
    twodarray =[[b,b,b],
                [b,b,b],
                [b,b,b]]
    winner =""

    winnerb =Label(width =300,height =300)
    winnerb.place(x=10,y=10)
    startup1 = Label(text="naughts and crosses \n -by Tom Leigh-")
    startup1.place(x=10,y=10)

    startupb = Button(text="click here to \n start the game",command = startup)
    startupb.place(x=22,y=45)
loading()
