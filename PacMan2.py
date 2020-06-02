from python_neinformirano_prebaruvanje import *


def isValid(current):
    # da ne e nadvor od tabla 
    if current[0] < 0 or current[0] > 4 or current[1] < 0 or current[1] > 6:
        return False

    # da ne e na prepreka nekoja
    if current in prepreki:
        return False

    return True 

 

def getDirection(momentalna, posakuvana):   
    # return realnata nova nasoka 

    if posakuvana == "VratiseNazad":
        posakuvana = (1,0)
    if posakuvana == "SvrtiDesno":
        posakuvana = (0,1)
    if posakuvana == "ProdolziPravo":
        posakuvana = (-1,0)
    if posakuvana == "SvrtiLevo":
        posakuvana = (0,-1)

    nasoki = [(1,0),(0,1),(-1,0),(0,-1)]
    # index:   [0]   [1]    [2]    [3] 
    #         dolu  desno   gore   levo
 

    if momentalna == (-1,0): # ako momentalno e svrten nagore (ProdolziPravo)
        return nasoki[nasoki.index(posakuvana)] 


    if momentalna == (0,1):  # ako momentalno e svrten nadesno (SvrtiDesno)
        return nasoki[(nasoki.index(posakuvana) - 1) % 4]


    if momentalna == (0,-1): # ako momentalno e svrten nalevo (SvrtiLevo)
        return nasoki[(nasoki.index(posakuvana) + 1) % 4]


    if momentalna == (1,0):  # ako momentalno e svrten nadolu (VratiseNazad)
        '''
        for nasoka in nasoki:
            if nasoki == posakuvana:
                return nasoki[(nasoki.index(posakuvana) + 2) % 4]
        '''  

        # ako posakuvana e desno
        if posakuvana == (0,1):
            return (0,-1)
            # svrti levo

        # ako posakuvana e levo
        if posakuvana == (0,-1):
            return (0,1)
            # svrti desno
        
        if posakuvana == (1,0):
            return (-1,0)
            # vratise nazad  
        
        if posakuvana == (-1,0):
            return (1,0)
            # prodolzi pravo  

     


class PacMan(Problem):
    def __init__(self, initial, prepreki):
        self.initial = initial
        self.prepreki = prepreki

    def successor(self, state):
        successors = dict()
                           
        # mozni dvizenja: nazad,  desno,   gore,   pravo
        ################  (1,0),  (0,1),  (-1,0), (0,-1)
        
        # state as: pac_man, nasoka, hrana
        ###########   s[0]    s[1]   s[2]

        possible = "ProdolziPravo VratiseNazad SvrtiLevo SvrtiDesno".split()
        for posakuvana in possible:
            #nasoka_new = getDirection(state[1], getPosakuvana(d))
            nasoka_new = getDirection(state[1], posakuvana)
            pac_man_new = state[0][0] + nasoka_new[0], state[0][1] + nasoka_new[1]
            if isValid(pac_man_new):
                hrana_new = tuple(x for x in state[2] if x != pac_man_new)
                successors[posakuvana] = pac_man_new, nasoka_new, hrana_new  

           

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        hrana = state[2]
        return len(hrana) == 0

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


pac_man = (1,3)
nasoka = (-1,0)
prepreki = ((1,0), (1,1), (1,2), (1,4), (1,5), (3,1), (3,2), (3,4), (3,5), (4,1))
hrana = ((0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (1,6), (2,0), (2,1), (2,5), (2,6), (3,6), (4,2), (4,3), (4,4), (4,5), (4,6))

################################ 
initial = pac_man, nasoka, hrana 
######## state[0],  s[1],  s[2]  
# mozit da se pridvizit samo vo praven na momentalnata nasoka 

instanca = PacMan(initial, prepreki)
answer = breadth_first_graph_search(instanca)
print(answer.solution())
