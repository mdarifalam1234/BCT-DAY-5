class person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def showName(self):
        print("Name =", self.name)

    def showage(self):
        print("Age =", self.age)

class student(person):
    def __init__(self, n, a, r):
        super().__init__(n, a) 
        self.rollno = r

    def showRollno(self):
        print("Roll number =", self.rollno)

s1 = student("print", 20, 100)
s1.showName()
s1.showage()
s1.showRollno()                           