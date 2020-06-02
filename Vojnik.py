from python_neinformirano_prebaruvanje import *


class Vojnik(Problem):
    def __init__(self, initial):
        self.initial = initial

    def successor(self, state):
        successors = dict()
        vojnik_x = state[0][0]
        vojnik_y = state[0][1]
        stars = state[1]

        ## move12oclock
        if ((vojnik_x - 1, vojnik_y) in polinja) and ((vojnik_x - 1, vojnik_y) not in prepreki):
            vojnik_new = vojnik_x - 1, vojnik_y
            stars_new = tuple(s for s in stars if s != vojnik_new)
            successors['move12oclock'] = vojnik_new, stars_new

        ## move2oclock
        if ((vojnik_x - 1, vojnik_y + 1) in polinja) and ((vojnik_x - 1, vojnik_y + 1) not in prepreki):
            successors['move2oclock'] = (vojnik_x - 1, vojnik_y + 1), tuple(s for s in stars if s != (vojnik_x - 1, vojnik_y + 1))

        ## move4oclock
        if ((vojnik_x + 1, vojnik_y + 1) in polinja) and ((vojnik_x + 1, vojnik_y + 1) not in prepreki):
            successors['move4oclock'] = (vojnik_x + 1, vojnik_y + 1), tuple(s for s in stars if s != (vojnik_x + 1, vojnik_y + 1))

        ## move6oclock
        if ((vojnik_x + 1, vojnik_y) in polinja) and ((vojnik_x + 1, vojnik_y) not in prepreki):
            successors['move6oclock'] = (vojnik_x + 1, vojnik_y), tuple(s for s in stars if s != (vojnik_x + 1, vojnik_y))

        ## move8oclock
        if ((vojnik_x + 1, vojnik_y - 1) in polinja) and ((vojnik_x + 1, vojnik_y - 1) not in prepreki):
            successors['move8oclock'] = (vojnik_x + 1, vojnik_y - 1), tuple(s for s in stars if s != (vojnik_x + 1, vojnik_y - 1))

        ## move10oclock
        if ((vojnik_x - 1, vojnik_y - 1) in polinja) and ((vojnik_x - 1, vojnik_y - 1) not in prepreki):
            successors['move10oclock'] = (vojnik_x - 1, vojnik_y - 1), tuple(s for s in stars if s != (vojnik_x - 1, vojnik_y - 1))



        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        number_of_stars = len(state[-1])
        return number_of_stars == 0

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]



vojnik_redica = int(input())
vojnik_kolona = int(input())

polinja = list(map(int, input()))
prepreki = list(map(int, input()))
stars = list(map(int, input()))


initial = (vojnik_redica, vojnik_kolona), stars

instanca = Vojnik(initial)

answer = breadth_first_graph_search(instanca)

print(answer.solution())
