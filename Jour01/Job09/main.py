class Produit:
    def __init__(self, nom , prixHT , TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA 

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)
    
    def modifierPrix(self, nouveauPrix):
        self.prixHT = nouveauPrix
        return self.prixHT

    def modifierNom(self, nouveauNom):
        self.nom = nouveauNom
        return self.nom
    
    def afficherInfos(self):
        return f"Produit : {self.nom} \nPrix : {self.prixHT} \nTVA : {self.TVA} \nPrix TTC : {self.CalculerPrixTTC()}"


produit1 = Produit("Banane", 2 , 20)
produit1.modifierNom("Pomme")
produit1.modifierPrix(3)
print(produit1.afficherInfos())