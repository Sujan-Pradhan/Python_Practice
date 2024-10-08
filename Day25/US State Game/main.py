import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. State Game')
image = 'blank_states_img.gif'

screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")

all_states = data.state.to_list()

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 States Correct", prompt="What's another state's name?")
    # print(answer_state)

    if answer_state == "EXIT":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_Data = pd.DataFrame(missing_states)  
        new_Data.to_csv("states_to_learn.csv") 
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item())
        t.write(answer_state)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()





screen.exitonclick()