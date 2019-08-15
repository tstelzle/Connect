#!/usr/bin/python

import function as f
import gui as g

# stores the color scheme of current board
colorBoard = {}
# stores which player put a stone; True -> Player one; False -> Player two;
stoneBoard = {}
# stores the Tkinter object button in a dictionary; schmema: "button_x_y":Button Object
board_buttons = {}

red = "red"
orange = "orange"
yellow = "yellow"
blue = "blue"
green = "green"

boardSize = 6
playerNames = []
playerNamesTurn = 0
winner_name = ""
player = None
winner = None

# both these lists walk through the field from the top left through each row
# stores the color of the field
colorList = [red, red, orange, yellow, red, red, red, orange, blue, green, yellow, red, orange, blue, blue, green,
             green, yellow, yellow, green, green, blue, blue, orange, red, yellow, green, blue, orange, red, red, red,
             yellow, orange, red, red]
# stores the colorgroup the field belongs to
groupList = [1, 1, 2, 3, 4, 4, 1, 2, 5, 6, 3, 4, 2, 5, 5, 6, 6, 3, 7, 8, 8, 9, 9, 10, 11, 7, 8, 9, 10, 12, 11, 11, 7,
             10, 12, 12]
groupDic = {}

playerOne = True

f.fill_board(stoneBoard)
f.fill_board(colorBoard)
f.fieldGroupLlist_to_dic()

if __name__ == "__main__":
    g.main()
