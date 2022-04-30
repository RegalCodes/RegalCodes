import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# turtle.hideturtle()
turtle.penup()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")


        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # or can do t.write(state_data.state.item()) to pull from the data frame.
        # print(guessed_states)

# states_to_learn.csv

# screen.exitonclick()

#
#
# game_not_over = True
#
# while game_not_over == True:
#     for correct_answer in state_list:
#         if answer_state == correct_answer:
#             print("Correct")
#             turtle.write(answer_state, True)
#         elif answer_state != correct_answer:
#             print("False")
#             game_not_over = False
#
#
#


