#!/usr/bin/python

import quango as q
import gui as g
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
        q.playerNamesTurn = (q.playerNamesTurn + 1) % 2
        q.player.set(q.playerNames[q.playerNamesTurn])
        if q.playerOne:
            put_color(string_2, q.colorBoard[string_2], q.colorBoard, "black" , "b_")
        else:
            put_color(string_2, q.colorBoard[string_2], q.colorBoard, "white" , "w_")

        q.playerOne = not q.playerOne
        return True
    else:
        return False
    
def put_color(button, color, puttingBoard, directory, stone_color):
    puttingBoard[button] = color
    file = Image.open("./" + directory + "/" + stone_color + color + ".png",mode='r')
    my_image = ImageTk.PhotoImage(file)
    q.board_buttons[button]["image"]= my_image
    q.board_buttons[button].image = my_image

def fill_color_board(colorList, colorBoard):
    color = 0
    for x in range(1, q.boardSize + 1):
        for y in range(1, q.boardSize + 1):
            string = "button_" + str(x) + "_" + str(y)
            put_color(string, colorList[color], colorBoard, "block", "")
            color += 1
