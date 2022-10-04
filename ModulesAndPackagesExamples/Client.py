#Packages: Package is collections of modules, classes, methods.


# import other modules by using import sys & sys.path.append("our package path") syntax

#Approach1:
import sys
sys.path.append("C:/Users/Admin/Desktop/new_python_project/ModulesAndPackagesExamples/Pack1")

import Module1
import Module2

Module1.display()
Module2.show()

#Approach2:
from Module1 import *
from Module2 import *

display()
show()