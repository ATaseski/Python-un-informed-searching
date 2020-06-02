from python_neinformirano_prebaruvanje import *



'''
Od input se cita:
n - goleminata na nizata
m - brojot na polinja koj ke bidat popolneti
broevi - vrednosti na prvite m - polinja
cel: broevite da se naredat vo sortiracki redosled pocnuvajki od n - m , do n
  
primer input: n = 10, m = 4, brovi = "3,4,2,1"
pocetna sostojba ke e    :  3,4,2,1,x,x,x,x,x,x
celna sostojba treba da e:  x,x,x,x,x,x,1,2,3,4 
'''

'''
def make_swap(positon_x, positon_y):
    niza = state
    nova_niza = []
    pos_x = positon_x  
    pos_y = positon_y  

    for i in range(pos_x): # fakticki od 0 do pos_x - 1, poso posledniot broj ne vlegvit vo opseg 
        nova_niza.append(niza[i]) 
    nova_niza.append(niza[pos_y])
    for i in range(pos_x + 1, pos_y):
        nova_niza.append(niza[i])
    nova_niza.append(niza[pos_x])
    for i in range(pos_y + 1, len(niza)):
        nova_niza.append(niza[i])
'''

def swap(niza, pozicija_x, pozicija_y):
    
    niza = list(niza)
    vrednost_pozicija_x = niza[pozicija_x]
    vrednost_pozicija_y = niza[pozicija_y]
    niza[pozicija_x] = vrednost_pozicija_y
    niza[pozicija_y] = vrednost_pozicija_x

    return tuple(niza)



class nizaJanuari(Problem):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        successors = dict()
        
        #niza = state
          
        for i in range(n):
            for j in range(i+1, n):
                #successors[f'Swap position {i} and position {j}'] = swap(state, i, j)
                successors[f'Swap {state[i]} and {state[j]}'] = swap(state, i, j)



        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return state == self.goal


    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


n = 10 # input()
m = 4 # input()
#broevi = list(map(int, input().split(',')))
broevi = [3,4,2,1]
 
lista_initial = []
for i in range(m):
    lista_initial.append(broevi[i])
for i in range(n-m):
    lista_initial.append('x')

initial = tuple(lista_initial)

 
broevi_sortirani = list(set(broevi))
lista_goal = []
for i in range(n-m):
    lista_goal.append('x')
for i in range(m):
    lista_goal.append(broevi_sortirani[i])

goal = tuple(lista_goal)


instanca = nizaJanuari(initial, goal)
answer = breadth_first_graph_search(instanca)

numberOfSwaps = answer.path_cost

print(f'Number of swaps required: {numberOfSwaps}')
print(f'Solution:')
for swapce in answer.solution():
    print(swapce)
#print(answer.solution())
 