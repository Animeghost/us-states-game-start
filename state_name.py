import pandas

state=pandas.read_csv("C:/Users/bassey/Desktop/PYTHON CODES/100 days/day 25/us-states-game-start/50_states.csv")
list=state['state'].to_list() 

def state_cor(name):
    x= state[state['state'] == name]
    cor = (int(x.x),int(x.y))
    return cor


x= state[state['state'] == 'Ohio']
cor = (int(x.x),int(x.y))
print(cor)