#!/usr/bin/python

import quango as q
import tkinter as tk
from PIL import Image, ImageTk

def make_string(x, y):
    string = str(x) + "_" + str(y)
    return string

def fill_board(fillingBoard):
    for x in range(1,q.boardSize + 1):
        for y in range(1,q.boardSize + 1):
            string = make_string(x, y)
            if string not in fillingBoard:
                fillingBoard[string] = ""

def print_board(printingBoard):
    for key,val in printingBoard.items():
        print(str(key) + ":" + str(val))
 

def put_stone(x, y, btn_text): 
    string = make_string(x, y)
    string_2 = "button_" + string
    if not q.stoneBoard[string]:
        q.stoneBoard[string] = str(q.playerOne)
        print("Name: " + string + " : " + str(q.playerOne))
        if q.playerOne:
            image = Image.open("w_red.png")
            w_red = ImageTk.PhotoImage(image)
            #q.board_buttons[string_2]["text"] = str(q.playerOne)
            q.board_buttons[string_2]["image"] = w_red
            #btn_text.set(str(q.playerOne))
        else:
            image = Image.open("b_red.png")
            b_red = ImageTk.PhotoImage(image)
            #q.board_buttons[string_2]["text"] = str(q.playerOne)
            q.board_buttons[string_2]["image"] = b_red
            #btn_text.set(str(q.playerOne))
        q.playerOne = not q.playerOne
        return True
    else:
        return False
    
def put_color(x, y, color, puttingBoard):
    string = "button_" + str(x) + "_" + str(y)
    puttingBoard[string] = color
    q.board_buttons[string]["bg"]=color

def fill_color_board(colorList, colorBoard):
    color = 0
    for x in range(1, q.boardSize + 1):
        for y in range(1, q.boardSize + 1):
            put_color(x, y, colorList[color], colorBoard)
            color += 1
