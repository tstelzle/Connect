#!/usr/bin/python

from PIL import Image, ImageTk

import connect as c


def make_string(x, y):
    string = "button_" + str(x) + "_" + str(y)
    return string


def fill_board(fillingBoard):
    for x in range(1, c.boardSize + 1):
        for y in range(1, c.boardSize + 1):
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
    c.board_buttons[button]["image"] = my_image
    c.board_buttons[button].image = my_image


def fill_color_board(colorList, colorBoard):
    color = 0
    for x in range(1, c.boardSize + 1):
        for y in range(1, c.boardSize + 1):
            string = make_string(x, y)
            put_color(string, colorList[color], colorBoard, "block", "")
            color += 1


def check_win():
    # Quadrate checken
    for x in range(1, c.boardSize):
        for y in range(1, c.boardSize):
            button = make_string(x, y)
            neighbour_1 = make_string(x, y + 1)
            neighbour_2 = make_string(x + 1, y)
            neighbour_3 = make_string(x + 1, y + 1)
            if ("True" == c.stoneBoard[button] == c.stoneBoard[neighbour_1] == c.stoneBoard[neighbour_2] ==
                    c.stoneBoard[neighbour_3]):
                c.winner_name = c.playerNames[0]
                return True
            if ("False" == c.stoneBoard[button] == c.stoneBoard[neighbour_1] == c.stoneBoard[neighbour_2] ==
                    c.stoneBoard[neighbour_3]):
                c.winner_name = c.playerNames[1]
                return True
    # 5er Reihe
    for x in range(1, c.boardSize + 1):
        for y in range(1, c.boardSize + 1):
            button = make_string(x, y)
            if (y + 4 <= c.boardSize):
                horizontal_1 = make_string(x, y + 1)
                horizontal_2 = make_string(x, y + 2)
                horizontal_3 = make_string(x, y + 3)
                horizontal_4 = make_string(x, y + 4)
                if ("True" == c.stoneBoard[button] == c.stoneBoard[horizontal_1] == c.stoneBoard[horizontal_2] ==
                        c.stoneBoard[horizontal_3] == c.stoneBoard[horizontal_4]):
                    c.winner_name = c.playerNames[0]
                    return True
                if ("False" == c.stoneBoard[button] == c.stoneBoard[horizontal_1] == c.stoneBoard[horizontal_2] ==
                        c.stoneBoard[horizontal_3] == c.stoneBoard[horizontal_4]):
                    c.winner_name = c.playerNames[1]
                    return True
            if (x + 4 <= c.boardSize):
                vertical_1 = make_string(x + 1, y)
                vertical_2 = make_string(x + 2, y)
                vertical_3 = make_string(x + 3, y)
                vertical_4 = make_string(x + 4, y)
                if ("True" == c.stoneBoard[button] == c.stoneBoard[vertical_1] == c.stoneBoard[vertical_2] ==
                        c.stoneBoard[vertical_3] == c.stoneBoard[vertical_4]):
                    c.winner_name = c.playerNames[0]
                    return True
                if ("False" == c.stoneBoard[button] == c.stoneBoard[vertical_1] == c.stoneBoard[vertical_2] ==
                        c.stoneBoard[vertical_3] == c.stoneBoard[vertical_4]):
                    c.winner_name = c.playerNames[1]
                    return True
            if (x + 4 <= c.boardSize and y + 4 <= c.boardSize):
                diagonal_1 = make_string(x + 1, y + 1)
                diagonal_2 = make_string(x + 2, y + 2)
                diagonal_3 = make_string(x + 3, y + 3)
                diagonal_4 = make_string(x + 4, y + 4)
                if ("True" == c.stoneBoard[button] == c.stoneBoard[diagonal_1] == c.stoneBoard[diagonal_2] ==
                        c.stoneBoard[diagonal_3] == c.stoneBoard[diagonal_4]):
                    c.winner_name = c.playerNames[0]
                    return True
                if ("False" == c.stoneBoard[button] == c.stoneBoard[diagonal_1] == c.stoneBoard[diagonal_2] ==
                        c.stoneBoard[diagonal_3] == c.stoneBoard[diagonal_4]):
                    c.winner_name = c.playerNames[1]
                    return True

    # same color
    for key, value in c.groupDic.items():
        a = value[0]
        b = value[1]
        c = value[2]
        if ("True" == c.stoneBoard[a] == c.stoneBoard[b] == c.stoneBoard[c]):
            c.winner_name = c.playerNames[0]
            return True
        if ("False" == c.stoneBoard[a] == c.stoneBoard[b] == c.stoneBoard[c]):
            c.winner_name = c.playerNames[1]
            return True


def fieldGroupLlist_to_dic():
    listCounter = 0
    for x in range(1, c.boardSize + 1):
        for y in range(1, c.boardSize + 1):
            button_name = make_string(x, y)
            if c.groupList[listCounter] in c.groupDic:
                c.groupDic[c.groupList[listCounter]].append(button_name)
            else:
                c.groupDic[c.groupList[listCounter]] = [button_name]
            listCounter = listCounter + 1
