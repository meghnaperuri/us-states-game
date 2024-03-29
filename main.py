import turtle
import pandas

screen = turtle.Screen()
lola=turtle.Turtle()
screen.title("US States game")

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
missing_states = []
empty_df=pandas.DataFrame()
empty_df.to_csv("states_to_learn.csv")
data = pandas.read_csv("50_states.csv", encoding='ISO-8859-1')
# print(data)
all_states = list(data.state)
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="state name: ").lower()
    # print(answer_state)
    # answer_state="ohio"
    # print(all_states)
    data1 = data[data["state"].str.lower() == answer_state]
    if not data1.empty:
        guessed_states.append(answer_state)
        x=data1["x"].iloc[0]
        y=data1["y"].iloc[0]
        # print(data1)
        # print(x,y)
        lola.penup()
        lola.hideturtle()
        lola.goto(x, y)
        lola.write(answer_state, font=("Arial",12,"normal"))
        guessed_state_original_case = data1["state"].iloc[0]
        all_states.remove(guessed_state_original_case)
        print(all_states)
    elif answer_state=="exit":
        # screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="game over. ")
        # print("wrong state.")
        lola.penup()
        lola.hideturtle()
        lola.goto(-85,0)
        lola.write(f"game over. your score is {len(guessed_states)} ", font=("Courier",18,"normal"))
        missing_states=all_states
        print(all_states)
        print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

screen.mainloop()