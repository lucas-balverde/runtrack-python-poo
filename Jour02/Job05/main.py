class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = km
        self.en_marche = False
        self.reservoir = 50

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.en_marche = True
            print("La voiture démarre")
        else:
            print("Le réservoir est vide")

    def arreter(self):
        self.en_marche = False

    def __verifier_plein(self):
        return self.reservoir
    
voiture1 = Voiture("BMW", "e36", 1996, 148000)                                                                                                                                                 # en temps normal meme avec un reservoir plein une e36 ne démare pas, il y a forcément au moins un voyant moteur qui s'allume
voiture1.demarrer()