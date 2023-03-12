"""
Author: Chinmay Malvania
"""
#Importing modules
import tkinter as tk #This is the module for UI
import random #this is the module to generate random numbers
import threading
board=[["","",""],["","",""],["","",""]] #Game board

class boardUI:
    """The board UI and controls"""
    def __init__(self,root,player,game):
        self.j=tk.StringVar()
        self.k=tk.StringVar()
        self.l=tk.StringVar()
        self.m=tk.StringVar()
        self.n=tk.StringVar()
        self.o=tk.StringVar()
        self.p=tk.StringVar()
        self.q=tk.StringVar()
        self.r=tk.StringVar()
        self.root=root
        self.game=game
        self.opponent=game.logic.opponent
        self.a = tk. Label(self.root, height=5, width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.j, relief="solid")
        self.a.grid(row=1, column=1)
        
        
        self.b = tk. Label(self.root, height=5, width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.k, relief="solid")
        self.b.grid(row=1, column=2)
        
        self.c = tk. Label(self.root,height=5,width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.l, relief="solid")
        self.c.grid(row=1, column=3)

        
        self.d = tk. Label(self.root,height=5,width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.m, relief="solid")
        self.d.grid(row=2, column=1)
        
        self.e = tk. Label(self.root,height=5,width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.n, relief="solid")
        self.e.grid(row=2, column=2)
       
        self.f = tk. Label(self.root,height=5,width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.o, relief="solid")
        self.f.grid(row=2, column=3)
        
        self.g = tk. Label(self.root,height=5,width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.p, relief="solid")
        self.g.grid(row=3, column=1)
       
        self.h = tk. Label(self.root,height=5,width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.q, relief="solid")
        self.h.grid(row=3, column=2)
        
        self.i = tk. Label(self.root,height=5,width=5, fg='blue',font=('Arial',16,'bold'),textvar=self.r, relief="solid")
        self.i.grid(row=3, column=3)
        
    #The functions below make the board UI work
    def row1_1(self,event):
        
        if board[0][0] == self.opponent:
            return
        board[0][0]=self.opponent
        self.update()
        self.game.turn()
        #timer = threading.Timer(1.0, self.update)
            
        self.update()
    def row1_2(self,event):
        if board[0][1] == self.opponent:
            return
        board[0][1]=self.opponent
        self.update()
        self.game.turn()
        timer = threading.Timer(1.0, self.update)
            
        self.update()
    def row1_3(self,event):
        if board[0][2] == self.opponent:
            return
        board[0][2]=self.opponent
        self.update()
        self.game.turn()
        timer = threading.Timer(1.0, self.update)
        self.update()
    def row2_1(self,event):
        if board[1][0] == self.opponent:
            return
        board[1][0]=self.opponent
        self.update()
        self.game.turn()
        timer = threading.Timer(1.0, self.update)
        self.update()
    def row2_2(self,event):
        if board[1][1] == self.opponent:
            return
        board[1][1]=self.opponent
        self.update()
        self.game.turn()
        timer = threading.Timer(1.0, self.update)
        self.update()
    def row2_3(self,event):
        if board[1][2] == self.opponent:
            return
        board[1][2]=self.opponent
        self.update()
        self.game.turn()
        timer = threading.Timer(1.0, self.update)
        self.update()
    def row3_1(self,event):
        if board[2][0] == self.opponent:
            return
        board[2][0]=self.opponent
        self.update()
        self.game.turn()
        timer = threading.Timer(1.0, self.update)
    def row3_2(self,event):
        if board[2][1] == self.opponent:
            return
        board[2][1]=self.opponent
        self.update()
        self.game.turn()
        self.update()
        os.sleep(1)
    def row3_3(self,event):
        if board[2][2] == self.opponent:
            return
        board[2][2]=self.opponent
        self.update()
        self.game.turn()
        timer = threading.Timer(1.0, self.update)
    def update(self):
        self.j.set(board[0][0])
        self.k.set(board[0][1])
        self.l.set(board[0][2])
        
        self.m.set(board[1][0])
        self.n.set(board[1][1])
        self.o.set(board[1][2])
        
        self.p.set(board[2][0])
        self.q.set(board[2][1])
        self.r.set(board[2][2])
        
    def start(self):
        """This function starts the UI. After you run this, the board will be clickable"""
        self.a.bind('<Button-1>',self.row1_1)
        self.b.bind('<Button-1>',self.row1_2)
        self.c.bind('<Button-1>',self.row1_3)

        self.d.bind('<Button-1>',self.row2_1)
        self.e.bind('<Button-1>',self.row2_2)
        self.f.bind('<Button-1>',self.row2_3)

        self.g.bind('<Button-1>',self.row3_1)
        self.h.bind('<Button-1>',self.row3_2)
        self.i.bind('<Button-1>',self.row3_3)

