from turtle import Turtle, Screen
from tkinter import *
MOVING, DRAGGING = range(2)  # states

def move_handler(x, y):
    if state != MOVING:  # ignore stray events
        return

    onmove(screen, None)  # avoid overlapping events
    mrTurtle.penup()
    mrTurtle.setheading(mrTurtle.towards(x, y))
    mrTurtle.goto(x, y)
    onmove(screen, move_handler)

def click_handler(x, y):
    global state

    mrTurtle.onclick(None)  # disable until release
    onmove(screen, None)  # disable competing handler

    mrTurtle.onrelease(release_handler)  # watch for release event
    mrTurtle.ondrag(drag_handler)  # motion is now dragging until release

    state = DRAGGING

def release_handler(x, y):
    global state

    mrTurtle.onrelease(None)  # disable until click
    mrTurtle.ondrag(None)  # disable competing handler

    mrTurtle.onclick(click_handler)  # watch for click event
    onmove(screen, move_handler)  # dragging is now motion until click

    state = MOVING

def drag_handler(x, y):
    if state != DRAGGING:  # ignore stray events
        return

    mrTurtle.ondrag(None)  # disable event inside event handler
    mrTurtle.pendown()
    mrTurtle.setheading(mrTurtle.towards(x, y))
    mrTurtle.goto(x, y)
    mrTurtle.ondrag(drag_handler)  # reenable event on event handler exit

def onmove(self, fun, add=None):
    """
    Bind fun to mouse-motion event on screen.

    Arguments:
    self -- the singular screen instance
    fun  -- a function with two arguments, the coordinates
        of the mouse cursor on the canvas.

    Example:

    >>> onmove(turtle.Screen(), lambda x, y: print(x, y))
    >>> # Subsequently moving the cursor on the screen will
    >>> # print the cursor position to the console
    >>> screen.onmove(None)
    """

    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)
        self.cv.bind('<Motion>', eventfun, add)

screen = Screen()
screen.title("Drawing")
screen.setup(500, 600)
screen.screensize(1920, 1080)
screen.colormode(255)
mrTurtle = Turtle('turtle')
screen.addshape('brush.gif')
mrTurtle.shape('brush.gif')
mrTurtle.speed('fastest')

canvas = screen.getcanvas()
controls=Frame(master=canvas.master)
controls.pack()
#R
Label(master=controls,text="R").pack(side="left")
r=Scale(master=controls, from_=0, to=255, orient=HORIZONTAL)
r.pack(side="left")
#G
Label(master=controls,text="G").pack(side="left")
g=Scale(master=controls, from_=0, to=255, orient=HORIZONTAL)
g.pack(side="left")
#B
Label(master=controls,text="B").pack(side="left")
b=Scale(master=controls, from_=0, to=255, orient=HORIZONTAL)
b.pack(side="left")
#clear button
Button(master=controls,text="clear",command=mrTurtle.clear).pack(side="bottom")

state = MOVING

# Initially we track the turtle's motion and left button clicks
onmove(screen, move_handler)  # a la screen.onmove(move_handler)
mrTurtle.onclick(click_handler)  # a click will turn motion into drag

while True:
    mrTurtle.color(r.get(),g.get(),b.get())
