from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(5, -5)
leo.setheading(0.0)
leo.pendown() 
i: int = 0
while i < 5:
    leo.forward(50)
    leo.right(60)
    print("4")
    i = i + 1

done()
