#!/usr/bin/python

import tkinter as tk

colorBoard = {}
stoneBoard = {}
board_buttons = {}

boardSize = 6
playerNames = []

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

class Mainframe(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = Firstframe(self)
        self.frame.grid()

    def change(self, frame):
        list = self.grid_slaves()
        for item in list:
            item.destroy()
        self.frame = frame(self)

class Firstframe(tk.Frame):
    def start_game(self):
        nameOne = self.playerOne.get()
        nameTwo = self.playerTwo.get()
        if not nameOne or not nameTwo:
            return False
        else:
            playerNames.append(nameOne)
            playerNames.append(nameTwo)
            self.master.change(Secondframe)
            return True

    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        master.title("Quango")
        self.playerOne_Label = tk.Label(master, text="Name Spieler 1")
        self.playerOne_Label.grid(row=0, column=0)

        self.playerOne = tk.Entry(master)
        self.playerOne.grid(row=1, column=0)

        self.playerTwo_Label = tk.Label(master, text="Name Spieler 2")
        self.playerTwo_Label.grid(row=0, column=2)

        self.playerTwo = tk.Entry(master)
        self.playerTwo.grid(row=1, column=2)

        self.Start = tk.Button(master, text="start", command=self.start_game)
        self.Start.grid(row=3, column=1)

class Secondframe(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        master.title("Quango")

        for x in range(1, boardSize + 1):
            for y in range(1, boardSize + 1):
                btn_name = "button_" + str(x) + "_" + str(y) 
                self.btn_name = tk.Button(master, width=9, height=5, text=btn_name, command=master.quit)
                #self.btn_name.pack()
                board_buttons[btn_name] = self.btn_name
        for x in range(1, boardSize + 1):
            for y in range(1, boardSize + 1):
                btn_name = "button_" + str(x) + "_" + str(y)
                board_buttons[btn_name].grid(row=x, column=y)                

def main():
    app = Mainframe()
    app.mainloop()

if __name__ == "__main__":
    main()
