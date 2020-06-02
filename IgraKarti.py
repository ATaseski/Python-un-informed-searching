from python_neinformirano_prebaruvanje import *


class IgraProba(Problem):
    #def __init__(self, initial, strelki, karti):
    def __init__(self, initial):
        self.initial = initial
        #self.strelki = strelki
        #self.karti = karti

    def successor(self, state):
        successors = dict()
        
        covece = state[0]
        covece_x = state[0][0]
        covece_y = state[0][1]
 
        vrednosti = state[1]
        vrednosti = [list(vrednosti[m]) for m in range(len(vrednosti))]
         
        # strelki i karti se globalno definirani

        nemaStrelka = True
        nemaKarta = True

         
        #############################
        # Gore ######################
        #############################
        if covece_x > 0:
            # priverka dali momentalno se naogat na strelka 
            for strelka in strelki: 
                if (strelka[0], strelka[1]) == (covece_x, covece_y):
                    nemaStrelka = False
                    if strelka[2] == 'Gore':
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                     
                        vrednosti_new = tuple(tuple(element) for element in vrednosti)
                        covece_new = (covece_x - 1, covece_y) 
                        state_new = covece_new, vrednosti_new#, strelki, karti
                        successors['Gore'] = state_new
            
            # ako ne e strelka togas si na obicna vrednost
            if nemaStrelka:
                # ako gore od coveceto imat karta 
                for karta in karti:
                    if (covece_x - 1, covece_y) == (karta[0], karta[1]):
                        nemaKarta = False
                        # prvo namalija vrednosta na momentalnata lokacija 
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                     
                        vrednosti_new = tuple(tuple(element) for element in vrednosti)
                        # pomesti go coveceto na drugata karta 
                        for drugaKarta in karti:
                            if (drugaKarta[2] == karta[2]) and ((drugaKarta[0], drugaKarta[1]) != (covece_x, covece_y)):
                                covece_new = drugaKarta[0], drugaKarta[1]
                                state_new = covece_new, vrednosti_new#, strelki, karti
                                successors['Gore'] = state_new
                
                # ako gore od coveceto imat obicna vrednost
                if nemaKarta:
                    if covece_x - 1 >= 0:
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                    
                            vrednosti_new = tuple(tuple(element) for element in vrednosti)
                            covece_new = (covece_x - 1, covece_y)
                            state_new = covece_new, vrednosti_new#, karti, strelki
                            successors['Gore'] = state_new
 


        #############################
        # Dolu ######################
        #############################
        if covece_x < 4:
            # priverka dali momentalno se naogat na strelka 
            for strelka in strelki: 
                if (strelka[0], strelka[1]) == (covece_x, covece_y):
                    nemaStrelka = False
                    if strelka[2] == 'Dolu':
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                    
                        vrednosti_new = tuple(tuple(element) for element in vrednosti)
                        covece_new = (covece_x + 1, covece_y) 
                        state_new = covece_new, vrednosti_new#, strelki, karti
                        successors['Dolu'] = state_new
            
            # ako ne e strelka togas si na obicna vrednost
            if nemaStrelka:
                # ako dolu od coveceto imat karta 
                for karta in karti:
                    if (covece_x + 1, covece_y) == (karta[0], karta[1]):
                        nemaKarta = False
                        # prvo namalija vrednosta na momentalnata lokacija 
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                    
                        vrednosti_new = tuple(tuple(element) for element in vrednosti)
                        # pomesti go coveceto na drugata karta 
                        for drugaKarta in karti:
                            if (drugaKarta[2] == karta[2]) and ((drugaKarta[0], drugaKarta[1]) != (covece_x, covece_y)):
                                covece_new = drugaKarta[0], drugaKarta[1]
                                state_new = covece_new, vrednosti_new#, strelki, karti
                                successors['Dolu'] = state_new
                
                # ako dolu od coveceto imat obicna vrednost
                if nemaKarta:
                    if covece_x + 1 >= 0:
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                    
                            vrednosti_new = tuple(tuple(element) for element in vrednosti)
                            covece_new = (covece_x + 1, covece_y)
                            state_new = covece_new, vrednosti_new#, karti, strelki
 


        #############################
        # Levo ######################
        #############################
        if covece_y > 0:
            # priverka dali momentalno se naogat na strelka 
            for strelka in strelki: 
                if (strelka[0], strelka[1]) == (covece_x, covece_y):
                    nemaStrelka = False
                    if strelka[2] == 'Levo':
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                    
                        vrednosti_new = tuple(tuple(element) for element in vrednosti)
                        covece_new = (covece_x, covece_y - 1) 
                        state_new = covece_new, vrednosti_new#, strelki, karti
                        successors['Levo'] = state_new
            
            # ako ne e strelka togas si na obicna vrednost
            if nemaStrelka:
                # ako levo od coveceto imat karta 
                for karta in karti:
                    if (covece_x, covece_y - 1) == (karta[0], karta[1]):
                        nemaKarta = False
                        # prvo namalija vrednosta na momentalnata lokacija 
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                    
                        vrednosti_new = tuple(tuple(element) for element in vrednosti)
                        # pomesti go coveceto na drugata karta 
                        for drugaKarta in karti:
                            if (drugaKarta[2] == karta[2]) and ((drugaKarta[0], drugaKarta[1]) != (covece_x, covece_y)):
                                covece_new = drugaKarta[0], drugaKarta[1]
                                state_new = covece_new, vrednosti_new#, strelki, karti
                                successors['Levo'] = state_new
                
                # ako levo od coveceto imat obicna vrednost
                if nemaKarta:
                    if covece_y - 1 >= 0:
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                    
                            vrednosti_new = tuple(tuple(element) for element in vrednosti)
                            covece_new = (covece_x, covece_y - 1)
                            state_new = covece_new, vrednosti_new#, karti, strelki
                            successors['Levo'] = state_new
        



        #############################
        # Desno #####################
        #############################
        if covece_y < 4:
            # priverka dali momentalno se naogat na strelka 
            for strelka in strelki: 
                if (strelka[0], strelka[1]) == (covece_x, covece_y):
                    nemaStrelka = False
                    if strelka[2] == 'Desno':
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                   
                        vrednosti_new = tuple(tuple(element) for element in vrednosti)
                        covece_new = (covece_x, covece_y + 1) 
                        state_new = covece_new, vrednosti_new#, strelki, karti
                        successors['Desno'] = state_new
            
            # ako ne e strelka togas si na obicna vrednost
            if nemaStrelka:
                # ako desno od coveceto imat karta 
                for karta in karti:
                    if (covece_x, covece_y + 1) == (karta[0], karta[1]):
                        nemaKarta = False
                        # prvo namalija vrednosta na momentalnata lokacija 
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                   
                        vrednosti_new = tuple(tuple(element) for element in vrednosti)
                        # pomesti go coveceto na drugata karta 
                        for drugaKarta in karti:
                            if (drugaKarta[2] == karta[2]) and ((drugaKarta[0], drugaKarta[1]) != (covece_x, covece_y)):
                                covece_new = drugaKarta[0], drugaKarta[1]
                                state_new = covece_new, vrednosti_new#, strelki, karti
                                successors['Desno'] = state_new
                
                # ako desno od coveceto imat obicna vrednost
                if nemaKarta:
                    if covece_y + 1 >= 0:
                        for i in range(0, len(vrednosti)):
                            if (vrednosti[i][0], vrednosti[i][1]) == (covece_x, covece_y):
                                if vrednosti[i][2] > 0:
                                    vrednosti[i][2] -= 1
                                
                            vrednosti_new = tuple(tuple(element) for element in vrednosti)
                            covece_new = (covece_x, covece_y + 1)
                            state_new = covece_new, vrednosti_new#, karti, strelki
                            successors['Desno'] = state_new
 


        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        vrednosti = state[1]
        for vrednost in vrednosti:
            if vrednost[2] != 0:
                return False
        return True 

    def result(self, state, action):
        possible = self.successor(state)
        return possible[action]


 
