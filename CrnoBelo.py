from python_neinformirano_prebaruvanje import *

class CrnoBelo(Problem):
    def __init__(self,initial, goal):
        self.initial = initial
        self.goal = goal
    
    def successor(self,state):
        successors = dict()

        for x in range(n):
            for y in range(n):
                matrix = [[state[m] for m in range(n*row,n*(row+1))] for row in range(n)]                
                                                                                #len(cols)
                matrix[x][y] = (1 if matrix[x][y] == 0 else 0)
                if x+1 < n:
                    matrix[x+1][y] = (1 if matrix[x+1][y] == 0 else 0)
                if x-1 >= 0:
                    matrix[x-1][y] = (1 if matrix[x-1][y] == 0 else 0)
                if y+1 < n:
                    matrix[x][y+1] = (1 if matrix[x][y+1] == 0 else 0)
                if y-1 >= 0:
                    matrix[x][y-1] = (1 if matrix[x][y-1] == 0 else 0)
                    
                list_of_elements = [element for redica in matrix for element in redica]
                tuple_of_elements = tuple(list_of_elements)
                successors[f'x: {x}, y: {y}'] = tuple_of_elements
        
        return successors
    
    def actions(self,state):
        return self.successor(state).keys()
    
    def goal_test(self, state):
        return self.goal == state
    
    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]

    #Hamingovo rastojanie
    #def h(self, node):
    #    state = node.state
    #    vrednost = 0
    #    for i in range(0, len(state)):
    #        if state[i] != self.goal[i]:
    #            vrednost = vrednost + 1
    #    return vrednost

    
#n = int(input())
n = 3
#polinja = list(map(int, input().split(',')))
polinja = [0,0,0,1,0,0,1,1,0]

polinja = tuple(polinja)

initial = polinja 

goal = tuple([1 for _ in range(n*n)])

instanca = CrnoBelo(initial, goal)

answer = breadth_first_graph_search(instanca)

print(answer.solution())