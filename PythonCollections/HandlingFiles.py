

#Handling files in python to write, read, append

#Writing a data in file:
file=open("D:/Demofiles/pythonDemo.txt", 'w')   #====================> path need & w means write mode
file.write("This is the first statement \n")    #====================> write means write something in text file
file.write("This is the second statement \n")
file.write("This is the third statement \n")
file.write("This is the fourth statement \n")
file.close()

#Read a data in file:
file=open("D:/Demofiles/pythonDemo.txt", 'r')   #====================> path need & r means read mode
print(file.read())
#print(file.readline())
file.close()

#Append a data in file:
file=open("D:/Demofiles/pythonDemo.txt", 'a')   #====================> path need & a means append mode
file.write("This is my new line using append function \n")
file.close()
print("program completed")


