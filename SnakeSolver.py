from python_neinformirano_prebaruvanje import *


def getDirection(current, new):

    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    #             dolu  desno  gore   levo

    if new == "SvrtiLevo":
        return directions[(directions.index(current) + 1) % 4]

    elif new == "SvrtiDesno":
        return directions[(directions.index(current) - 1) % 4]
    # (gore - 2) % 4 , dolu % 4 
    else:
        return current


def isValid(state):
      
    new_head_x = state[0][-1][0]
    new_head_y = state[0][-1][1]

    # ako glavata od zmijata e nadvor od tabla 
    if new_head_x < 0 or new_head_x > 9 or new_head_y < 0 or new_head_y > 9:
        return False

    # ako zmijata imat kasnato crveno jabolko 
    if (new_head_x, new_head_y) in state[2]:
        return False

    # ako zmijata se imat kasnato sama sebe 
    if len(state[0]) != len(set(state[0])):
        return False
    
    # ne funkcionirat ova !!!
    #for i in range(len(state[1])-1):
    #   if state[1][i] == state[1][-1]:
    #       return False 

    return True    

class Snake(Problem):
    def __init__(self, initial):
        self.initial = initial
         
    def successor(self, state):
        successors = dict()

        possible = "ProdolzhiPravo SvrtiLevo SvrtiDesno".split()
        for posakuvana in possible:
            direction = getDirection(state[-1], posakuvana)
            new_head_position = state[0][-1][0] + direction[0], state[0][-1][1] + direction[1]

            if new_head_position in state[1]:
                snake_cords = state[0] + tuple([new_head_position])
                
                new_green = list(state[1])
                new_green.remove(new_head_position)
                new_green = tuple(new_green)

                successors[posakuvana] =  snake_cords, new_green, state[2], direction 

            else:
                #snake_cords = tuple(list(state[0])[1:] + [new_head_position])  
                snake_cords = (state[0])[1:] + tuple([new_head_position])
                state_new =  snake_cords, state[1], state[2], direction 
                if isValid(state_new):
                    successors[posakuvana] = state_new
        

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return len(state[1]) == 0

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


n = int(input())
zeleni_jabolka = [tuple(map(int, input().split(','))) for _ in range(n)]
m = int(input())
crveni_jabolka = [tuple(map(int, input().split(','))) for _ in range(m)]

initial =  ((0,0),(1,0),(2,0)), tuple(zeleni_jabolka), tuple(crveni_jabolka), (1,0) 

instanca = Snake(initial)
answer = breadth_first_graph_search(instanca)
print(answer.solution())