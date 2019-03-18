#!/usr/bin/python

import tkinter as tk
import quango as q
import function as f

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
            q.playerNames.append(nameOne)
            q.playerNames.append(nameTwo)
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

        if q.boardSize % 2 == 0:
            columnTurn = int(q.boardSize / 2)
            columnPlayer = int((q.boardSize / 2) + 1)
        else:
            columnTurn = int(round(q.boardSize / 2) - 1)
            columnPlayer = int(round(q.boardSize / 2))

        self.TurnLabel = tk.Label(master, text="Spieler am Zug:")
        self.TurnLabel.grid(row=0, column=columnTurn)
        self.Turn = tk.Label(master, text=q.playerNames[0])
        self.Turn.grid(row=0, column=columnPlayer)
    
        for x in range(1, q.boardSize + 1):
            for y in range(1, q.boardSize + 1):
                btn_name = "button_" + str(x) + "_" + str(y) 
                #btn_text = tk.StringVar()
                self.btn_name = tk.Button(master, width=9, height=5, text=btn_name, command=lambda x=x, y=y, name=btn_name: f.put_stone(x,y,name))
                #self.btn_name.pack()
                q.board_buttons[btn_name] = self.btn_name
        for x in range(1, q.boardSize + 1):
            for y in range(1, q.boardSize + 1):
                btn_name = "button_" + str(x) + "_" + str(y)
                q.board_buttons[btn_name].grid(row=x, column=y)                
        f.fill_color_board(q.colorList, q.colorBoard)
        
def main():
    app = Mainframe()
    app.mainloop()
