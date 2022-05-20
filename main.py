import turtle
from turtle import Screen
from scoreboard import Score
from states import States

screen = Screen()

screen.title("US states")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.tracer(0)
state = States()
score = Score()

game_is_on = True
while game_is_on:
    screen.update()
    user_input = turtle.textinput("US States", "Enter the name of the state: ").capitalize()
    check_answer = state.check_states(user_input)
    if check_answer:
        score.add_score()
    else:
        pass

turtle.mainloop()
