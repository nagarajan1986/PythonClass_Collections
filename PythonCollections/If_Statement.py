#conditional statements
# if     if..else       elif

#Example 1: Print a person is eligible for vote or not

age=15

if age>=18:
    print("Person is eligible for voting")
else:
    print("Person is NOT eligible for voting")

#Example 2: Boolean vlaue  True=1; False=0;

if True:
    print("True conditions")
else:
    print("false condtions")

if 0:
    print("True conditions")
else:
    print("false condtions")

#Example 3: Find a number even or odd

num=17

if num%2==0:
    print("Given number is EVEN")
else:
    print("Given number is ODD")

#Example 4: Find a number even or odd (ternary operator)
num=10

print("Even number") if num%2==0 else print("Odd number")

#Example 5: if else - multiple statement in single line

a=4

print({"hello", "python"}) if a>=10 else print({"hi", "java"})

#Example 6: elif - multiple conditions

weekno=3

if weekno==1:
    print("Sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("Tueday")
elif weekno==4:
    print("Wedday")
elif weekno==5:
    print("Thursday")
elif weekno==6:
    print("Friday")
elif weekno==7:
    print("Satday")
else:
    print("Invalid week")

