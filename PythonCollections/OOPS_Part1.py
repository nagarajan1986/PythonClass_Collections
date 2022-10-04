
#creating a class, methods and objects

# 2 types methods we can define within the class
#1. instance method ( we can call through using object only )
#2. static method ( we can call using class itself )


#1. instance method ( we can call through using object only )
class Myclass:                   #==============>class
    def myfunc(self):          #==============>Method
        print("Hello")
    def display(self, name):
        print(name)

mc1=Myclass()          #==============>Object and saved in one variable

mc1.myfunc()          #==============>Call a Object
mc1.display("John")

#2. static method ( we can call using class itself )
class Myclass1:
    def employee(self):
        print("Employee 1")
    @staticmethod                     #==============>Static method annotation
    def employee1(self, num):
        print(num)

mc=Myclass1()
mc.employee()
mc.employee1(100, 30)

Myclass1.employee1(100,30)      #classname.methodname()

print("=========================================================================================")
class Myclass3:
    a,b=10,20           # class variables
    def add(self):
        print(self.a+self.b)     #'self' keyword is referring to class name
    def multi(self):
        print(self.a*self.b)

mc=Myclass3()
mc.add()
mc.multi()
print("=========================================================================================")

i,j=10,20                           #==============>here i and j are global variables
class Myclass4:
    a,b=100,200           #==============>here a and b are class variables.......class variables can access only by using 'classname.variable name'. here classname is 'self'
    def add(self,x,y):
        print(x+y)                      #==============>here x and y are local variables
        print(self.a+self.b)
        print(i+j)

mc=Myclass4()
mc.add(1000,2000)

print("=======================================================================")
k,m=10,20
class Myclass5:
    def add(self,k=100,m=900):
        print(k+m)
        print(globals()["k"]*globals()["m"])    #NOTE: we can use  globals()[" "]  keyword for same variable names used as local,class and global

mc=Myclass5()
mc.add()


print("=============================================================================================")
#Constructor - OOPs concept:
class const:
    a,b=10,20
    def __init__(self,x,y):                 #==============>creating Constructor by using __init__(self):
        print(self.a*self.b)            #==============>here a and b are class variables. by using self keyword we can access those (example: self.variableName like that)
        print(x+y)                      #============>here it is local variable we can access directly without self keyword, whereas global variable also call anywhere else

mc=const(1000,3000)              #==============>here object creation is enough to call constructor like java. no need to access with object.

class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
        print(eid,ename,sal)

    def __str__(self):    #================> this is string constructor. it can only capable of return string values only
        return(self.ename)

e1=Emp(1851,"Nagarajan",80000)
print(e1)










