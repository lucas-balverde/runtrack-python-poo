class Animal:
    def __init__(self ,prenom):
        self.prenom = prenom
        self.age = int(input("age = "))

    def nommer (self):
        print(f"l'animal se nomme {self.prenom}")

    def vieillir(self):
        print(f"l'age de {self.prenom} est de {self.age} ans")
        print(f"L'age de {self.prenom} apres avoir été vieillit est de {self.age + 1} ans")

animal1 = Animal("rex")
animal1.nommer()
animal1.vieillir()