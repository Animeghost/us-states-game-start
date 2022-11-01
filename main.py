import turtle
import pandas
import state_name


state=pandas.read_csv("C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 25/us-states-game-start/50_states.csv")
screen = turtle.Screen()
screen.title('U.S states Game')
image = "C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)

start = True
turtle.shape(image)
oyo = turtle.Turtle()
oyo.penup()
oyo.hideturtle()
listed_states = []
score = 0
while score < 50:
    answer_state = screen.textinput(title=f"{score}/ 50 guess the state",prompt="what's another state name?").title()
    list=state['state'].to_list() 
    if answer_state == 'Exit':
        break
    for x in list:
        if answer_state == x and answer_state not in listed_states :
            listed_states.append(answer_state)
            oyo.goto(state_name.state_cor(answer_state))
            oyo.write(arg=answer_state,move=False,align='center')
            score += 1

failed = [x for x in list if x not in listed_states]

print(failed)

data = pandas.DataFrame(failed)
data.to_csv('C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 25/us-states-game-start/states to learn.csv')