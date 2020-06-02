from python_neinformirano_prebaruvanje import *


precki = ((5, 0), (5, 1), (3, 1), (1, 2), (0, 3), (0, 5), (0, 7), (1, 8), (5, 3), (4, 4), (5, 6), (4, 6), (3, 6), (3, 7))


def isValid(h1, o, h2):
    h1_x, h1_y = h1
    o_x, o_y = o
    h2_x, h2_y = h2

    # molekulite da ne se nadvor od tabla  
    if h1_x < 0 or h1_x > 6 or h1_y < 0 or h1_y > 8 or o_x < 0 or o_x > 6 or o_y < 0 or o_y > 8 or h2_x < 0 or h2_x > 6 or h2_y < 0 or h2_y > 8:
        return False

    # da nema dve molekuli na ista pozicija
    if (h1_x == o_x and h1_y == o_y) or (h1_x == h2_x and h1_y == h2_y) or (o_x == h2_x and o_y == h2_y):
        return False

    # da nema molekula na ista pozicija so nekoja precka 
    if (h1_x, h1_y) in precki:
        return False
    if (o_x, o_y) in precki:
        return False
    if (h2_x, h2_y) in precki:
        return False

    return True


class Molekula(Problem):
    def __init__(self, initial):
        self.initial = initial

    def successors(self, state):
        successors = dict()

        h1_x, h1_y = state[0]
        o_x, o_y = state[1] 
        h2_x, h2_y = state[2]


        ### move H1 atom ###
        # H1 gore
        possible_state_new = (h1_x - 1, h1_y), (o_x, o_y), (h2_x, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0] - 1, state_new[0][1]), (state_new[1][0], state_new[1][1]), (state_new[2][0], state_new[2][1])
            successors['GoreH1'] = state_new 

        # H1 dolu
        possible_state_new = (h1_x + 1, h1_y), (o_x, o_y), (h2_x, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0] + 1, state_new[0][1]), (state_new[1][0], state_new[1][1]), (state_new[2][0], state_new[2][1])
            successors['DoluH1'] = state_new 

        # H1 levo
        possible_state_new = (h1_x, h1_y - 1), (o_x, o_y), (h2_x, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1] - 1), (state_new[1][0], state_new[1][1]), (state_new[2][0], state_new[2][1])
            successors['LevoH1'] = state_new 

        # H1 desno
        if isValid(*possible_state_new):
            possible_state_new = (h1_x, h1_y + 1), (o_x, o_y), (h2_x, h2_y)
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1] + 1), (state_new[1][0], state_new[1][1]), (state_new[2][0], state_new[2][1])
            successors['DesnoH1'] = state_new 


        
        ### move O atom ###
        # O gore 
        possible_state_new = (h1_x, h1_y), (o_x - 1, o_y), (h2_x, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1]), (state_new[1][0] + 1, state_new[1][1]), (state_new[2][0], state_new[2][1])
            successors['GoreO'] = state_new 

        # O dolu
        possible_state_new = (h1_x, h1_y), (o_x + 1, o_y), (h2_x, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1]), (state_new[1][0] - 1, state_new[1][1]), (state_new[2][0], state_new[2][1])
            successors['DoluO'] = state_new 

        # O levo
        possible_state_new = (h1_x, h1_y), (o_x, o_y - 1), (h2_x, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1]), (state_new[1][0], state_new[1][1] - 1), (state_new[2][0], state_new[2][1])
            successors['LevoO'] = state_new 
     
        # O desno
        possible_state_new = (h1_x, h1_y), (o_x, o_y + 1), (h2_x, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1]), (state_new[1][0], state_new[1][1] + 1), (state_new[2][0], state_new[2][1])
            successors['DesnoO'] = state_new 


        
        ### move H2 atom ###
        # H2 gore 
        possible_state_new = (h1_x, h1_y), (o_x, o_y), (h2_x - 1, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1]), (state_new[1][0], state_new[1][1]), (state_new[2][0] + 1, state_new[2][1])
            successors['GoreH2'] = state_new 

        # H2 dolu
        possible_state_new = (h1_x, h1_y), (o_x, o_y), (h2_x + 1, h2_y)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1]), (state_new[1][0], state_new[1][1]), (state_new[2][0] - 1, state_new[2][1])
            successors['DoluH2'] = state_new 

        # H2 levo
        possible_state_new = (h1_x, h1_y), (o_x, o_y), (h2_x, h2_y - 1)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1]), (state_new[1][0], state_new[1][1]), (state_new[2][0], state_new[2][1] - 1)
            successors['LevoH2'] = state_new 

        # H2 desno
        possible_state_new = (h1_x, h1_y), (o_x, o_y), (h2_x, h2_y + 1)
        if isValid(*possible_state_new):
            while isValid(*possible_state_new):
                state_new = possible_state_new
                possible_state_new = (state_new[0][0], state_new[0][1]), (state_new[1][0], state_new[1][1]), (state_new[2][0], state_new[2][1] + 1)
            successors['DesnoH2'] = state_new 


        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        h1_x = state[0][0]
        h1_y = state[0][1]
        o_x = state[1][0]
        o_y = state[1][1]
        h2_x = state[2][0]
        h2_y = state[2][1]

        return h1_x == o_x and o_x == h2_x and h1_y == o_y - 1 and o_y == h2_y - 1


    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]



h1_atom_row = 5#int(input())
h1_atom_column = 2#int(input())
o_atom_row = 4#int(input())
o_atom_column = 7#int(input())
h2_atom_row = 0#int(input())
h2_atom_column = 2#int(input())

 

###################################################################################################
initial = (h1_atom_row, h1_atom_column), (o_atom_row, o_atom_column), (h2_atom_row, h2_atom_column)
###################################################################################################

instanca = Molekula(initial)

answer = breadth_first_graph_search(instanca)

print(answer.solution())