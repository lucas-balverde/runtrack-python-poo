class Personne:
    def __init__(self, nom , prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f"je suis {self.nom} {self.prenom} ")

personne1=Personne("Balverde" , "Lucas")
personne1.SePresenter()