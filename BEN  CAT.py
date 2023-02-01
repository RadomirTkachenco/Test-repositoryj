class Student:
    def __init__(self, name):
        self.name = name
        self.hungry = 5
        self.gladness = 5
        self.freindship = 0


    def hungry(self):
        print('Hungry')
        self.hungry -= 0.1
        self.gladness -=0.4


    def park(self):
        self.hungry += 0.01
        self.gladness += 0.4
        self.freindship -= 0.3


    def freindship_with_cat(self):
        self.freindship += 0.4
        self.gladness += 0.01
        self.hungry -= 4


    def over(self):
        if self.freindship < -5
            print('over')

