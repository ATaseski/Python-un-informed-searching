from python_neinformirano_prebaruvanje import *

def is_valid(state):
    misioneri_l, kanibali_l, chamec, misioneri_d, kanibali_d = state
 
 
    #ako ima misioneri na nekoja strana, a brojot na kanibali e pogolem od misioneri -> nevalidno
    if (kanibali_l > misioneri_l and misioneri_l > 0) or (kanibali_d > misioneri_d and misioneri_d > 0):
        return False
 
    return True
 
 
class MisioneriKanibali(Problem):
 
    def __init__(self, sostojba, goal, N, K):
        self.initial = sostojba
        self.goal = goal
        self.N = N
        self.K = K
 
    def goal_test(self, state):
        if state == self.goal:
            return True
        return False
 
    def successor(self, state):
        successors = {}
        misioneri_l, kanibali_l, chamec, misioneri_d, kanibali_d = state
 
        # ako chamecot e na levata strana
        # gi izminuvame site misioneri i kanibali na taa strana
        # sekoja kombinacija kade sto nivniot zbir e > 0 a e <= kapacitet  ja preslikuvame vo nova sostojba
        # i proveruvame dali sostojbata e validna, ako e ja dodavame vo successors
        if chamec == 'L':
            for i in range(misioneri_l + 1):
                for j in range(kanibali_l + 1):
                    if i + j > 0 and i + j <= self.K:
 
                        misioneri_l_new = misioneri_l - i
                        kanibali_l_new = kanibali_l - j
                        misioneri_d_new = misioneri_d + i
                        kanibali_d_new = kanibali_d + j
 
                        state_new = (misioneri_l_new, kanibali_l_new, 'D', misioneri_d_new, kanibali_d_new)
                        if is_valid(state_new):
                            successors[str(i)+'M_'+str(j)+'K'] = state_new
 
        # ako chamecot e na desna strana
        # slicno kako za chamecot koga e na leva strana
        if chamec == 'D':
            for i in range(misioneri_d + 1):
                for j in range(kanibali_d + 1):
                    if i + j > 0 and i + j <= self.K:
 
                        misioneri_d_new = misioneri_d - i
                        kanibali_d_new = kanibali_d - j
                        misioneri_l_new = misioneri_l + i
                        kanibali_l_new = kanibali_l + j
 
                        state_new = (misioneri_l_new, kanibali_l_new, 'L', misioneri_d_new, kanibali_d_new)
                        if is_valid(state_new):
                            successors[str(i)+'M_'+str(j)+'K'] = state_new
        return successors
 
    #hevristika vrakja broj na misioneri i kanibali levo, 0 koga site se desno
    def h(self, node):
        misioneri_l, kanibali_l, chamec, misioneri_d, kanibali_d = node.state
        return misioneri_l + kanibali_l
 
 
    def actions(self, state):
        return self.successor(state).keys()
 
    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]
 
 
 
if __name__ == "__main__":
    N = int(input())
    K = int(input())
 
    Pocetna = (N, N, 'L', 0, 0)
    Cel = (0, 0, 'D', N, N)
 
    problem = MisioneriKanibali(Pocetna, Cel, N, K)
    answer = astar_search(problem)
    print(answer.solve())

