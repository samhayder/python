from turtle import Turtle,Screen
import pandas

US_IMAGE_PATH = "0_UDEMY_ANGELA_YU/3_projects/25_pandas_games/u.s_states/blank_states_img.gif"
US_STATES_CSV_PATH = "0_UDEMY_ANGELA_YU/3_projects/25_pandas_games/u.s_states/50_states.csv"
MISSING_STATE_PATH = "0_UDEMY_ANGELA_YU/3_projects/25_pandas_games/u.s_states/"

screen = Screen()
screen.title("US States Guessing Game.")
screen.addshape(US_IMAGE_PATH)
turtle = Turtle()
turtle.shape(US_IMAGE_PATH)

data = pandas.read_csv(US_STATES_CSV_PATH)
all_states = data['state'].to_list()
guess_state = []

while len(guess_state) < 50:
    turtle.showturtle()
    
    guess_state_name =screen.textinput(title=f"{len(guess_state)}/50 Guess the State", prompt="What's another State name?").title()

    if guess_state_name == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv(f"{MISSING_STATE_PATH}missing_state_name.csv")
        break
    
    if guess_state_name in all_states:
        state_data = data[data.state == guess_state_name]
        guess_state.append(state_data)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(x=state_data.x.item(), y=state_data.y.item())
        turtle.write(guess_state_name)


screen.exitonclick()