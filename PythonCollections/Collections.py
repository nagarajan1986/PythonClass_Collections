
#Collections
#1. List
#2. Set
#3. Tuple
#4. Dictionary

#List is a collection which is ordered and changeble. Lists are written in square bracket [ ]. List is mutable.

mylist1=[432,3424,43243,4332,3224,343,3443,433,"nagaraj"]
mylist2=["apple", "cherry", "tomato"]
mylist3=[20.5, "cherry", "tomato"]
mylist4=list()

print(mylist1[2:5])
# mylist5=mylist1.copy()
# print(mylist5)

mylist1.append("orange")
print(mylist1)
mylist1.insert(0, "cherry")
print(mylist1)

#mylist1.pop(0)
#print(mylist1)

mylist1.remove("cherry")
print(mylist1)
mylist1.extend(mylist2)
print(mylist1)

# del mylist1[-1]
# print(mylist1)

# mylist2=list(mylist1)
# print(mylist2)

#copying two lists
list1=["apole", "cherry", "avacado"]
list2=[1,2,3,4]

list3=list1+list2
print(list3)

for i in list2:
    list1.append(i)
print(list1)

print("===================================================================")

#Tuple is a collection which is ordered and unchangeble. Tuple are written in parenthesis ( ). Tuple is Immutable.

mytuple=("apple", "cherry", "tomato", "grapes", "brinjal", "avacado")
print(mytuple)

#access tuple items using index and slicing also by using index
print(mytuple[0])
print(mytuple[-1])
print(mytuple[1:4])

#changeing tuple by convert into list. becoz tuple is unchangable or immutable:
mytuple=("apple", "cherry", "tomato", "grapes", "brinjal", "avacado")
mylist=list(mytuple)
mylist.append("onion")
mylist[0]="broomstick"
print(mylist)

mytuple=tuple(mylist)
print(mytuple)

#searching items in tuple or not
if "cherry" in mytuple:
    print("Yes. cherry is present")
else:
    print("NO. cherry is present")

#copying tuple
mytuple1=("apple", "cherry", "tomato", "grapes", "brinjal", "avacado")
mytuple2=mytuple1
print(mytuple2)

#combining/join
mytuple1=("apple", "cherry", "tomato", "grapes", "brinjal", "avacado")
mytuple2=("cherry", "tomato", "grapes", "brinjal", "avacado")
mytuple3=mytuple1+mytuple2
print(mytuple3)

#check equal or not:
mytuple1=("apple", "cherry", "tomato", "grapes", "brinjal", "avacado")
mytuple2=("apple", "cherry", "tomato", "grapes", "brinjal", "avacado")

if mytuple1==mytuple2:
    print("YES")
else:
    print("NOT")

print("===================================================================================================")

#Set is a collection which is unordered and changeble. Set are written in parenthesis { }. Set is mutable. Not having index:

#creating a set:
myset={"apple", "cherry", "banana", "avacado"}
print(myset)

#access items from the set: But we cannot access individual item since it is non indexed
myset={"apple", "cherry", "banana", "avacado"}

for i in myset:
    print(i)

#checking the value exist or not in set
myset={"apple", "cherry", "banana", "avacado"}
print("banana" in myset)

#adding new items to the set:     add()    update()
myset={"apple", "cherry", "banana", "avacado"}
myset.add("oranges")   #=========>add only one item at a time
print(myset)

myset.update(["onion", "carrot", "brinjal"])    #=========>by using update we can add more than one items at a time
print(myset)

#find length of a set
myset={'oranges', 'banana', 'onion', 'brinjal', 'apple', 'cherry', 'avacado', 'carrot'}
print(len(myset))

#remove the item from set:  remove()    discard()
myset={'oranges', 'banana', 'onion', 'brinjal', 'apple', 'cherry', 'avacado', 'carrot'}
myset.remove("onion")
print(myset)

myset.discard("carrot")
print(myset)

#joining two sets:  union()   update()

myset1={'oranges', 'banana', 'onion', 'brinjal', 'apple', 'cherry', 'avacado', 'carrot'}
myset2={"ladysfinger", "drumstick"}
myset3=myset1.union(myset2)
print(myset3)

myset3.update({"reddish", "tomato"})
print(myset3)

print("===================================================================================================")

#Dictionary is a collection which is unordered and changeble. Dictionary are written in parenthesis { }. Dictionary is mutable. It is indexed:
# it has key and value pair like maps in java language. Here key should be unique and value can be duplicate.

#create a dictionary:
mydict={"brand":"LG", "product":"Trimmer", "Year":2022}
print(mydict)

#access items from dict:   get()   passing key
mydict={"brand":"LG", "product":"Trimmer", "Year":2022}
print(mydict["product"])            #====>by passing the key to get items individual

print(mydict.get("brand"))    #====>by using get() passing the key to get items individual

#CHANGE value in dictionary:
mydict={
    "brand":"LG",
    "product":"Trimmer",
    "Year":2022
}
mydict["Year"]=2023
print(mydict)

#read items in dict using loop statement:
mydict={
    "brand":"LG",
    "product":"Trimmer",
    "Year":2022
}

for i in mydict:
    print(i) #===============> read only key only

for i in mydict:
    print(mydict[i]) #===============> read only values only

for i in mydict.values(): #===============> read only values only
    print(i)

for x,y in mydict.items(): #===============> read all key and values
    print(x,y)

#check particular key exist or not:
mydict={
    "brand":"LG",
    "product":"Trimmer",
    "Year":2022
}

if "brand" in mydict:
    print("YES")
else:
    print("NOT")
#=======================================
print("product" in mydict)

#to find length of dictionary:
print(len(mydict))

#adding items into the dict:
mydict={
    "brand":"LG",
    "product":"Trimmer",
    "Year":2022
}

mydict["model"]="BMW"
mydict["car"]="Benz"
print(mydict)

#remove items from dict: pop()   del
# mydict.pop("Year")
# print(mydict)

# del mydict["car"]
# print(mydict)
#
# del mydict
# print(mydict)

#copying dict: copy()
mydict1={
    "brand":"Samsung",
    "product":"Speaker",
    "Year":2023
}

mydict2=mydict1
print(mydict2)

mydict2=mydict1.copy()
print(mydict2)

print("=======================================")
print("Collections concept over!!!!!!")


