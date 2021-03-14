from machine import *

taille_programme=16
taille_memoire=8 
taille_page=4

machine = Machine(taille_programme, taille_memoire, taille_page)
machine.affiche_tout()
instructions = [("R", 2, 0), ("W", 2, 2), ("R", 3, 1), ("W", 0, 2), ("R", 1, 0), ("W", 1, 3),
                ("R", 2, 2), ("W", 2, 3), ("R", 3, 1), ("W", 0, 3), ("R", 2, 1), ("W", 0, 0)]

#machine.affectation(2)
#machine.affiche_tout()
#machine.affectation(1)
#machine.affiche_tout()
#machine.affectation(3)
#machine.affiche_tout()

#machine.addrPhysiqueToAddrVirtuelle(2,0)
#machine.affiche_tout()
#machine.addrPhysiqueToAddrVirtuelle(1,1)
#machine.affiche_tout()
#machine.addrPhysiqueToAddrVirtuelle(3,2)
#machine.affiche_tout()

for instruction in instructions:
    machine.executer(instruction)
    machine.affiche_tout()