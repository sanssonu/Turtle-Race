""" Turtle Race! ------ """

from turtle import  Turtle, Screen
import random

screen = Screen()
# Setting the screen's width and height.
screen.setup(width=500, height=400)
# Since the screen has a width of 500px, range of X-coordinate = [-250 to 250].
# Since the screen has a height of 400px, range of Y-coordinate = [-200 to 200].

is_race_on = False

# Taking user's bet on who's gonna win >.<
user_bet = screen.textinput(title="Place your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# List of all turtle objects.
all_turtles = []
# All the turtles will have a fixed X-coordinate and Y-coordinates in the range [90 to -90].
y_coordinate = 90

# Creating 6 turtle objects with the following features:
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")      # Shape = turtle
    new_turtle.penup()                       # Don't draw while moving.
    new_turtle.color(colors[turtle_index])   # Colour of each turtle to be picked from respective index of color's list.
    new_turtle.goto(x=-238, y=y_coordinate)  # X-coordinate = -238  of all turtles, Y-coordinates = range [90 to -90].
    all_turtles.append(new_turtle)           # Add each turtle to the 'all_turtles' list.
    y_coordinate -= 30                       # Updating the Y-coordinate for next turtle.

# If user has made a bet, start the race.
if user_bet:
    is_race_on = True

# While the race is going on:
while is_race_on:
    # For every turtle in the list,
    for turtle in all_turtles:
        # If a turtle's X-coordinate > 230,
        if turtle.xcor() > 230:
            # End the race, and declare it as the winner.
            is_race_on = False
            winning_color = turtle.pencolor()
            # Tell the user if they won/lost the bet.
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        # Move the turtles forward by a random distance.
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# When the race is finished, exit the screen by clicking on it.
screen.exitonclick()
