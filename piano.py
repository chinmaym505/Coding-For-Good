#importing modules
import pysine
import time
import re
import tkinter as tk
import os
import threading
import tkinter.messagebox
#Defining notes
notes={"c":0,"d":2,"e":4,"f":5,"g":7,"a":9,"b":11,"highC":12}
#Setting preset songs
hotCrossBuns="e2 d2 c2 1 e2 d2 c2 1 c c c c d d d d e2 d2 c2"
londonBridge="g a g f e f g 1 d e f 1 e f g 1 g a g f e f g 1 d g e c"
morningFromPeerGynt="g e d c d e g e d c d e d e g e g a e a g e d c3"

def has_numbers(inputString):
    """checks if there are any numbers"""
    return any(char.isdigit() for char in inputString)
def extractNumbers(string):
    """extracts numbers"""
    a=re.findall(r'\d+',string)
    b=""
    for i in a:
        b+=i
    return int(b)
def freq(base_freq,n):
    """creates a frequency based on the note numbers"""
    return base_freq * 2**(n/12)
def play(note):
    """plays a note based on the frequency"""
    pysine.sine(frequency=freq(261.63,notes[note]), duration=1.0)
def playSong(song):
    """plays a song based on notes"""
    if type(song) is not list:
        song=song.split(" ")
    for i in song:
        try:
            b=int(i)
            time.sleep(b)
            
           
        except:
            if has_numbers(i):
                h=extractNumbers(i)
                i=i.removesuffix(str(h))
            
                for a in range(0,h):
                    play(i)
                    
            else:
                play(i)

class tkGif:
    def __init__(self,root,gif):
        self.root=root
        self.gif=gif
    def update(self,ind):
        frame = self.frames[ind]
        ind += 1
        if ind == self.frameCnt:
            ind = 0
        self.label.configure(image=frame)
        self.root.after(100, self.update, ind)
    def display(self):
        self.frameCnt = 23
        self.frames = [tk.PhotoImage(file=self.gif,format = 'gif -index %i' %(i)) for i in range(self.frameCnt)]
        self.label = tk.Label(self.root)
        self.label.pack()
        self.root.after(0, self.update, 0)
def playSongWindow(song):
    window = tk.Tk()
    tk.Label(text=f"Playing {song}").pack()
    gif=tkGif(window,"mygif.gif")
    gif.display()
    exec(f"playSong({song})")
    window.destroy()
#creating app
app=tk.Tk()

#creating interface for song player
def show():
    """shows song player and plays song"""
    if clicked.get() == "Select a song":
        tkinter.messagebox.showwarning(title="Warning", message="Please select a song")
    else:
        if clicked.get() == "Hot Cross Buns":
            a = threading.Thread(target=lambda:playSong(hotCrossBuns))
            b = threading.Thread(target=lambda:playSongWindow(clicked.get()))
            a.start()
            b.start()
        elif clicked.get() == "London Bridge":
            a = threading.Thread(target=lambda:playSong(londonBridge))
            b = threading.Thread(target=lambda:playSongWindow(clicked.get()))
            a.start()
            b.start()
        else:
            a = threading.Thread(target=lambda:playSong(morningFromPeerGynt))
            b = threading.Thread(target=lambda:playSongWindow(clicked.get()))
            a.start()
            b.start()
# Dropdown menu options
options = [
        "Select a song",
	"Hot Cross Buns",
	"London Bridge",
	"Morning From Peer Gynt"
]
# datatype of menu text
clicked = tk.StringVar()

# initial menu text
clicked.set( "Select a song" )

# Create Dropdown menu
tk.OptionMenu( app , clicked , *options ).pack()

# Create button, it will change label text
tk.Button( app , text = "Play" , command = show ).pack()

#creating keyboard
buttons = tk.Frame(app)
buttons2 = tk.Frame(app)
buttons2.pack(pady = 5,x=0,y=0)
buttons.pack(pady = 5)

#buttons1
tk.Button(master=buttons,height=5,text="c",command=lambda:play("c")).pack(side=tk.LEFT)
tk.Button(master=buttons,height=5,text="d",command=lambda:play("d")).pack(side=tk.LEFT)
tk.Button(master=buttons,height=5,text="e",command=lambda:play("e")).pack(side=tk.LEFT)
tk.Button(master=buttons,height=5,text="f",command=lambda:play("f")).pack(side=tk.LEFT)
tk.Button(master=buttons,height=5,text="g",command=lambda:play("g")).pack(side=tk.LEFT) 
tk.Button(master=buttons,height=5,text="a",command=lambda:play("a")).pack(side=tk.LEFT)
tk.Button(master=buttons,height=5,text="b",command=lambda:play("b")).pack(side=tk.LEFT)
tk.Button(master=buttons,height=5,text="c",command=lambda:play("highC")).pack(side=tk.LEFT)

#buttons2
tk.Button(master=buttons2,height=2,text="C#",command=lambda:play("c")).pack(side=tk.LEFT)

#loops the app
app.mainloop()