#################################################################################################3

igracRedica = 4 # = input()
igracKolona = 0 # = input()
covece = (igracRedica, igracKolona)


vrednosti = "0,0,1,2,0,0,1,0,1,1,0,0,1,1" # = input()
vrednosti = [int(x) for x in vrednosti.split(',')]
vrednosti = tuple(vrednosti)

vrednostiKoordinati = ((0, 1), (0, 2), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2))

vrednostiFinal = []

for i in range(0, len(vrednostiKoordinati)):
    vrednostiFinal.append((vrednostiKoordinati[i][0], vrednostiKoordinati[i][1], vrednosti[i]))
vrednostiFinal = tuple(vrednostiFinal)

# vrednostiFinal = ((0,1,4), (0,2,1), (0,3,5),...)

karti = ((0, 0, 'Tref'), (1, 0, 'Karo'), (1, 1, 'List'), (1, 4, 'Srce'), (2, 3, 'List'),(3, 4, 'Tref'), (4, 3, 'Karo'), (4, 4, 'Srce'))


strelka1Redica = 2#input()
strelka1Kolona = 0#input()
strelka1Nasoka = "Desno"#input()
strelka2Redica = 3#input()
strelka2Kolona = 1#input()
strelka2Nasoka = "Dolu"#input()
strelki = ((strelka1Redica, strelka1Kolona, strelka1Nasoka), (strelka2Redica, strelka2Kolona, strelka2Nasoka))

################################## 
initial = (covece, vrednostiFinal)
##################################

instanca = IgraProba(initial)

answer = breadth_first_graph_search(instanca)

print(answer.solution())

