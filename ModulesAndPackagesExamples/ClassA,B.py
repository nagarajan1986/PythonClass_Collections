#Approach1:
import ClassA  #=======>import module name (i.e filename.py)
import ClassB

mc1=ClassA.Animal()     #=======>import module name.class name to call methods from another class
mc1.display()           #Then objname.method

mc2=ClassB.Bird()     #=======>import module name.class name to call methods from another class from another class
mc2.display()

#Approach2:
from ClassA import *    #===>from keyword modulename import keyword classname or * to import package
from ClassB import *

obj1=Animal()
obj1.display()
obj2=Bird()
obj2.display()

