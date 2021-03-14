from math import ceil
from page import *

class Machine:
    def __init__(self, taille_prog, taille_mem, taille_page):
        self.taille_prog=taille_prog
        self.taille_mem=taille_mem
        self.taille_page=taille_page
        self.tab_physique=[]
        self.tab_virtuelle=[]
        self.file=[]

        for i in range(0, ceil(self.taille_prog/self.taille_page)): #Création des pages virtuelles
            self.tab_virtuelle.append(Page_virtuelle(i))
        
        for i in range(0, ceil(self.taille_mem/self.taille_page)):
            self.tab_physique.append(Page_physique(i))

    def affectation(self,numero):
        for page in self.tab_physique:
            if page.usage=="FREE":
                self.tab_virtuelle[numero].numeroPhysique= page.numero
                page.usage="USED"
                self.file.append(self.tab_virtuelle[numero])
                return 
        self.fifo(numero)

    def fifo(self,numero):
        #On parcours les non lues
        for page in self.file:
            if page.lecture=="NON-LUE":
                self.tab_physique[page.numeroPhysique].usage = "FREE"
                page.numeroPhysique=-1
                self.file.remove(page)
                self.affectation(numero)
        #Puis on parcours les non modifé 
        for page in self.file:
            if page.ecriture == "NON-MODIFIEE":
                self.tab_physique[page.numeroPhysique].usage = "FREE"
                page.numeroPhysique = -1
                self.file.remove(page)
                self.affectation(numero)

    def addrPhysiqueToAddrVirtuelle(self,numero,decalage):
        if self.tab_virtuelle[numero].numeroPhysique==-1:
            self.affectation(numero)
        return (self.tab_virtuelle[numero].numeroPhysique, decalage)

    def executer(self,instruction):
        if instruction[0]=="W":
            self.tab_virtuelle[instruction[1]].ecriture="MODIFIEE"
        if instruction[0]=="R":
            self.tab_virtuelle[instruction[1]].lecture="LUE"
        self.addrPhysiqueToAddrVirtuelle(instruction[1],instruction[2])
        
    def affiche_virtuelle(self):
        print("Page virtuelle : \n")
        for page in self.tab_virtuelle:
            print(f"Numéro de page : {page.numero} | Numéro de page physique : {page.numeroPhysique} | Lecture : {page.lecture} | Ecriture : {page.ecriture}")

    def affiche_physique(self):
        print("PAge physique : \n")
        for page in self.tab_physique:
            print(f"Numéro de page : {page.numero} | Etat : {page.usage}")
    def affiche_tout(self):
        self.affiche_virtuelle()
        self.affiche_physique()
