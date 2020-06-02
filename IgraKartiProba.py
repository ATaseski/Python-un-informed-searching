from python_neinformirano_prebaruvanje import *

def teleportiraj(covece_x, covece_y):
    # karti = ((0, 0, 'Tref'), (1, 0, 'Karo'),....)
    for karta in karti:
        if karta[0] == covece_x and karta[1] == covece_y:
            for drugaKarta in karti:
                if drugaKarta[2] == karta[2] and (drugaKarta[0] != covece_x or drugaKarta[1] != covece_y):
                    covece_new = drugaKarta[0], drugaKarta[1] 
              
    return covece_new


class KartiProbaa(Problem):

    def __init__(self, initial):
        self.initial = initial

    def successor(self, state):
        successors = dict()

        # state is (covece, polinja)
        # polinja sodrzat (vrednost, nasoka) 

        x, y = state[0]
        polinja = state[1]

        matrix =[[list(polinja[m]) for m in range(n*x, n*(x+1))] for x in range(n)]
         
        ## Desno 
        if y < 4 and matrix[x][y+1][1] != 'ZabranetoPole':
            if matrix[x][y][1] == 'Seedno' or matrix[x][y][1] == 'Desno':
                if matrix[x][y][0] > 0:
                    matrix[x][y][0] -= 1
                if matrix[x][y+1][1] == 'Teleportiraj':
                    covece_new = teleportiraj(x, y + 1)
                else:
                    covece_new = x, y + 1

                # matrix is list of lists, need to be tuple of tuples 
                tuple_of_elements = tuple(tuple(element) for row in matrix for element in row)
                successors['Desno'] = covece_new, tuple_of_elements



        ## Levo
        if y > 0 and matrix[x][y-1][1] != 'ZabranetoPole':
            if matrix[x][y][1] == 'Seedno' or matrix[x][y][1] == 'Levo':
                if matrix[x][y][0] > 0:
                    matrix[x][y][0] -= 1
                if matrix[x][y-1][1] == 'Teleportiraj':
                    covece_new = teleportiraj(x, y - 1)
                else:
                    covece_new = x, y - 1

                mat_tuple = tuple(tuple(element) for row in matrix for element in row)
                successors['Levo'] = covece_new, mat_tuple


        ## Dolu 
        if x < 4 and matrix[x+1][y][1] != 'ZabranetoPole':
            if matrix[x][y][1] == 'Seedno' or matrix[x][y][1] == 'Dolu':
                if matrix[x][y][0] > 0:
                    matrix[x][y][0] -= 1
                if matrix[x+1][y][1] == 'Teleportiraj':
                    covece_new = teleportiraj(x + 1, y)
                else:
                    covece_new = x + 1, y 

                mat_tuple = tuple(tuple(element) for row in matrix for element in row)
                successors['Dolu'] = covece_new, mat_tuple


        ## Gore 
        if x > 0 and matrix[x-1][y][1] != 'ZabranetoPole':
            if matrix[x][y][1] == 'Seedno' or matrix[x][y][1] == 'Gore':
                if matrix[x][y][0] > 0:
                    matrix[x][y][0] -= 1
                if matrix[x-1][y][1] == 'Teleportiraj':
                    covece_new = teleportiraj(x - 1, y)
                else:
                    covece_new = x - 1, y 

                mat_tuple = tuple(tuple(element) for row in matrix for element in row)
                successors['Gore'] = covece_new, mat_tuple

        return successors



    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
         
        flag = True
        polinija = state[1]

        #vrednostiKoordinati = ((0, 1), (0, 2), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2))

        for i in range(n):
            for j in range(n):
                for i,j in vrednostiKoordinati:
                    if polinija[i*n+j][0] != 0:
                        flag = False
                        break
        return flag 
         
    
    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


#####################################################################################################################################


n = 5

igracRedica = 4 # = input()
igracKolona = 0 # = input()
covece = igracRedica, igracKolona

vrednosti = "0,0,1,2,0,0,1,0,1,1,0,0,1,1"#input()
vrednosti = [int(x) for x in vrednosti.split(',')]
vrednostiKoordinati = ((0, 1), (0, 2), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2))
vrednostiFinal = []
for i in range(0, len(vrednostiKoordinati)):
    vrednostiFinal.append((vrednostiKoordinati[i][0], vrednostiKoordinati[i][1], vrednosti[i]))
vrednostiFinal = tuple(vrednostiFinal)

karti = ((0, 0, 'Tref'), (1, 0, 'Karo'), (1, 1, 'List'), (1, 4, 'Srce'), (2, 3, 'List'),(3, 4, 'Tref'), (4, 3, 'Karo'), (4, 4, 'Srce'))

strelka1Redica = 2#input()
strelka1Kolona = 0#input()
strelka1Nasoka = "Desno"#input()
strelka2Redica = 3#input()
strelka2Kolona = 1#input()
strelka2Nasoka = "Dolu"#input()
strelki = ((strelka1Redica, strelka1Kolona, strelka1Nasoka), (strelka2Redica, strelka2Kolona, strelka2Nasoka))

 
matrixInitial = []
for x in range(n):
    row = []
    for y in range(n):
        flag = True 
        for karta in karti:
            if x == karta[0] and y == karta[1]:
                flag = False
                row.append((karta[2], 'Teleportiraj'))
        for vrednost in vrednostiFinal:
            if x == vrednost[0] and y == vrednost[1]:
                flag = False
                if vrednost[0] == strelka1Redica and vrednost[1] == strelka1Kolona:
                    row.append((vrednost[2], strelka1Nasoka))
                elif vrednost[0] == strelka2Redica and vrednost[1] == strelka2Kolona:
                    row.append((vrednost[2], strelka2Nasoka))
                else:
                    row.append((vrednost[2], 'Seedno'))
        if flag:
            row.append(('X','ZabranetoPole'))
             
    matrixInitial.append(row)

 
polinja_initial = tuple(element for row in matrixInitial for element in row)  

initial = covece, polinja_initial
 
instanca = KartiProbaa(initial)
answer = breadth_first_graph_search(instanca)
print(answer.solution())

