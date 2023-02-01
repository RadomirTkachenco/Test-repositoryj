#class Student:
    #amout_of_student = 0;
    #group = "S 2929"
    #def__init__(self, height = 160)
        #self.height = height
    #Student.amout_of_student += 1


#st1 = Student()
#st2 = Student()
#st3 = Student()
#print(st1.height)
#print(st2.height)
#print(st3.height)
#print(Student.amout_of_student)

#st1.group = "V2925"

#class Student:
    #height = 150

    #def__init__(self):
        #print(self.height)
        #self.height += 20


    #def printer(self);
        #print(self.height)

#st1 = Student()
#st2 = printer

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 10
        self.gladness = 50
        self.progress = 0
        self.alive = True


    def to_study(self):
        print('Time to study')
        self.progress += 1.5
        self.gladness -= 0.3

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 0.3

    def to_relaxe(self):
        print('Time to study')
        self.progress -= 0.2
        self.gladness += 0.5
        self.money -= 5


    def is_VUZ(self):
        if self.progress < -0.5
            print('!You are cant study!')
            self.progress -= 5


    def work(self):
        print('You must work')
        self.money += 10
        self.gladness -= 0.3
        self.progress += 0.01


    def is_alive(self):
        if self.gladness < -5
            print('Game over')
            self.alive = False
            self.progress -= 778675657678
            