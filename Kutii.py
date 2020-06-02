from python_neinformirano_prebaruvanje import *




def isValid(coveceto, box1, box2, box3):
    c_x, c_y = coveceto
    b1_x, b1_y = box1
    b2_x, b2_y = box2
    b3_x, b3_y = box3

    # coveceto da ne e nadvor od tablata
    if c_x < 0 or c_x > 7 or c_y < 0 or c_y > 9:
        return False

    # b1 da ne  e nadvor od tablata
    if b1_x < 0 or b1_x > 7 or b1_y < 0 or b1_y > 9:
        return False

    # b2 da ne  e nadvor od tablata
    if b2_x < 0 or b2_x > 7 or b2_y < 0 or b2_y > 9:
        return False

    # b3 da ne  e nadvor od tablata
    if b3_x < 0 or b3_x > 7 or b3_y < 0 or b3_y > 9:
        return False

    # coveceto da ne e ista pozicija so nekoja kutija 
    if ((c_x, c_y) == (b1_x, b1_y)) or ((c_x, c_y) == (b2_x, b2_y)) or ((c_x, c_y) == (b3_x, b3_y)): 
        return False

    # da nema dve kutii na ista pozicija 
    if ((b1_x, b1_y) == (b2_x, b2_y)) or ((b2_x, b2_y) == (b3_x, b3_y)) or ((b1_x, b1_y) == (b3_x, b3_y)):
        return False


    return True 


