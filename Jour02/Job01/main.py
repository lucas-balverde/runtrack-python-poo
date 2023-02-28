class Rectangle:
    def __init__(self):
        self.longueur = 0
        self.largeur = 0

    def __setmodiflongueur(self):
        longueur = int(input("Entrez la longueur du rectangle : "))
        return longueur

    def __setmodiflargeur(self):
        largeur = int(input("Entrez la largeur du rectangle : "))
        return largeur

    def getmodiflongueur(self):
        self.longueur = self.__setmodiflongueur()
        print(f"La longueur du rectangle est de : {self.longueur} ")

    def getmodiflargeur(self):
        self.largeur = self.__setmodiflargeur()
        print(f"La largeur du rectangle est de : {self.largeur} ")

rectangle1 = Rectangle()
rectangle1.getmodiflongueur()
rectangle1.getmodiflargeur()