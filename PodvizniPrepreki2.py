from python_neinformirano_prebaruvanje import *


def isValid(state_new):
    # initial = (choveche_redica, choveche_kolona), p1, p2, p3
    c_x = state_new[0][0]
    c_y = state_new[0][1]
    p1 = state_new[1]
    p2 = state_new[2]
    p3 = state_new[3]

    # dali coveceto e nadvor od tabla 
    if c_x < 0 or c_x > 10 or c_y < 0 or c_y > 10 or (c_x < 5 and c_y > 5):
        return False

    # dali nekoja prepreka e nadvor od tabla 
        # ne e mozno 

    # dali ima dve prepreki na ista pozicija 
        # ne e mozno

    # dali coveceto e na ista pozicija so nekoja prepreka 
    if (c_x, c_y) in p1[0:len(p1)] or (c_x, c_y) in p2[0:len(p2)] or (c_x, c_y) in p3[0:len(p3)]:
        return False

    return True


'''
def update_precka1(precka1):
    nasoka = precka1[-1] 
    if precka1[0][1] == 0 and nasoka == -1:
        nasoka = nasoka * (-1) 
    return (precka1[0][0], precka1[0][1] + nasoka), (precka1[1][0], precka1[1][1] + nasoka), nasoka

def update_precka2(precka2):
    nasoka = precka2[-1]
    if precka2[0][0] == 5 and nasoka == -1:
        nasoka = nasoka * (-1)
    return (precka2[0][0] + nasoka, precka2[0][1] - nasoka), (precka2[1][0] + nasoka, precka2[1][1] - nasoka), (precka2[2][0] + nasoka, precka2[2][1] - nasoka), (precka2[3][0] + nasoka, precka2[3][1] - nasoka), nasoka

def update_precka3(precka3):
    nasoka = precka3[-1]
    if precka3[0][0] == 6 and nasoka == -1:
        nasoka = nasoka * (-1)
    return (precka3[0][0] + nasoka, precka3[0][1]), (precka3[1][0] + nasoka, precka3[1][1]), nasoka
'''

def update_precka1(precka):
    x = precka[0]
    y = precka[1]
    nasoka = precka[2]

    if (y == 0 and nasoka == -1) or (y == 4 and nasoka == 1):
        nasoka = nasoka * (-1)
    x_new = x 
    y_new = y + nasoka
    position_new = x_new, y_new, nasoka
    return position_new

def update_precka2(precka):
    x = precka[0]
    y = precka[1]
    nasoka = precka[2]

    if (x == 5 and nasoka == -1) or (x == 9 and nasoka == 1):
        nasoka = nasoka * (-1)
    x_new = x + nasoka 
    y_new = y - nasoka
    position_new = x_new, y_new, nasoka
    return position_new

def update_precka3(precka):
    x = precka[0]
    y = precka[1]
    nasoka = precka[2]

    if (x == 5 and nasoka == -1) or (x == 9 and nasoka == 1):
        nasoka = nasoka * (-1)
    x_new = x + nasoka
    y_new = y
    position_new = x_new, y_new, nasoka
    return position_new


class probaaa(Problem):
    def __init__(self, initial, goal):
        self.initial = initial
        self. goal = goal

    def successor(self, state):
        successors = dict()

        # initial = (choveche_redica, choveche_kolona), p1, p2, p3
        c_x, c_y = state[0]

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        possible = "Dolu Desno Gore Levo".split()

        p1_new = update_precka1(state[1])
        p2_new = update_precka2(state[2])
        p3_new = update_precka3(state[3])

        for i in range(len(dx)):
            c_x_new = c_x + dx[i]
            c_y_new = c_y + dy[i]
            state_new = (c_x_new, c_y_new), p1_new, p2_new, p3_new
            if isValid(state_new):
                successors[possible[i]] = state_new

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return state[0] == self.goal


    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]

    def h(self, node):
        S = node.state
        g = self.goal
        return mhd(S[0], g)

# mhd (zbiror od dolzinite na kracite) = abs(Xa - Xb) + abs(Ya - Yb)
# ed (dijagonalnata dolzina) = sqrt( (Xa - Xn)**2 + (Xa - Xb)**2 )

def mhd(covece, cel):
    Xa, Ya = covece
    Ya, Yb = cel
    return abs(Xa - Xb) + abs(Ya - Yb)


choveche_redica = 0#int(input())
choveche_kolona = 0#int(input())
kukja_redica = 10#int(input())
kukja_kolona = 10#int(input())

p1 = (2, 2, -1)
p2 = (6, 2, -1)
p3 = (6, 8, 1)

initial = (choveche_redica, choveche_kolona), p1, p2, p3
goal = kukja_redica, kukja_kolona

instanca = probaaa(initial, goal)
answer = breadth_first_graph_search(instanca)
print(answer.solution())