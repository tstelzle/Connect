#!/usr/bin/python

from PIL import Image, ImageTk

import connect


def make_string(x, y):
    string = "button_" + str(x) + "_" + str(y)
    return string


def fill_board(fillingBoard):
    for x in range(1, connect.boardSize + 1):
        for y in range(1, connect.boardSize + 1):
            string = make_string(x, y)
            if string not in fillingBoard:
                fillingBoard[string] = ""


def print_board(printingBoard):
    for key, val in printingBoard.items():
        print(str(key) + ":" + str(val))


def put_color(button, color, puttingBoard, directory, stone_color):
    puttingBoard[button] = color
    file = Image.open("./" + directory + "/" +
                      stone_color + color + ".png", mode='r')
    my_image = ImageTk.PhotoImage(file)
    connect.board_buttons[button]["image"] = my_image
    connect.board_buttons[button].image = my_image


def fill_color_board(colorList, colorBoard):
    color = 0
    for x in range(1, connect.boardSize + 1):
        for y in range(1, connect.boardSize + 1):
            string = make_string(x, y)
            put_color(string, colorList[color], colorBoard, "block", "")
            color += 1


def check_win():
    # Quadrate checken
    for x in range(1, connect.boardSize):
        for y in range(1, connect.boardSize):
            button = make_string(x, y)
            neighbour_1 = make_string(x, y + 1)
            neighbour_2 = make_string(x + 1, y)
            neighbour_3 = make_string(x + 1, y + 1)
            if ("True" == connect.stoneBoard[button] == connect.stoneBoard[neighbour_1] == connect.stoneBoard[
                neighbour_2] ==
                    connect.stoneBoard[neighbour_3]):
                connect.winner_name = connect.playerNames[0]
                return True
            if ("False" == connect.stoneBoard[button] == connect.stoneBoard[neighbour_1] == connect.stoneBoard[
                neighbour_2] ==
                    connect.stoneBoard[neighbour_3]):
                connect.winner_name = connect.playerNames[1]
                return True
    # 5er Reihe
    for x in range(1, connect.boardSize + 1):
        for y in range(1, connect.boardSize + 1):
            button = make_string(x, y)
            if (y + 4 <= connect.boardSize):
                horizontal_1 = make_string(x, y + 1)
                horizontal_2 = make_string(x, y + 2)
                horizontal_3 = make_string(x, y + 3)
                horizontal_4 = make_string(x, y + 4)
                if ("True" == connect.stoneBoard[button] == connect.stoneBoard[horizontal_1] == connect.stoneBoard[
                    horizontal_2] ==
                        connect.stoneBoard[horizontal_3] == connect.stoneBoard[horizontal_4]):
                    connect.winner_name = connect.playerNames[0]
                    return True
                if ("False" == connect.stoneBoard[button] == connect.stoneBoard[horizontal_1] == connect.stoneBoard[
                    horizontal_2] ==
                        connect.stoneBoard[horizontal_3] == connect.stoneBoard[horizontal_4]):
                    connect.winner_name = connect.playerNames[1]
                    return True
            if (x + 4 <= connect.boardSize):
                vertical_1 = make_string(x + 1, y)
                vertical_2 = make_string(x + 2, y)
                vertical_3 = make_string(x + 3, y)
                vertical_4 = make_string(x + 4, y)
                if ("True" == connect.stoneBoard[button] == connect.stoneBoard[vertical_1] == connect.stoneBoard[
                    vertical_2] ==
                        connect.stoneBoard[vertical_3] == connect.stoneBoard[vertical_4]):
                    connect.winner_name = connect.playerNames[0]
                    return True
                if ("False" == connect.stoneBoard[button] == connect.stoneBoard[vertical_1] == connect.stoneBoard[
                    vertical_2] ==
                        connect.stoneBoard[vertical_3] == connect.stoneBoard[vertical_4]):
                    connect.winner_name = connect.playerNames[1]
                    return True
            if (x + 4 <= connect.boardSize and y + 4 <= connect.boardSize):
                diagonal_1 = make_string(x + 1, y + 1)
                diagonal_2 = make_string(x + 2, y + 2)
                diagonal_3 = make_string(x + 3, y + 3)
                diagonal_4 = make_string(x + 4, y + 4)
                if ("True" == connect.stoneBoard[button] == connect.stoneBoard[diagonal_1] == connect.stoneBoard[
                    diagonal_2] ==
                        connect.stoneBoard[diagonal_3] == connect.stoneBoard[diagonal_4]):
                    connect.winner_name = connect.playerNames[0]
                    return True
                if ("False" == connect.stoneBoard[button] == connect.stoneBoard[diagonal_1] == connect.stoneBoard[
                    diagonal_2] ==
                        connect.stoneBoard[diagonal_3] == connect.stoneBoard[diagonal_4]):
                    connect.winner_name = connect.playerNames[1]
                    return True

    # same color
    for key, value in connect.groupDic.items():
        a = value[0]
        b = value[1]
        c = value[2]
        if ("True" == connect.stoneBoard[a] == connect.stoneBoard[b] == connect.stoneBoard[c]):
            connect.winner_name = connect.playerNames[0]
            return True
        if ("False" == connect.stoneBoard[a] == connect.stoneBoard[b] == connect.stoneBoard[c]):
            connect.winner_name = connect.playerNames[1]
            return True


def fieldGroupLlist_to_dic():
    listCounter = 0
    for x in range(1, connect.boardSize + 1):
        for y in range(1, connect.boardSize + 1):
            button_name = make_string(x, y)
            if connect.groupList[listCounter] in connect.groupDic:
                connect.groupDic[connect.groupList[listCounter]].append(button_name)
            else:
                connect.groupDic[connect.groupList[listCounter]] = [button_name]
            listCounter = listCounter + 1
