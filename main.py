from random import *

grille = [' ' for i in range(10)]

#Pour afficher la grille

def affGrille():
    print('\033[2J\033[1;1H')
    print(f"""  |   | 
 {grille[1]}| {grille[2]} |{grille[3]}
---------
 {grille[4]}| {grille[5]} |{grille[6]}
---------
 {grille[7]}| {grille[8]} |{grille[9]}
  |   |""")
    
    
#Placer un symbole sur la grille et return false si la case est non vide 

def placeGrille(t, p):
    if grille[p]== ' ':
        grille[p]=t
        return True
    return False

#Fonction qui vérifie que la grille actuelle a une victoire et retourne le symbole gagnant

def win():
    if grille[1]==grille[2] and grille[2]==grille[3] and grille[1] != " ":
        return grille[1]
    if grille[4]== grille[5] and grille[4]==grille[6] and grille[4]!=" ":
        return grille[4]
    if grille[7]== grille[8] and grille[7]==grille[9] and grille[7]!=" ":
        return grille[7]
    if grille[1]== grille[4] and grille[1]==grille[7] and grille[1]!=" ":
        return grille[1]
    if grille[2]== grille[5] and grille[2]==grille[8] and grille[2]!=" ":
        return grille[2]
    if grille[3]== grille[6] and grille[3]==grille[9] and grille[3]!=" ":
        return grille[3]  
    if grille[1]== grille[5] and grille[1]==grille[9] and grille[1]!=" ":
        return grille[1]
    if grille[3]== grille[5] and grille[3]==grille[7] and grille[3]!=" ":
        return grille[3]
    if grille.count(' ')==1:
        return ' '
    return False

#Renvoi les cases vide

def legit():
    res=[]
    for i in range(1, 10):
        if grille[i]==' ':
            res.append(i)
        return res

#l'ordinateur joue au hasard

def cpuJoue(symb): #L'ordinateur joue au hasard.
    possibles=legit()
    i = randint(0,len(possibles)-1)
    placeGrille(symb,possibles[i])
    
#Jeu du joueur

def joueurJoue(symb):
    ligne = None
    while True:
        p = input("Ou ?")
        possible =  legit()
        try:
            p=int(p)
            if p<1 or p>9:
                print("Entre 1 et 9")
            else:
                if not placeGrille(symb,p):
                    print("Emplacement déjà occupé.")
                else:
                    print("ok")
                return
        except:
            print("Un entier entre 1 et 9.")

winner = False
current = randint(0, 1)

while not winner:
    affGrille()
    if current == 1:
        cpuJoue('X')
    else:
        joueurJoue('O')
        
    current = 1-current
    
    winner = win()
    
    affGrille()
    if winner not in ['X', 'O']:
        print('Egalité')
    else:
        print(winner+' gagne')