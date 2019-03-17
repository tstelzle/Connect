#!/usr/bin/python

from tkinter import *

colorBoard = {}
stoneBoard = {}
board_buttons = {}

boardSize = 6

playerOne = True

def make_string(x, y):
    string = str(x) + "_" + str(y)
    return string

def fill_board(fillingBoard):
    for x in range(1,boardSize + 1):
        for y in range(1,boardSize + 1):
            string = make_string(x, y)
            if string not in fillingBoard:
                fillingBoard[string] = ""

def print_board(printingBoard):
    for key,val in printingBoard.items():
        print(str(key) + ":" + str(val))

def put_stone(x, y, playerOne, puttingBoard): 
    string = make_string(x, y)
    if not puttingBoard[string]:
        puttingBoard[string] = playerOne
        return True
    else:
        return False
    
def put_color(x, y, color, puttingBoard):
    string = str(x) + "_" + str(y)
    puttingBoard[string] = color

fill_board(stoneBoard)
fill_board(colorBoard)

class Application:
    def __init__(self, master):
        self.master = master
        master.title("Quango")
        for x in range(1, boardSize + 1):
            for y in range(1, boardSize + 1):
                btn_name = "button_" + str(x) + "_" + str(y) 
                self.btn_name = Button(master, width=9, height=5, text=btn_name, command=master.quit)
                #self.btn_name.pack()
                board_buttons[btn_name] = self.btn_name
        for x in range(1, boardSize + 1):
            for y in range(1, boardSize + 1):
                btn_name = "button_" + str(x) + "_" + str(y)
                board_buttons[btn_name].grid(row=x, column=y)
                

root = Tk()
app = Application(root)
root.mainloop()
