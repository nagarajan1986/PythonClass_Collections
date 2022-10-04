
#importing classes and methods from different packages using import sys syntax:

#NOTE: sys syntax: sys.path.append("our desired package path")


import sys                      #===========>import sys module (NOTE: sys is one of predefined module by python inbuilt)
sys.path.append("C:/Users/Admin/Desktop/new_python_project/ModulesAndPackagesExamples/Package1")    #===========>Need To mention package1 path
sys.path.append("C:/Users/Admin/Desktop/new_python_project/ModulesAndPackagesExamples/Package2")    #===========>Need To mention package2 path

#Approach 1:
import emp                                  #===========>import module name
empobj=emp.Employee(1851,"Nagarajan",80000)  #===========>modulename.classname and stored in a variable (i.e. empobj)
empobj.display()                            #===========>variable.methodname to call

import stu
stuobj=stu.Student(1851,"Nagarajan","A++")
stuobj.show()

#Approach 2:
from emp import *
from stu import *

empobj=emp.Employee(1851,"Nagarajan",90000)  #===========>modulename.classname and stored in a variable (i.e. empobj)
empobj.display()                            #===========>variable.methodname to call

stuobj=stu.Student(1851,"Nagarajan","A+++")
stuobj.show()