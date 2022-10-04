

#Functions : user defined functions:

#create a user defined function:
def myfun():
    print("Hello world")

myfun()    # it will call the function already declared or creating above

def myfun(name):
    print("Hello", name)

myfun("Nagarajan")


def cal(a,b):
    return (a+b)

print(cal(100,200))


def func():
    return

print(func())

def func(a,b,c):
    print(a,b,c)

func(10,20,300)    #positional arguments
func(10,20,c=300)    #keyword arguments

#NOTE: positional argument should appear before the keyword argument. it is a thumb rule.

#Global variable and local variable:
x=100 #=============>This is global variable. Global variable is for access anywhere. Global variable can be declared within fucntion or beyond function

def cool():
    x=900       #============>This is local variable, since it is only applicable for the particular function only. Not able to declare outside of fucntion.
    print(x)

def cool():
    global x       #============>This is global variable with  'global' keyword is must.
    x=900
    print(x)
