

# Each of the command classes below hold information for one of the 
# types of commands found in a graphics file.

class GoToCommand:
    # Constructor with default values for width and color
    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self, t):
        t.width(self.width)
        t.pencolor(self.color)
        t.goto(self.x, self.y)


class CircleCommand:
    def __init__(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, t):
        t.width(self.width)
        t.pencolor(self.color)
        t.circle(self.radius)


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, t):
        t.fillcolor(self.color)
        t.begin_fill()


class EndFillCommand:
    def __init__(self):
        pass

    def draw(self, t):
        t.end_fill()


class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, t):
        t.penup()


class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, t):
        t.pendown()


def main():
    filename = "turtle_cmd.txt" # input("Please enter drawing filename: ")

    t = turtle.Turtle()
    screen = t.getscreen()

    with open(filename, "r") as file:
        command = file.readline().strip()

        while command != "":
            if command == "goto":
                x = float(file.readline())
                y = float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                t.width(width)
                t.pencolor(color)
                t.goto(x, y)

            elif command == "circle":
                radius = float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                t.width(width)
                t.pencolor(color)
                t.circle(radius)

            elif command == "beginfill":
                color = file.readline().strip()
                t.fillcolor(color)
                t.begin_fill()

            elif command == "endfill":
                t.end_fill()

            elif command == "penup":
                t.penup()

            elif command == "pendown":
                t.pendown()

            else:
                print("Unknown command found in file:", command)

            # Read next command
            command = file.readline().strip()

    t.hideturtle()
    screen.exitonclick()
    print("Program Execution Completed.")


if __name__ == "__main__":
    main()
