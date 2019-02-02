class Student:
    def __init__(self,c):
        self.city=c
    def f(self,n,y):
        self.name=n
        self.year=y
        print (self.name, "is on the", self.year,"-th year")
s=Student("St.Petersburg")
print (s.city)
