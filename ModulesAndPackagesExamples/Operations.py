
#call module from one module to another module
#Approach 1:
import Calculator

Calculator.add(100,200)
Calculator.multi(400,500)

print("==============================================")

#Approach 2:
from Calculator import add,multi
add(100,200)
multi(300,900)

print("==============================================")

#Approach 3:
from Calculator import *
add(100,200)
multi(300,900)