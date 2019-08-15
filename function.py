#!/usr/bin/python

import quango as q
import gui as g
import tkinter as tk
from PIL import Image, ImageTk

def make_string(x, y):
    string = "button_" + str(x) + "_" + str(y)
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
 

""" def put_stone(x, y, btn_text): 
    string = make_string(x,y)
    if not q.stoneBoard[string]:
        q.stoneBoard[string] = str(q.playerOne)
        print("Name: " + string + " : " + str(q.playerOne))
        q.playerNamesTurn = (q.playerNamesTurn + 1) % 2
        q.player.set(q.playerNames[q.playerNamesTurn])
        if q.playerOne:
            put_color(string, q.colorBoard[string], q.colorBoard, "black" , "b_")
        else:
            put_color(string, q.colorBoard[string], q.colorBoard, "white" , "w_")

        if(check_win() == True):
            #g.root.event_generate("<<ENDE>>", when="tail")
            print("win")
           # g.Secondframe.change(g.my_frame , g.Thirdframe)
        q.playerOne = not q.playerOne
        return True
    else:
        return False """
    
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
            string = make_string(x,y)
            put_color(string, colorList[color], colorBoard, "block", "")
            color += 1

def check_win():
    #Quadrate checken
    for x in range(1, q.boardSize):
        for y in range(1, q.boardSize):
            button = make_string(x,y)
            neighbour_1 = make_string(x, y+1)
            neighbour_2 = make_string(x+1, y)
            neighbour_3 = make_string(x+1, y+1)
            if ("True" == q.stoneBoard[button] == q.stoneBoard[neighbour_1] == q.stoneBoard[neighbour_2] == q.stoneBoard[neighbour_3]):
                print("Gewonnen Player 1!")
                #g.master.destroy()
                return True
            if ("False" == q.stoneBoard[button] == q.stoneBoard[neighbour_1] == q.stoneBoard[neighbour_2] == q.stoneBoard[neighbour_3]):
                print("Gewonnen Player 2!")
                return True
    #5er Reihe
    for x in range(1, q.boardSize + 1):
        for y in range(1, q.boardSize + 1):
            button = make_string(x,y)
            if(y+4 <= q.boardSize):
                horizontal_1 = make_string(x, y+1)
                horizontal_2 = make_string(x, y+2)
                horizontal_3 = make_string(x, y+3)
                horizontal_4 = make_string(x, y+4)
                if("True" == q.stoneBoard[button] == q.stoneBoard[horizontal_1] == q.stoneBoard[horizontal_2] == q.stoneBoard[horizontal_3] == q.stoneBoard[horizontal_4]):
                    print("Gewonnen Player 1!")
                    return True
                if("False" == q.stoneBoard[button] == q.stoneBoard[horizontal_1] == q.stoneBoard[horizontal_2] == q.stoneBoard[horizontal_3] == q.stoneBoard[horizontal_4]):
                    print("Gewonnen Player 2!")
                    return True
            if(x+4 <= q.boardSize):
                vertical_1 = make_string(x+1, y)
                vertical_2 = make_string(x+2, y)
                vertical_3 = make_string(x+3, y)
                vertical_4 = make_string(x+4, y)
                if("True" == q.stoneBoard[button] == q.stoneBoard[vertical_1] == q.stoneBoard[vertical_2] == q.stoneBoard[vertical_3] == q.stoneBoard[vertical_4]):
                    print("Gewonnen Player 1!")
                    return True
                if("False" == q.stoneBoard[button] == q.stoneBoard[vertical_1] == q.stoneBoard[vertical_2] == q.stoneBoard[vertical_3] == q.stoneBoard[vertical_4]):
                    print("Gewonnen Player 2!")
                    return True
            if(x+4 <= q.boardSize and y+4 <= q.boardSize):
                diagonal_1 = make_string(x+1, y+1)
                diagonal_2 = make_string(x+2, y+2)
                diagonal_3 = make_string(x+3, y+3)
                diagonal_4 = make_string(x+4, y+4)
                if("True" == q.stoneBoard[button] == q.stoneBoard[diagonal_1] == q.stoneBoard[diagonal_2] == q.stoneBoard[diagonal_3] == q.stoneBoard[diagonal_4]):
                    print("Gewonnen Player 1!")
                    return True
                if("False" == q.stoneBoard[button] == q.stoneBoard[diagonal_1] == q.stoneBoard[diagonal_2] == q.stoneBoard[diagonal_3] == q.stoneBoard[diagonal_4]):
                    print("Gewonnen Player 2!")
                    return True

    #same color
    for key, value in q.groupDic.items():
        a = value[0]
        b = value[1]
        c = value[2]
        if("True" == q.stoneBoard[a] == q.stoneBoard[b] == q.stoneBoard[c]):
            print("Gewonnen Player 1!")
            return True 
        if("False" == q.stoneBoard[a] == q.stoneBoard[b] == q.stoneBoard[c]):  
            print("Gewonnen Player 2!")
            return True          

def fieldGroupLlist_to_dic():
    listCounter = 0
    for x in range(1, q.boardSize + 1):
        for y in range(1, q.boardSize + 1):
            button_name = make_string(x,y)
            if q.groupList[listCounter] in q.groupDic:
                q.groupDic[q.groupList[listCounter]].append(button_name)
            else:
                q.groupDic[q.groupList[listCounter]] = [button_name]
            listCounter = listCounter + 1