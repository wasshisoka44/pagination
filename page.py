class Page_virtuelle:
    def __init__(self, numero):
        self.numero=numero
        self.numeroPhysique=-1 #Par défaut
        self.lecture="NON-LUE"
        self.ecriture="NON-MODIFIER"

class Page_physique:
    def __init__(self, numero):
        self.numero=numero
        self.usage="FREE"