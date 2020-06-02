from python_neinformirano_prebaruvanje import *


class IstrazuvacVoGraf(Problem):
    def __init__(self, initial):
        self.initial = initial

    def successors(self, state):
        successors = dict()
        covece = state[0]  
        stars = state[1]  
        links = state[2]   


        # Desno 
        if covece % 4 != 0 and ((covece, covece + 1) in links or (covece + 1, covece) in links):
            covece_new = covece + 1
            stars_new = tuple(s for s in stars if s != covece_new)
            links_new = tuple(l for l in links if l != (covece, covece + 1) if l != (covece + 1, covece))
            successors['Desno'] = covece_new, stars_new, links_new

        # Levo
        if covece % 4 != 1 and ((covece, covece - 1) in links or (covece + 1, covece) in links):
            covece_new = covece - 1
            stars_new = tuple(s for s in stars if s != covece_new)
            links_new = tuple(l for l in links if l != (covece, covece - 1) if l != (covece - 1, covece))
            successors['Levo'] = covece_new, stars_new, links_new

        # Gore 
        if covece > 4 and ((covece, covece - 4) in links or (covece - 4, covece) in links):
            covece_new = covece - 4
            stars_new = tuple(s for s in stars if s != covece_new)
            links_new = tuple(l for l in links if l != (covece, covece - 4) if l != (covece - 4, covece))
            successors['Gore'] = covece_new, stars_new, links_new


        # Dolu 
        if covece < 13 and ((covece, covece + 4) in links or (covece + 4, covece) in links):
            covece_new = covece + 4
            stars_new = tuple(s for s in stars if s != covece_new)
            links_new = tuple(l for l in links if l != (covece, covece + 4) if l != (covece + 4, covece))
            successors['Dolu'] = covece_new, stars_new, links_new


        # DoluDesno
        if covece == 6 and ((covece, covece + 5) in links or (covece + 5, covece) in links):
            covece_new = covece + 5 
            stars_new = tuple(s for s in stars if s != covece_new)
            links_new = tuple(l for l in links if l != (covece, covece + 5) if l != (covece + 5, covece))
            successors['DoluDesno'] = covece_new, stars_new, links_new


        # GoreLevo
        if covece == 11 and ((covece, covece - 5) in links or (covece - 5, covece) in links):
            covece_new = covece - 5 
            stars_new = tuple(s for s in stars if s != covece_new)
            links_new = tuple(l for l in links if l != (covece, covece - 5) if l != (covece - 5, covece))
            successors['GoreLevo'] = covece_new, stars_new, links_new




        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return len(state[1]) == 0

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


IgracPozicija = 6#int(input())
Z1Pozicija = 1#int(input())
Z2Pozicija = 16#int(input())


initial = IgracPozicija, (Z1Pozicija, Z2Pozicija), ((1, 2), (3, 4), (5, 6), (6, 7), (7, 8), (9, 10), (10, 11), (11, 12), (13, 14), (15, 16), (1, 5), (2, 6), (3, 7), (4, 8), (6, 10), (7, 11), (9, 13), (10, 14), (11, 15), (12, 16), (6, 11))
    
instanca = IstrazuvacVoGraf(initial)

answer = breadth_first_graph_search(instanca)
 
print(answer.solution())
