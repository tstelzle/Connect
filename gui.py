#!/usr/bin/python

import tkinter as tk
import quango as q
import function as f

class Firstframe(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.winfo_toplevel().title("Quango")
        self.createWidgets()

    def createWidgets(self):
        self.playerOne_Label = tk.Label(self, text="Name Spieler 1")
        self.playerOne_Label.grid(row=0, column=0)

        self.playerOne = tk.Entry(self)
        self.playerOne.grid(row=1, column=0)

        self.playerTwo_Label = tk.Label(self, text="Name Spieler 2")
        self.playerTwo_Label.grid(row=0, column=2)

        self.playerTwo = tk.Entry(self)
        self.playerTwo.grid(row=1, column=2)

        self.Start = tk.Button(self, text="start", command=self.start_game)
        self.Start.grid(row=3, column=1)

    def start_game(self):
        nameOne = self.playerOne.get()
        nameTwo = self.playerTwo.get()
        if not nameOne or not nameTwo:
            return False
        else:
            q.playerNames.append(nameOne)
            q.playerNames.append(nameTwo)
            self.change(Secondframe)
            return True

    def change(self, frame):
        list = self.grid_slaves()
        for item in list:
            item.destroy()
        self.frame = frame(self)
    
class Secondframe(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        if q.boardSize % 2 == 0:
            columnTurn = int(q.boardSize / 2)
            columnPlayer = int((q.boardSize / 2) + 1)
        else:
            columnTurn = int(round(q.boardSize / 2) - 1)
            columnPlayer = int(round(q.boardSize / 2))

        self.TurnLabel = tk.Label(self, text="Spieler am Zug:")
        self.TurnLabel.grid(row=0, column=columnTurn)
        q.player = tk.StringVar()
        q.player.set(q.playerNames[q.playerNamesTurn])
        tk.Label(self, textvariable=q.player).grid(row=0, column=columnPlayer)
    
        for x in range(1, q.boardSize + 1):
            for y in range(1, q.boardSize + 1):
                btn_name = "button_" + str(x) + "_" + str(y) 
                self.btn_name = tk.Button(self, width=100, height=100, text=btn_name, command=lambda x=x, y=y, name=btn_name: self.put_stone(x,y,name))
                q.board_buttons[btn_name] = self.btn_name
        for x in range(1, q.boardSize + 1):
            for y in range(1, q.boardSize + 1):
                btn_name = "button_" + str(x) + "_" + str(y)
                q.board_buttons[btn_name].grid(row=x, column=y)                
        f.fill_color_board(q.colorList, q.colorBoard)

    def change(self, frame):
        list = self.grid_slaves()
        for item in list:
            item.destroy()
        self.frame = frame(self)

    def put_stone(self, x, y, btn_text): 
        string = f.make_string(x,y)
        if not q.stoneBoard[string]:
            q.stoneBoard[string] = str(q.playerOne)
            print("Name: " + string + " : " + str(q.playerOne))
            q.playerNamesTurn = (q.playerNamesTurn + 1) % 2
            q.player.set(q.playerNames[q.playerNamesTurn])
            if q.playerOne:
                f.put_color(string, q.colorBoard[string], q.colorBoard, "black" , "b_")
            else:
                f.put_color(string, q.colorBoard[string], q.colorBoard, "white" , "w_")

            if(f.check_win() == True):
                self.change(Thirdframe)
            q.playerOne = not q.playerOne
            return True
        else:
            return False
    
class Thirdframe(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.Winner = tk.Label(self, text="Gewinner: ")
        self.Winner.grid(row=0, column=2)

        self.exit = tk.Button(self, text="Exit", command=self.quit)
        self.exit.grid(row=1, column=3)
        self.again = tk.Button(self, text="Play again", command=self.switch_window)
        self.again.grid(row=1, column=0)
    
    def switch_window(self):
        self.change(Secondframe)

    def change(self, frame):
        list = self.grid_slaves()
        for item in list:
            item.destroy()
        self.frame = frame(self)

def main():
    root = tk.Tk()
    app = Firstframe(master=root)
    app.mainloop()