class gameUI():
    """This is the game UI. It combines everything together and makes the app"""
    def __init__(self):
        
        self.game=ticTacToeGameEngine()
        app = tk.Tk()
        self.board=boardUI(app,self.game.logic.opponent,self.game)
        self.board.start()
        tk.mainloop()
        
        

class ticTacToeGameLogic:
    """This is the logic of the game. It uses methods to keep it from loosing and to try winning"""
    def __init__(self,opponent="x"):
        self.opponent=opponent
        if self.opponent=="x":
            self.player="o"
        else:
            self.player = "x"
    def across(self):
        """Checks if the player is trying to win using across. this is what it would look like: |x|x|o|"""
        for i in range(0,2):
            if board[i].count(self.opponent) == 2 and board[i].count(self.player) == 0:
                return i

    def diagnalLeftUp(self):
        """Checks if the player is trying to win diagnaly left. this is what it would look like: \n|x| | |\n| |x| |\n| | |o|"""
        if board[0][0] == self.opponent and board[1][1] == self.opponent and board[2][2] is not self.player:
            return 1


    def diagnalRightUp(self):
        """Checks if the player is trying to win diagnaly right. this is what it would look like: \n| | |x|\n| |x| |\n|o| | |"""
        if board[0][2] == self.opponent and board[1][1] == self.opponent and board[2][0] is not self.player:
            return 1

    def middle(self):
        """Checks if the player is in the middle. this is what it would look like: \n| | | |\n| |x| |\n| | | |"""
        for i in range(0,2):
            if board[i][1]==self.opponent:
                return i
    def down(self):
       for i in range(0,2):
            
            if board[0][i] == self.opponent and board[1][i] == self.opponent:
               
                return i
    def up(self):
        for i in range(0,2):
            
            if board[2][i] == self.opponent and board[1][i] == self.opponent:
                return i
    def diagnalLeftDown(self):
##        """Checks if the player is trying to win diagnaly left. this is what it would look like: \n|x| | |\n| |x| |\n| | |o|"""
        if board[2][0] == self.opponent and board[1][1] == self.opponent and board[0][2] is not self.player:
            return 1


    def diagnalRightDown(self):
##        """Checks if the player is trying to win diagnaly right. this is what it would look like: \n| | |x|\n| |x| |\n|o| | |"""
        if board[2][2] == self.opponent and board[1][1] == self.opponent and board[0][0] is not self.player:
            return 1

class ticTacToeGameEngine:
    """This is the engine. It takes the logic and uses it to make a move"""
    def __init__(self,opponent="x"):
        self.logic=ticTacToeGameLogic(opponent)
    def turn(self):
        """This function makes a move. It uses the functions from the logic object to see what the player is trying to do so it can block the move"""
        a=self.logic.up()
        b=self.logic.across()
        c=self.logic.diagnalLeftUp()
        d=self.logic.diagnalRightUp()
        g=self.logic.diagnalLeftDown()
        h=self.logic.diagnalRightDown()
        e=self.logic.middle()
        f=self.logic.down()
        
        if f is not None:
            if board[2][f] != self.logic.opponent or self.logic.player:
                board[2][f] = self.logic.player
            else:
                return False
        elif a is not None:
            if board[0][a] != self.logic.opponent or self.logic.player:
                board[0][a] = self.logic.player
            else:
                return False
        elif b is not None:
            board[b][board[b].index("")] = self.logic.player
            
        elif c is not None:
            if not board[2][2] == self.logic.opponent:
                board[2][2]=self.logic.player
            else:
                return False
        elif d is not None:
            if not board[2][0]==self.logic.opponent:
                board[2][0]=self.logic.player
            else:
                return False
        elif g is not None:
             if not board[0][2] == self.logic.opponent:
                board[0][2]=self.logic.player
             else:
                 return False
        elif h is not None:
            if not board[0][0] == self.logic.opponent:
                board[0][0]=self.logic.player
            else:
                 return False
        elif e is not None:
            a=random.randint(0,2)
            if a == 1:
                board[e][2]=self.logic.player
                pass
            elif a==0:
                board[e][0]=self.logic.player
                pass
            else:
                try:
                    if board[e+1][1] != self.logic.opponent or self.logic.player:
                        board[e+1][1]=self.logic.player
                except:
                     if board[e-1][1] != self.logic.opponent or self.logic.player:
                         board[e-1][1]=self.logic.player
                return False
                

        else:
            for i in range(0,2):
                try:
                    opponentLocation = board[i].index(self.logic.opponent)
                    opponentLocation2=i
                    
                except:
                    continue
                
                
                try:
                    board[opponentLocation2][opponentLocation+1]=self.logic.player
                except:
                    board[opponentLocation2][opponentLocation-1]=self.logic.player
                pass
ticTacToe=gameUI()
                
                


