#1. Write a Python script to merge two Python dictionaries
d1={1:'m',2:'o',3:'h',4:'d'}
d2={5:'z',6:'a',7:'h',8:'i',9:'d'}
print(d2)
d3={**d1, **d2}
d2.update(d1) 
print(d1)
print(d3)
print(d2)

#2. Write a program to sort the value from descending to ascending in list and convert it in to a set
l1=[2,3,4,5,6,7,1,2,3,43,12,14]
l1.sort() 
print(l1)
l1.sort(reverse=True)
print(l1)
set1=set(l1) 
print(set1)
type(set1)
type(l1)

#3. Write a Python program to list number of items in a dictionary key and sort the list with the help of a function & without the function.
my_dict={'python':[12,13,21,16],'java':[12,67,54,43],'javascript':[34,87,88,98],'html':[33,66,55,44]}
print("Original dictionary :" + str(my_dict))
res=dict()
for key in sorted(my_dict):
    res[key]=sorted(my_dict[key])
print("Sorted dictionary:" + str(res))

#4. Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.
def fun():
    user=input("Enter the string :")
    word="String is given by user  "
    return user+word[2:]
fun()

#5.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.
def fun3():
    user=input("Enter the string :")
    return user.capitalize()

fun3()
def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, str1[0].upper())
    str1 = char + str1[1:]
    return str1
change_char('Stay home, Stay safe')

#6. Write a Python program to find the repeated items of a list
from collections import Counter
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))

#7.  Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
sum1=a+b+c
print(sum1)
user=int(input("Enter the number to divide sum!"))
if sum1% user==0:
    print("The given input divide")
else :
    print("The given input does not divide sum1")

#8.  Write a Python program to find the Mean,median,mode among three given numbers
    from collections import Counter
    n_num=[3,6,8,1,5]
    n = len(n_num)
    get_sum = sum(n_num)
    mean = get_sum / n
    print("Mean / Average is: " + str(mean))
    n_num.sort()
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
    print("Median is: " + str(median))
    data = Counter(n_num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
    print(get_mode)

#9. Write a Python program to swap cases of a given string
a="Hello"
b="World"
temp=a
a=b
b=temp
print(a,b)
x = a
y = b
x, y = y, x
print(x,y)

#Q10. Write a program to convert an integer to binary & octa decimal
def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")
n=65
decToOctal(n)
n=3
decToOctal(n)