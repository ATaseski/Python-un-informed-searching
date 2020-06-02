from python_neinformirano_prebaruvanje import *
 

 

class Tenk(Problem):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        successors = dict()
        
        for i in range(n):
            for j in range(n): 
                matrix = [[state[m] for m in range(n*x, n*(x+1))] for x in range(n)]

                if matrix[i][j] != 'X': 
                
                    # if projectile
                    if matrix[i][j] == 0: 

                        matrix[i][j] = 'X'
                        # najdi go najbliskiot tenk gore 
                        if i > 0:
                            for brojac in range(i-1, -1, -1):
                                if matrix[brojac][j] != 'X':
                                    if matrix[brojac][j] == 0:
                                        matrix[brojac][j] = 'X'
                                         
                                    else:
                                        matrix[brojac][j] -= 1
                                    break
                        # najdi go najbliskiot tenk dolu 
                        if i < n:
                            for brojac in range(i+1, 4, 1):
                                if matrix[brojac][j] != 'X':
                                    if matrix[brojac][j] == 0:
                                        matrix[brojac][j] = 'X'
                                         
                                    else:
                                        matrix[brojac][j] -= 1
                                    break
                        # najdi go najbliskiot tenk levo
                        if j > 0:
                            for brojac in range(j-1, -1, -1):
                                if matrix[i][brojac] != 'X':
                                    if matrix[i][brojac] == 0:
                                        matrix[i][brojac] = 'X'
                                         
                                    else:
                                        matrix[i][brojac] -= 1
                                    break
                        # najdi go najbliskiot tenk desno
                        if j < n:
                            for brojac in range(j+1, 4, 1):
                                if matrix[i][brojac] != 'X':
                                    if matrix[i][brojac] == 0:
                                        matrix[i][brojac] = 'X'
                                         
                                    else:
                                        matrix[i][brojac] -= 1
                                    break

                        list_of_elements =  [element for row in matrix for element in row]
                        tuple_of_elements = tuple(list_of_elements)
                        successors[f'{i},{j}'] = tuple_of_elements


                    # if no projecile 
                    else:  
                        matrix[i][j] -= 1
                        list_of_elements =  [element for row in matrix for element in row]
                        tuple_of_elements = tuple(list_of_elements)
                        successors[f'{i},{j}'] = tuple_of_elements
                         
      

        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


n = 4 
tanks = ((1, 0, 1), (3, 1, 2), (0, 2, 1), (1, 2, 1), (2, 2, 1), (1, 3, 1), (3, 3, 1))

lista = []
for i in range(n*n):
    flag = True
    for tank in tanks:
        if tank[0]*n + tank[1] == i:
            lista.append(tank[2])
            flag = False
    if flag:
        lista.append('X')

initial = tuple(lista)

 
goal = tuple(['X' for _ in range(n*n)])

instanca = Tenk(initial, goal)
answer = breadth_first_graph_search(instanca)
print(answer.solution())
