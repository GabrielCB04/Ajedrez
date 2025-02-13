# Archivo en el que se usan las clases cons sus respectivas funcionas para simular una partida (no interaztivo de momento)
from piezas import *
torreb1 = Torre([0,0], "T")
torreb2 = Torre([0,7], "T")
torreb1.añadir_pieza()
torreb2.añadir_pieza()
torren1 = Torre([7,0], "t")
torren2 = Torre([7,7], "t")
torren1.añadir_pieza()
torren2.añadir_pieza()
reinab = Reina([0,3], "Q")
reinan = Reina([7,3], "q")
reinab.añadir_pieza()
reinan.añadir_pieza()
reyb = Rey([0,4], "K")
reyn = Rey([7,4], "k")
reyb.añadir_pieza()
reyn.añadir_pieza()
alfilb1 = Alfil([0,2], "A")
alfilb2 = Alfil([0,5], "A")
alfilb1.añadir_pieza()
alfilb2.añadir_pieza()
alfiln1 = Alfil([7,2], "a")
alfiln2 = Alfil([7,5], "a")
alfiln1.añadir_pieza()
alfiln2.añadir_pieza()
caballob1 = Caballo([0,1], "C")
caballob2 = Caballo([0,6], "C")
caballob1.añadir_pieza()
caballob2.añadir_pieza()
caballon1 = Caballo([7,1], "c")
caballon2 = Caballo([7,6], "c")
caballon1.añadir_pieza()
caballon2.añadir_pieza()
peonb1 = Peon([1,0], "P")
peonb2 = Peon([1,1], "P")
peonb3 = Peon([1,2], "P")
peonb4 = Peon([1,3], "P")
peonb5 = Peon([1,4], "P")
peonb6 = Peon([1,5], "P")
peonb7 = Peon([1,6], "P")
peonb8 = Peon([1,7], "P")
peonb1.añadir_pieza()
peonb2.añadir_pieza()
peonb3.añadir_pieza()
peonb4.añadir_pieza()
peonb5.añadir_pieza()
peonb6.añadir_pieza()
peonb7.añadir_pieza()
peonb8.añadir_pieza()
peonn1 = Peon([6,0], "p")
peonn2 = Peon([6,1], "p")
peonn3 = Peon([6,2], "p")
peonn4 = Peon([6,3], "p")
peonn5 = Peon([6,4], "p")
peonn6 = Peon([6,5], "p")
peonn7 = Peon([6,6], "p")
peonn8 = Peon([6,7], "p")
peonn1.añadir_pieza()
peonn2.añadir_pieza()
peonn3.añadir_pieza()
peonn4.añadir_pieza()
peonn5.añadir_pieza()
peonn6.añadir_pieza()
peonn7.añadir_pieza()
peonn8.añadir_pieza()

peonb1.mover_pieza([2,0])
peonb1.mover_pieza([3,0])
torreb1.mover_pieza([2,0])
torreb1.mover_pieza([2,5])
torreb1.comer_pieza([6,5])
torreb1.mover_pieza([2,5])
torreb1.comer_pieza([7,5])
imprimir_tablero()
