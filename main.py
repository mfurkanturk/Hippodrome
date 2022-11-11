from turtle import Turtle, Screen
import random

screen = Screen()
width = 1000
height = 480
screen.setup(width=width, height=height)

colors = ["purple", "green", "red", "blue", "orange"]
horses = ["nazli", "oymapinar", "ayse", "saffet", "esmerim"]


def creator():
    horse_objects = []
    for m in horses:
        m = Turtle()
        horse_objects.append(m)
    return horse_objects


def coordinates(counterr):
    x = -(width/2) + 50
    y = -(height/2) + counterr * (height / (len(horses) + 1))
    return x, y


counter = 0
for horse_object in creator():
    horse_object.shape("turtle")
    horse_object.penup()
    horse_object.goto(coordinates(counter+1))
    horse_object.color(colors[counter])
    horse_object.speed(3)
    counter += 1

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

cont = True
step = [5, 10, 15]
while cont:
    for horse in screen.turtles():
        horse.forward(random.choice(step))
        if horse.xcor() >= width/2-15:
            winner = horse
            if winner.color() == (bet, bet):
                screen.title(f"You win.")
            else:
                screen.title(f"You lose. Winner is {winner.color()}")
            cont = False


screen.exitonclick()