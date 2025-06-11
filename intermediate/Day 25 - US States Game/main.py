import turtle
import pandas as pd
from pytz import all_timezones_set

from place_state import PlaceState

screen = turtle.Screen()
screen.setup(725,491)
screen.title("U.S States game")
screen.bgpic("blank_states_img.gif")
df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = []
        for actual_state in all_states:
            if not actual_state in guessed_states:
                state_data = df[df.state == actual_state]
                PlaceState(state_data.state.item(), state_data.x.item(), state_data.y.item(), "red")
                missing_states.append(actual_state)
        new_df = pd.DataFrame(missing_states, columns=["state"])
        new_df.to_csv("states_to_learn.csv")
        break
    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        state_data = df[df.state == answer]
        PlaceState(state_data.state.item(), state_data.x.item(), state_data.y.item(), "green")

screen.exitonclick()