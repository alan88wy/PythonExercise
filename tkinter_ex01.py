import tkinter
import xml.dom.minidom
import turtle
from tkinter import colorchooser, filedialog


# This class defines the drawing application
class DrawingApplication(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.graphicsCommands = PyList()
        self.buildWindow()

    def buildWindow(self):
        self.master.title("Draw")

        # --- MENU BAR SETUP ---
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)

        # --- TURTLE AND CANVAS SETUP ---
        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.shape("circle")
        screen = theTurtle.getscreen()
        screen.tracer(0)

        # ========== FILE MENU COMMANDS ==========

        def newWindow():
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = PyList()

        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)
            graphicsCommandsElement = xmldoc.getElementsByTagName("GraphicsCommands")[0]
            graphicsCommands = graphicsCommandsElement.getElementsByTagName("Command")

            for commandElement in graphicsCommands:
                command = commandElement.firstChild.data.strip()
                attr = commandElement.attributes
                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = GoToCommand(x, y, width, color)
                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = CircleCommand(radius, width, color)
                elif command == "BeginFill":
                    color = attr["color"].value.strip()
                    cmd = BeginFillCommand(color)
                elif command == "EndFill":
                    cmd = EndFillCommand()
                elif command == "PenUp":
                    cmd = PenUpCommand()
                elif command == "PenDown":
                    cmd = PenDownCommand()
                else:
                    raise RuntimeError("Unknown Command: " + command)

                self.graphicsCommands.append(cmd)

        def loadFile():
            filename = filedialog.askopenfilename(title="Select a Graphics File")
            if not filename:
                return
            newWindow()
            self.graphicsCommands = PyList()
            parse(filename)
            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)
            screen.update()

        def addToFile():
            filename = filedialog.askopenfilename(title="Select a Graphics File")
            if not filename:
                return
            parse(filename)
            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)
            screen.update()

        def write(filename):
            with open(filename, "w") as file:
                file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
                file.write('<GraphicsCommands>\n')
                for cmd in self.graphicsCommands:
                    file.write(f'    {str(cmd)}\n')
                file.write('</GraphicsCommands>\n')

        def saveFile():
            filename = filedialog.asksaveasfilename(title="Save Picture As...")
            if not filename:
                return
            write(filename)

        fileMenu.add_command(label="New", command=newWindow)
        fileMenu.add_command(label="Load...", command=loadFile)
        fileMenu.add_command(label="Load Into...", command=addToFile)
        fileMenu.add_command(label="Save As...", command=saveFile)
        fileMenu.add_command(label="Exit", command=self.master.quit)

        bar.add_cascade(label="File", menu=fileMenu)
        self.master.config(menu=bar)

        # ========== SIDEBAR WIDGETS ==========
        sideBar = tkinter.Frame(self, padx=5, pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        pointLabel = tkinter.Label(sideBar, text="Width")
        pointLabel.pack()
        widthSize = tkinter.StringVar(value="1")
        widthEntry = tkinter.Entry(sideBar, textvariable=widthSize)
        widthEntry.pack()

        radiusLabel = tkinter.Label(sideBar, text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar(value="10")
        radiusEntry = tkinter.Entry(sideBar, textvariable=radiusSize)
        radiusEntry.pack()
        
        
        def circleHandler():
            cmd = CircleCommand(float(radiusSize.get()), float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        circleButton = tkinter.Button(sideBar, text="Draw Circle", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)


        screen.colormode(255)

        penLabel = tkinter.Label(sideBar, text="Pen Color")
        penLabel.pack()
        penColor = tkinter.StringVar(value="#000000")
        penEntry = tkinter.Entry(sideBar, textvariable=penColor)
        penEntry.pack()

        def getPenColor():
            color = colorchooser.askcolor(title="Pick Pen Color")
            if color and color[1]:
                penColor.set(color[1])

        penColorButton = tkinter.Button(sideBar, text="Pick Pen Color", command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)

        fillLabel = tkinter.Label(sideBar, text="Fill Color")
        fillLabel.pack()
        fillColor = tkinter.StringVar(value="#000000")
        fillEntry = tkinter.Entry(sideBar, textvariable=fillColor)
        fillEntry.pack()

        def getFillColor():
            color = colorchooser.askcolor(title="Pick Fill Color")
            if color and color[1]:
                fillColor.set(color[1])

        fillColorButton = tkinter.Button(sideBar, text="Pick Fill Color", command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH)

        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        beginFillButton = tkinter.Button(sideBar, text="Begin Fill", command=beginFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        endFillButton = tkinter.Button(sideBar, text="End Fill", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)

        penStatusLabel = tkinter.Label(sideBar, text="Pen Is Down")
        penStatusLabel.pack()

        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            penStatusLabel.configure(text="Pen Is Up")
            self.graphicsCommands.append(cmd)

        penUpButton = tkinter.Button(sideBar, text="Pen Up", command=penUpHandler)
        penUpButton.pack(fill=tkinter.BOTH)

        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(theTurtle)
            penStatusLabel.configure(text="Pen Is Down")
            self.graphicsCommands.append(cmd)

        penDownButton = tkinter.Button(sideBar, text="Pen Down", command=penDownHandler)
        penDownButton.pack(fill=tkinter.BOTH)

        # --- Mouse Click and Drag Handlers ---
        def clickHandler(x, y):
            cmd = GoToCommand(x, y, float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        def dragHandler(x, y):
            cmd = GoToCommand(x, y, float(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        screen.onclick(clickHandler)
        theTurtle.ondrag(dragHandler)

        def undoHandler():
            if len(self.graphicsCommands.items) > 0:
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0, 0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()

        undoButton = tkinter.Button(sideBar, text="Undo", command=undoHandler)
        undoButton.pack(fill=tkinter.BOTH)
        screen.onkeypress(undoHandler, "u")
        screen.listen()


# --- Command Classes ---
class GoToCommand:
    def __init__(self, x, y, width=1, color="black"):
        self.x, self.y, self.width, self.color = x, y, width, color

    def draw(self, t):
        t.width(self.width)
        t.pencolor(self.color)
        t.goto(self.x, self.y)

    def __str__(self):
        return f'<Command x="{self.x}" y="{self.y}" width="{self.width}" color="{self.color}">GoTo</Command>'


class CircleCommand:
    def __init__(self, radius, width=1, color="black"):
        self.radius, self.width, self.color = radius, width, color

    def draw(self, t):
        t.width(self.width)
        t.pencolor(self.color)
        t.circle(self.radius)

    def __str__(self):
        return f'<Command radius="{self.radius}" width="{self.width}" color="{self.color}">Circle</Command>'


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, t):
        t.fillcolor(self.color)
        t.begin_fill()

    def __str__(self):
        return f'<Command color="{self.color}">BeginFill</Command>'


class EndFillCommand:
    def draw(self, t):
        t.end_fill()

    def __str__(self):
        return "<Command>EndFill</Command>"


class PenUpCommand:
    def draw(self, t):
        t.penup()

    def __str__(self):
        return "<Command>PenUp</Command>"


class PenDownCommand:
    def draw(self, t):
        t.pendown()

    def __str__(self):
        return "<Command>PenDown</Command>"


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


# --- MAIN ---
def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)
    drawingApp.mainloop()
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