class KutiiLab(Problem):
    def __init__(self, initial):
        self.initial = initial

    def successors(self, state):
        successors = dict()

        #initial = covece, b1, b2, b3

        c = state[0]
        c_x, c_y = c
        b1 = state[1]
        b1_x, b1_y = b1
        b2 = state[2]
        b2_x, b2_y = b2
        b3 = state[3]
        b3_x, b3_y = b3


        #GoreC
        c_new = c_x - 1, c_y
        if isValid(c_new, b1, b2, b3):
            successors['GoreC'] = c_new, b1, b2, b3

        #DoluC
        c_new = c_x + 1, c_y
        if isValid(c_new, b1, b2, b3):
            successors['DoluC'] = c_new, b1, b2, b3

        #LevoC
        c_new = c_x, c_y - 1
        if isValid(c_new, b1, b2, b3):
            successors['DoluC'] = c_new, b1, b2, b3

        #DesnoC
        c_new = c_x, c_y + 1
        if isValid(c_new, b1, b2, b3):
            successors['DoluC'] = c_new, b1, b2, b3



        ##GoreCK
        # Gore CK1
        if (c_x - 1, c_y) == (b1_x, b1_y) and (b1 not in tocki):
            c_new = c_x - 1, c_y
            b1_new = b1_x - 1, b1_y
            if isValid(c_new, b1_new, b2, b3):
                successors['GoreCK'] = c_new, b1_new, b2, b3 

        # Gore CK2
        if (c_x - 1, c_y) == (b2_x, b2_y) and (b2 not in tocki):
            c_new = c_x - 1, c_y
            b2_new = b2_x - 1, b2_y
            if isValid(c_new, b1, b2_new, b3):
                successors['GoreCK'] = c_new, b1, b2_new, b3 

        # Gore CK3
        if (c_x - 1, c_y) == (b3_x, b3_y) and (b3 not in tocki):
            c_new = c_x - 1, c_y
            b3_new = b3_x - 1, b3_y
            if isValid(c_new, b1, b2, b3_new):
                successors['GoreCK'] = c_new, b1, b2, b3_new 


        ##DoluCK
        # Dolu CK1
        if (c_x + 1, c_y) == (b1_x, b1_y) and (b1 not in tocki):
            c_new = c_x + 1, c_y
            b1_new = b1_x + 1, b1_y
            if isValid(c_new, b1_new, b2, b3):
                successors['DoluCK'] = c_new, b1_new, b2, b3 

        # Dolu CK2
        if (c_x + 1, c_y) == (b2_x, b2_y) and (b2 not in tocki):
            c_new = c_x + 1, c_y
            b2_new = b2_x + 1, b2_y
            if isValid(c_new, b1, b2_new, b3):
                successors['DoluCK'] = c_new, b1, b2_new, b3 

        # Dolu CK3
        if (c_x + 1, c_y) == (b3_x, b3_y) and (b3 not in tocki):
            c_new = c_x + 1, c_y
            b3_new = b3_x + 1, b3_y
            if isValid(c_new, b1, b2, b3_new):
                successors['DoluCK'] = c_new, b1, b2, b3_new 



        ##LevoCK 
        # Levo CK1 
        if (c_x, c_y - 1) == (b1_x, b1_y) and (b1 not in tocki):
            c_new = c_x, c_y - 1
            b1_new = b1_x, b1_y - 1
            if isValid(c_new, b1_new, b2, b3):
                successors['LevoCK'] = c_new, b1_new, b2, b3

        # Levo CK2
        if (c_x, c_y - 1) == (b2_x, b2_y) and (b2 not in tocki):
            c_new = c_x, c_y - 1
            b2_new = b2_x, b2_y - 1
            if isValid(c_new, b1, b2_new, b3):
                successors['LevoCK'] = c_new, b1, b2_new, b3

        # Levo CK3
        if (c_x, c_y - 1) == (b3_x, b3_y) and (b3 not in tocki):
            c_new = c_x, c_y - 1
            b3_new = b3_x, b3_y - 1
            if isValid(c_new, b1, b2, b3_new):
                successors['LevoCK'] = c_new, b1, b2, b3_new


        
        ##DesnoCK
        # Desno CK1 
        if (c_x, c_y + 1) == (b1_x, b1_y) and (b1 not in tocki):
            c_new = c_x, c_y + 1
            b1_new = b1_x, b1_y + 1
            if isValid(c_new, b1_new, b2, b3):
                successors['DesnoCK'] = c_new, b1_new, b2, b3

        # Desno CK2
        if (c_x, c_y + 1) == (b2_x, b2_y) and (b2 not in tocki):
            c_new = c_x, c_y + 1
            b2_new = b2_x, b2_y + 1
            if isValid(c_new, b1, b2_new, b3):
                successors['DesnoCK'] = c_new, b1, b2_new, b3

        # Desno CK3
        if (c_x, c_y + 1) == (b3_x, b3_y) and (b3 not in tocki):
            c_new = c_x, c_y + 1
            b3_new = b3_x, b3_y + 1
            if isValid(c_new, b1, b2, b3_new):
                successors['DesnoCK'] = c_new, b1, b2, b3_new



        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        b1 = state[1]
        b2 = state[2]
        b3 = state[3]
        
        flag = False
        if (b1 in tocki) and (b2 in tocki) and (b3 in tocki) and (b1 != b2) and (b2 != b3) and (b1 != b3):
            flag = True
        
        return flag


    def result(self, state):
        possible = self.successor(state)
        return possible[action]

    def h(self, node):
        player, stars, links = node.state
        star1, star2, star3 = stars
        min_score = 9999999999
        for star in stars:
            dist = self.ed(points[player], points[stars])
            if dist < min_score:
                min_score = dist
        return min_score
        # shoud be
        return ed(points[player], points[star1]) + ed(points[star1], points[star2]) + ed(points[star2], points[star3])

def ed(point1, point2):
    return ((point1[0]-point1[1])**2 + (point1[1]-point2[1])**2)**1/2



man_row = 0#int(input())
man_column = 5#int(input())
b1_row = 2#int(input())
b1_column = 2#int(input())
b2_row = 1#int(input())
b2_column = 5#int(input())
b3_row = 2#int(input())
b3_column = 9#int(input())

covece = man_row, man_column
b1 = b1_row, b1_column
b2 = b2_row, b2_column
b3 = b3_row, b3_column

tocki = (2,3), (2,5), (2,7)

############################  
initial = covece, b1, b2, b3
############################ 

instanca = KutiiLab(initial)
answer = breadth_first_graph_search(instanca)
print(answer.solution())