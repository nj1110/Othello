from board_class import Plateau
from player_class import Joueur,minmax
from copy import deepcopy
plat=Plateau()
j1=Joueur("Humain",1) #initialise deux joueurs humains j1 et j2 respectivement noirs et blancs
j2=Joueur("MinMax",2,3)
liste_coup_j2=plat.liste_coup_valide(j2)
a=minmax(plat,3,j2,j1)
print(a)