from python_neinformirano_prebaruvanje import *


class TenkProba(Problem):
    def __init__(self, initial):
        self.initial = initial

    def successor(self, state):
        successors = dict()

        for i in range(n):
            for j in range(n):
                matrix = [[list(state[m]) for m in range(n*x, n*(x+1))] for x in range(n)]
                
                if matrix[i][j][1] == "Projectile":
                    
                    # najdi go najgliskiot tenk gore 
                    if i > 0:
                        for brojac in range(i-1, -1, -1):
                            if matrix[brojac][j][0] != 'X':
                                if matrix[brojac][j][0] == 0:
                                    matrix[brojac][j] = 'X', "Projectile"
                                else:
                                    matrix[brojac][j][0] -= 1 
                                break

                    # najdi go najbliskiot tenk dolu
                    if i < n-1:
                        for brojac in range(i+1, n, 1):
                            if matrix[brojac][j][0] != 'X':
                                if matrix[brojac][j][0] == 0:
                                    matrix[brojac][j] = 'X', "Projectile"
                                else:
                                    matrix[brojac][j][0] -= 1 
                                break

                    # najdi go najbliskiot tenk levo
                    if j > 0:
                        for brojac in range(j-1, -1, -1):
                            if matrix[i][brojac][0] != 'X':
                                if matrix[i][brojac][0] == 0:
                                    matrix[i][brojac] = 'X', "Projectile"
                                else:
                                    matrix[i][brojac][0] -= 1 
                                break

                    # najdi go najbliskiot tenk desno
                    if j < n-1:
                        for brojac in range(j+1, n, 1):
                            if matrix[i][brojac][0] != 'X':
                                if matrix[i][brojac][0] == 0:
                                    matrix[i][brojac] = 'X', "Projectile"
                                else:
                                    matrix[i][brojac][0] -= 1 
                                break


                    tuple_of_elements = tuple(tuple(element) for row in matrix for element in row)
                    successors[f'ProjectileActivated on ({i},{j})'] = tuple_of_elements


                else: # ako nema aktiven projectile na toa pole 
                    if matrix[i][j][0] != 'X':
                        if matrix[i][j][0] == 0:
                            matrix[i][j] = 'X', "Projectile"
                        else:
                            matrix[i][j][0] -= 1
                        
                        tuple_of_elements = tuple(tuple(element) for row in matrix for element in row)
                        successors[f'PlayerShoot on ({i},{j})'] = tuple_of_elements

                         
 

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        # site polinja da se 'X'
        # state is ((vrednost, projectile), (vrednost, projectile),...)
        flag = True
        for i in range(n*n):
            if state[i][0] != 'X':
                flag = False
        return flag


    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


n = 4 
tanks = ((1, 0, 1), (3, 1, 2), (0, 2, 1), (1, 2, 1), (2, 2, 1), (1, 3, 1), (3, 3, 1))

tanks_lista = []
# (vrednost, projectile), (vrednost, projectile)

for i in range(n*n):
    flag = True
    for tank in tanks:
        if tank[0]*n + tank[1] == i:
            tanks_lista.append((tank[2], "noProjectile"))
            flag = False
    if flag:
        tanks_lista.append(('X', "noProjectile"))

initial = tuple(tanks_lista)

instanca = TenkProba(initial)
answer = breadth_first_graph_search(instanca)
print(answer.solution())


