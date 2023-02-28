from math import *

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self):
        nouveaurayon = int(input("rayon = "))
        self.rayon = nouveaurayon
        print(f'{self.rayon}')

    def circonférence(self):
        return self.rayon * pi * 2
        
    def aire(self):
        return pi * (self.rayon **2)
        
    def diametre(self):
        return self.rayon *2 
        
    def afficherInfos(self):
        print(" ")
        print("rayon ", self.rayon)
        print("périmetre ",self.circonférence())
        print("aire " , self.aire())
        print("diametre " , self.diametre())

cercle1 = Cercle(4)
cercle2 = Cercle(7)
cercle1.changerRayon()
cercle2.changerRayon()
cercle1.afficherInfos()
cercle2.afficherInfos()