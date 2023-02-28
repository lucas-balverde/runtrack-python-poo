class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f'{self.x},{self.y}')

    def afficherX(self):
        print(f'{self.x}')

    def afficherY(self):
        print(f'{self.y}')

    def changerX(self, x):
        self.x = x
        print(f'{self.x}')

    def changerY(self, y):
        self.y = y
        print(f'{self.y}')


point1 = Point(12 , 8)
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
point1.changerX(5)
point1.changerY(10)