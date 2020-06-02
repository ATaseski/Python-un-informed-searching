from python_neinformirano_prebaruvanje import *


def getDirection(current, new):
    
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
           #dolu  desno  gore   levo
    
    if new == "SvrtiLevo":
        return dirs[(dirs.index(current) + 1) % 4]
    elif new == "SvrtiDesno":
        return dirs[(dirs.index(current) - 1) % 4]
    else:
        return current
  

class InsectMaze(Problem):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        successors = dict()
        insekt_cords = state[0]
        insekt_nasoka = state[1]
        insekt_vozduh = state[2]

       

        dirs = "ProdolzhiPravo SvrtiLevo SvrtiDesno".split()
        for d in dirs:
            direction_new = getDirection(state[1], d)
            insekt_cords_new = state[0][0] + direction_new[0], state[0][1] + direction_new[1]

            if insekt_cords_new in polinja_vozduh:
                successors[d] = insekt_cords_new, direction_new, insekt_vozduh
            
            if insekt_cords_new in polinja_voda:
                insekt_vozduh_new = insekt_vozduh - 1
                flag = False
                
                if insekt_vozduh_new == 1:
                    # ako samo ednas imas stapnato na pole so voda 
                    # succs - samo ako imas pole so vozduh za dva cekori   
                    for dd in dirs:
                        direction_new_2 = getDirection(direction_new, dd)
                        insekt_cords_new_2 = insekt_cords_new[0] + direction_new_2[0], insekt_cords_new[1] + direction_new_2[1]
                        if insekt_cords_new_2 in polinja_vozduh:
                            #flag = True
                            successors[d] = insekt_cords_new, direction_new, insekt_vozduh_new
                        else:
                            # ako ne postojt pole so vozduh za eden cekor
                            # proveri dali mozis da zemis vozduh vo dva cekori 
                            for ddd in dirs:
                                direction_new_3 = getDirection(direction_new_2, ddd)
                                insekt_cords_new_3 = insekt_cords_new_2[0] + direction_new_3[0], insekt_cords_new_2[1] + direction_new_3[1]
                                if insekt_cords_new_3 in polinja_vozduh:
                                    flag = True

                            if flag:
                                # ako imat izlez vo maksimum dva cekori - succs 
                                successors[d] = insekt_cords_new, direction_new, insekt_vozduh_new


                     

                if insekt_vozduh_new == 0:
                    # ako veke dva pati imas stapnato na pole so voda 
                    # succs - samo ako slednoto pole imat vozduh 
                    for dd in dirs:
                        direction_new_2 = getDirection(direction_new, dd)
                        insekt_cords_new_2 = insekt_cords_new[0] + direction_new_2[0], insekt_cords_new[1] + direction_new_2[1]
                        if insekt_cords_new_2 in polinja_vozduh:
                            successors[d] = insekt_cords_new, direction_new, insekt_vozduh_new

                      
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return state[0][0] == self.goal[0] and state[0][1] == self.goal[1]

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


n = 5 
polinja_vozduh = (0,0), (0,1), (0,2), (0,3), (0,4), (2,0), (2,2), (2,3), (2,4), (3,3), (4,0), (4,2), (4,3), (4,4)
polinja_voda = (1,1), (2,1), (3,1), (4,1)
insekt_cords = (4,0) 
insekt_vozduh = 2
insekt_nasoka = (0,1)

initial = insekt_cords, insekt_nasoka, insekt_vozduh
goal = (0,4)

instanca = InsectMaze(initial, goal)
answer = breadth_first_graph_search(instanca)
print(answer.solution())