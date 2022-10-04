
#Exception handlings are try,except,else and finally. try and except is must to handle exception, whereas else and finally optionbale

#Example 1:
# print("The program started")
# print("The program in progress")
# try:
#     print(x)
# except:
#     print("Exception occured & handled")
# print("Program completed")

#Example 2:

def enterage(num):
    if num<0:
        print("Value error occured")
    if num%2==0:
        print("even")
    else:
        print("odd")

num=-1
try:
    enterage(num)
except:
    print("value error exception occured and handled")

print("program completed")
