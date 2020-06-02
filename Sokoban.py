from python_neinformirano_prebaruvanje import *




polinja = ((0,3), (0,4), (0,6), (0,7), (1,2), (1,3), (1,4), (1,6), (1,7), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (3,2), (3,3), (3,6), (3,7), (4,2), (4,3), (4,4), (4,6), (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6))

stars = ((5,0), (5,1), (5,2), (5,3), (5,4))


def isValid(c, b):
    b1, b2, b3, b4, b5 = b
    # b = (b1, b2, b3, b4, b5)

    # kutiite da se na razlicni pozicii
    b_list = list(b)
    for i in range(len(b)):
        for j in range(len(b)):
            if i != j:
                if b[i] == b[j]:
                    return False

    # coveceto da ne e na ista pozicija so nekoja kutija 
    if c == b1 or c == b2 or c == b3 or c == b4 or c == b5:
        return False

    # kutiite da ne se nadvor od tabla
    for box in b:
        if box not in polinja:
            return False

    # coveceto da ne e nadvor od tabla
    if c not in polinja:
        return False


    return True


def isNeighbours(b1, b2):
    b1_x, b1_y = b1
    b2_x, b2_y = b2

    if b1_x == b2_x and abs(b1_y - b2_y) == 1:
        return True

    if b1_y == b2_y and abs(b1_x - b2_x) == 1:
        return True

    return False


def deadlock(c, b):
    
    b1, b2, b3, b4, b5 = b
    # ako dve kutii se edna do druga
    # barem ednata kutija morat da imat slobodno pole od dve sprotivni strani 

    polinjaFree = [pole for pole in polinja if pole != b1 if pole != b2 if pole != b3 if pole != b4 if pole != b5]

    flag = False

    b_list = list(b)
    
    for i in range(len(b)):
        for j in range(len(b)):
            if i != j: 
                if isNeighbours(b[i], b[j]):
                    if b[i][0] - 1 in polinjaFree and b[i][0] + 1 in polinjaFree:
                        flag = False
                    elif b[i][1] - 1 in polinjaFree and b[i][1] + 1 in polinjaFree:
                        flag = False
                    elif b[j][0] - 1 in polinjaFree and b[j][0] + 1 in polinjaFree:
                        flag = False
                    elif b[j][1] - 1 in polinjaFree and b[j][1] + 1 in polinjaFree:
                        flag = False
                    else:
                        flag = True

    return flag



def thereIsBox(covece_new, boxes):
    flag = False
    for box in boxes:
        if box[0] == covece_new[0] and box[1] == covece_new[1]:
            flag = True

    return flag 




class Sokoban(Problem):
    def __init__(self, initial):
        self.initial = initial

    def successor(self, state):
        successors = dict()
        covece = state[0]
        boxes = state[1]
        b1, b2, b3, b4, b5 = boxes

        polinjaFree = [pole for pole in polinja if pole != b1 if pole != b2 if pole != b3 if pole != b4 if pole != b5]


        ################### go #######################
        ## goUp
        covece_new = covece[0] + 1, covece[1]
        if covece_new in polinjaFree:
            if isValid(covece_new, boxes):
                successors['goUp'] = covece_new, boxes

        ## goDown
        covece_new = covece[0] - 1, covece[1]
        if covece_new in polinjaFree:
            if isValid(covece_new, boxes):
                successors['goDown'] = covece_new, boxes

        ## goLeft
        covece_new = covece[0], covece[1] - 1
        if covece_new in polinjaFree:
            if isValid(covece_new, boxes):
                successors['goLeft'] = covece_new, boxes

        ## goRight
        covece_new = covece[0], covece[1] + 1
        if covece_new in polinjaFree:
            if isValid(covece_new, boxes):
                successors['goRight'] = covece_new, boxes



        ################### push #######################
        
        b1_new = b1
        b2_new = b2
        b3_new = b3
        b4_new = b4
        b5_new = b5        

        state_new = state      

        ## pushUp
        covece_new = covece[0] + 1, covece[1]
        if thereIsBox(covece_new, boxes):
            if covece_new == b1 and b1 not in stars:
                b1_new = b1[0] + 1, b1[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b2 and b2 not in stars:
                b2_new = b2[0] + 1, b2[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b3 and b3 not in stars:
                b3_new = b3[0] + 1, b3[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b4 and b4 not in stars:
                b4_new = b4[0] + 1, b4[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b5 and b5 not in stars:
                b5_new = b5[0] + 1, b5[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new


            if state_new != state:
                successors['pushUp'] = state_new



        ## pushDown
        covece_new = covece[0] - 1, covece[1]
        if thereIsBox(covece_new, boxes):
            if covece_new == b1 and b1 not in stars:
                b1_new = b1[0] - 1, b1[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b2 and b2 not in stars:
                b2_new = b2[0] - 1, b2[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b3 and b3 not in stars:
                b3_new = b3[0] - 1, b3[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b4 and b4 not in stars:
                b4_new = b4[0] - 1, b4[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b5 and b5 not in stars:
                b5_new = b5[0] - 1, b5[1]
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new


            if state_new != state:
                successors['pushDown'] = state_new


        ## pushRight
        covece_new = covece[0], covece[1] + 1
        if thereIsBox(covece_new, boxes):
            if covece_new == b1 and b1 not in stars:
                b1_new = b1[0], b1[1] + 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b2 and b2 not in stars:
                b2_new = b2[0], b2[1] + 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b3 and b3 not in stars:
                b3_new = b3[0], b3[1] + 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b4 and b4 not in stars:
                b4_new = b4[0], b4[1] + 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b5 and b5 not in stars:
                b5_new = b5[0], b5[1] + 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new


            if state_new != state:
                successors['pushRight'] = state_new



        ## pushLeft
        covece_new = covece[0], covece[1] - 1
        if thereIsBox(covece_new, boxes):
            if covece_new == b1 and b1 not in stars:
                b1_new = b1[0], b1[1] - 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b2 and b2 not in stars:
                b2_new = b2[0], b2[1] - 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b3 and b3 not in stars:
                b3_new = b3[0], b3[1] - 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b4 and b4 not in stars:
                b4_new = b4[0], b4[1] - 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new

            if covece_new == b5 and b5 not in stars:
                b5_new = b5[0], b5[1] - 1
                boxes_new = b1_new, b2_new, b3_new, b4_new, b5_new
                if isValid(covece_new, boxes_new) and not deadlock(covece_new, boxes_new):
                    state_new = covece_new, boxes_new


            if state_new != state:
                successors['pushLeft'] = state_new



        return successors



    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):

        flag = False

        c = state[0]
        b = state[1]
        b1, b2, b3, b4, b5 = b 

        razlicni = True
        b_list = list(b)
        for i in range(len(b)):
            for j in range(len(b)):
                if i != j:
                    if b[i] == b[j]:
                        razlicni = False

        if razlicni:
            if b1 in stars and b2 in stars and b3 in stars and b4 in stars and b5 in stars:
                flag = True

        return flag

    
    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]



covece = (0,7)
b1 = (2,2)
b2 = (3,3)
b3 = (4,3)
b4 = (2,4)
b5 = (2,6)
boxes = b1, b2, b3, b4, b5


#######################
initial = covece, boxes
#######################

instanca = Sokoban(initial)
answer = breadth_first_graph_search(instanca)
print(answer.solution())