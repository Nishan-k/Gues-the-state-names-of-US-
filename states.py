import pandas as pd
from turtle import Turtle

dataframe = pd.read_csv("50_states.csv")
FONT = ("Arial", 8, "normal")


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.x = None
        self.y = None
        self.hideturtle()
        self.states = dataframe['state']
        self.x_cor = dataframe['x']
        self.y_cor = dataframe['y']
        self.states_dict = {}
        coordinates = list(zip(self.x_cor, self.y_cor))

        for i in range(0, len(self.states)):
            self.states_dict[self.states[i]] = coordinates[i]

    def check_states(self, state_name):
        if state_name in self.states_dict.keys():
            self.x = self.states_dict[state_name][0]
            self.y = self.states_dict[state_name][1]
        else:
            return False
        location = (self.x, self.y)
        self.locate_state(location, state_name)
        return True

    def locate_state(self, location, state_name):
        self.hideturtle()
        self.penup()
        self.goto(location)
        self.write(state_name, font=FONT)

