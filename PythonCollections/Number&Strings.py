
#Number demo

num1=100
num2=10.5

print(type(num1))
print(type(num2))

print(max(10,20,30,100000)) #max() return max value
print(min(10,20,30,2)) #min() return max value
print("=======================================================")

#Strings demo
s="welcome to python"      # creating string variable
s=str("welcome to python")  # creating string variable
print(s)

s=""

#Mutable and immutable strings

#Immutable string
s="naga"
print(id(s))       #1730310075824

s=s+"rajan"
print(id(s))      #1730310374128

#concat string
s="naga"
print(s+"rajan")
print((s+"rajan")*2)

#slicing string
s="welcome to python program"
print(len(s))
print(s[:25])
print(s[2:])
print(s[1:-1])  #last one character removed
print(s[1:-2]) #last two character removed


#ASCII ord()   and chr()

print(ord("A"))     #ASCII code of the alphabet
print(chr(66))     #by ASCII code it gives corresponding alphabet
print(chr(57))

print(max("abc"))
print(min("abc"))
print(len("welcome"))

#in and not in operators in string usage
s="welcome"
print("to" in s)   # it gives true or false boolean value
print("to" not in s)

#convert strings

s="nagarajan is a programmer GHJJ"
print(s.startswith("n"))
print(s.isalpha())
print(s.capitalize())
print(s.title())
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.replace("GHJJ", ""))

#reverse a string

#Method1:
s="nagarajan is a programmer"
rev=""

for i in s:
    rev=i+rev
print("reverse string is : ", rev)

#Method2:
s="nagarajan is a programmer"
print(s[::-1])    #s[starting point:end point:decrement or reverse those character]






