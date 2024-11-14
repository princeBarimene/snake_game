from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Obec Snake game")

#create a lsit of tuple for the positions
starting_positions = [(0,0),(-20,0),(-40,0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)



















screen.exitonclick()