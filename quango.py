#!/usr/bin/python

import gui as g
import function as f
import tkinter as tk

colorBoard = {}
stoneBoard = {}
board_buttons = {}

red = "red"
orange = "orange"
yellow = "yellow"
blue = "blue"
green = "green"

boardSize = 6
playerNames = []

colorList = [red, red, orange, yellow, red, red, red, orange, blue, green, yellow, red, orange, blue, blue, green, green, yellow, yellow, green, green, blue, blue, orange, red, yellow, green, blue, orange, red, red, red, yellow, orange, red, red]

playerOne = True



f.fill_board(stoneBoard)
f.fill_board(colorBoard)

if __name__ == "__main__":
   g. main()
