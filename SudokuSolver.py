from python_neinformirano_prebaruvanje import *


def isValid(mat, num, pos):
   
    # check column
    for i in range(len(mat)):  # len(mat) return number od rows 
        if mat[i][pos[1]] == num and pos[0] != i:   
            return False

    # check row
    for j in range(len(mat[0])):  # len(mat[0]) return number of cols
        if mat[pos[0]][j] == num and pos[1] != j: 
            return False

    # check box 
    box_x = pos[0] // 3 
    box_y = pos[1] // 3
    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if mat[i][j] == num and (i,j) != pos:
                return False

    return True



class Sudoku(Problem):
    def __init__(self, initial):
        self.initial = initial

    def successor(self, state):
        successors = dict()

        for i in range(n):
            for j in range(n):
                matrix = [[state[m] for m in range(n*x, n*(x+1))] for x in range(n)]
                if matrix[i][j] == 0:
                    for broj in range(1,10):
                        pozicija = (i,j)
                        if isValid(matrix, broj, pozicija):
                            matrix[i][j] = broj
                            successors[f'{i},{j} = {broj}'] = tuple([element for row in matrix for element in row])  



        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
         
        for i in range(n*n):
            if state[i] == 0:
                return False
        return True


    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]




n = 9  # golemina na tabla 
vrednosti = "0,0,0,0,0,8,0,0,4,0,8,4,0,1,6,0,0,0,0,0,0,5,0,0,1,0,0,1,0,3,8,0,0,9,0,0,6,0,8,0,0,0,4,0,3,0,0,2,0,0,9,5,0,1,0,0,7,0,0,2,0,0,0,0,0,0,7,8,0,2,6,0,2,0,0,3,0,0,0,0,0"
vrednosti = [int(x) for x in vrednosti.split(',')]
vrednosti = tuple(vrednosti)
 
initial = vrednosti
 
instanca = Sudoku(initial)
answer = breadth_first_graph_search(instanca)
print(answer.solution())