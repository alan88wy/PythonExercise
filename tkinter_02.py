import tkinter
import turtle

#from tkinter import colorchooser, filedialog

# --- Custom List Class ---
class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def removeLast(self):
        if self.items:
            self.items.pop()

    def __iter__(self):
        for c in self.items:
            yield c

root = tkinter.Tk()
root.title("Draw")

bar = tkinter.Menu(root)
fileMenu = tkinter.Menu(bar, tearoff=0)

canvas = tkinter.Canvas(root, bg="white")
canvas.pack()
graphicsCommands = PyList()

theTurtle = turtle.RawTurtle(canvas)
theTurtle.shape("turtle")
screen = theTurtle.getscreen()
screen.tracer(0)

def newWindow():
    theTurtle.clear()
    theTurtle.penup()
    theTurtle.goto(0, 0)
    theTurtle.pendown()
    screen.update()
    screen.listen()
    graphicsCommands = PyList()

def loadFile():
    pass

def addToFile():
    pass

def saveFile():
    pass

fileMenu.add_command(label="New", command=newWindow)
fileMenu.add_command(label="Load...", command=loadFile)
fileMenu.add_command(label="Load Into...", command=addToFile)
fileMenu.add_command(label="Save As...", command=saveFile)
fileMenu.add_command(label="Exit", command=root.quit)

bar.add_cascade(label="File", menu=fileMenu)
root.config(menu=bar)

root.mainloop()
print("Done!")