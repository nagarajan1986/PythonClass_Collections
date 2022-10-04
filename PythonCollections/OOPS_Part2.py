#INHERITANCE:

#Single Inheritance:

class A:
    def m1(self):
        print("this is a method from class A in single inheritance")

class B(A):     #================================> extends parent class like this in parenthesis   childclassname(parent classname)
    def m2(self):
        print("this is a method from class B in single inheritance")

mc=B()
mc.m1()
mc.m2()


#multilevel inheritance : one parent is going to support child chain like structure formation lik in java as well
class A:
    def m1(self):
        print("this is a method from class A in multilevel inheritance")

class B(A):     #================================> extends parent class like this in parenthesis   childclassname(parent classname)
    def m2(self):
        print("this is a method from class B in multilevel inheritance")

class C(B):         #================================> extends parent class like this in parenthesis   childclassname(parent classname)
    def m3(self):
        print("this is a method from class C in multilevel inheritance")

mc=C()
mc.m1()
mc.m2()
mc.m3()

#Hierachy inheritance: one parent is going to support more than one child separtely

class A:
    def m1(self):
        print("this is a method from class A in Hierachy inheritance")

class B(A):     #================================> extends parent class like this in parenthesis   childclassname(parent classname)
    def m2(self):
        print("this is a method from class B in Hierachy inheritance")

class C(A):         #================================> extends parent class like this in parenthesis   childclassname(parent classname)
    def m3(self):
        print("this is a method from class C in Hierachy inheritance")

mc=B()
mc.m1()
mc.m2()

mc=C()
mc.m1()
mc.m3()

#Multiple inheritance: two parent is going to support one child

class A:
    def m1(self):
        print("this is a method from class A in Multiple inheritance")

class B:     #================================> extends parent class like this in parenthesis   childclassname(parent classname)
    def m2(self):
        print("this is a method from class B in Multiple inheritance")

class C(A,B):         #================================> extends parent class like this in parenthesis   childclassname(parent classname)
    def m3(self):
        print("this is a method from class C in Multiple inheritance")

mc=C()
mc.m1()
mc.m2()
mc.m3()

#super() keyword usage: SYNTAX: super().methodname in child class

class A:
    def m1(self):
        print("this is a method from class A")

class B(A):     #================================> extends parent class like this in parenthesis   childclassname(parent classname)
    def m1(self):
        print("this is a method from class B")
        super().m1()            #==========> super().methodname keyword is used to invoke parent class methods when same method name occurs.

mc=B()
mc.m1()

#Polymorphism:
#Overriding variables:
class parent:
    name="scott"

class child(parent):
    name="john"

mc=child()
print(mc.name)

#Overriding methods:
class bank:
    def rateOfInterest(self):
        return 0

class Xbank(bank):
    def rateOfInterest(self):  #================>overriding methods by using same methods from parent class and change some value as our wish
        return 10

class Ybank(bank):
    def rateOfInterest(self):  #================>overriding methods by using same methods from parent class and change some value as our wish
        return 12

b=Xbank()
print(b.rateOfInterest())

c=Ybank()
print(c.rateOfInterest())


#Overloading methods:
class Human:
    def sayhello(self,name=None):   #===============>This is Overloading concept in python not lik tat in java
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello")

mc=Human()
mc.sayhello("Nagarajan")
mc.sayhello()

print("=========================================================================================")

class Calculation:
    def add(self,a=0,b=0,c=0):      #===============>This is Overloading concept in python not lik tat in java
        print(a+b+c)

mc=Calculation()
mc.add()
mc.add(100,200)
mc.add(1000,2000,5000)







