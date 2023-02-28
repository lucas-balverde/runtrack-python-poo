class Personnage:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def haut(self):
        self.y += 1

    def bas(self):
        self.y -= 1

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def position(self):
        print(f'{self.x} , {self.y}')

personne1 = Personnage(0 , 0)
personne1.haut()
personne1.droite()
personne1.position()