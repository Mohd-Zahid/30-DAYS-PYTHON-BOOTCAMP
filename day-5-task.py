# 1)Write a program to create a list of n integer values
a=[10,20,30,40,50]
print(a)

#add an item into the list (using function)
a=[10,20,30,40,50]
print(a)
a.append(60)
print(a)

#delete (using function)
a=[10,20,30,40,50]
print(a)
del a[3]
print(a)

#store the largest number from the list to a variable
def myMax(a):
    max=a[0]
    for x in a:
        if x>max:
            max=x
    return max
a=[10,20,29,39,90]
print("Largest element is:", myMax(a))

#store the smallest number from the list to a variable
def myMin(a):
    min=a[1]
    for x in a:
        if x<min:
            min=x
    return min
a=[10,20,29,39,90]
print("Smallest element is:",myMin(a))

# 2)Create a tuple and print the reverse of the created tuple
a=("Java","Python","HTML","PHP")
b=reversed(a)
print(tuple(b))

# 3)Create a tuple and convert tuple into list
a=("Java","Python","HTML","PHP")
aList=list(a)
print("List elements:",aList)