#1. Write a program to loop through a list of numbers and add +2 to every value to elements in list
list1=[10,11,12,13,14,15,16,17,18,19,20]
result=[]
for i in list1:
    result.append(i+2)
print(result)

#2. Write a program to get the below pattern
54321
4321
321
21
1 

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

#3. Python Program to Print the Fibonacci sequence
def Fib(n):
   
    if n < 0:
        print("Incorrect input")
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fib(n-1) + Fib(n-2)
print(Fib(11))

def Fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    if n<0:
        print("Incorrect Input")
    elif n == 1 or n == 2:
        print('1')
    else :
         while count < n:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
Fibonacci(12)

#4. Explain Armstrong number and write a code with a function armstrong number the number whose digit cube is equal to the same number Example :153 111=1 555=125 333=27 1+125+27=153 this is the same input number
num = int(input("Enter a number: "))
sum1 = 0
temp1 = num
while temp1 > 0:
    digit1 = temp1 % 10
    sum1 += digit1**3
    temp1 //= 10
if num == sum1:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

#5. Write a program to print the multiplication table of 9
for i in range(1,11):
    print("9 x ",i,' = ',i*9 )

#6. Check if a program is negative or positive
gi=[0,2,+3,-9,6,+8,-55]
for i in gi:
    if i >=0:
        print(i," is positive")
    else :
        print(i,' is negative ')

#7. Write a program to convert the number of days to ages
def find( number_of_days ):
    year = int(number_of_days / 365)
    print(year,'Years ago !')

#8. Solve Trigonometry problem using math function write a program to solve using math function
import math
def trigo(n,m):
    if n=='sin':
        return math.sin(m)
    elif n=='cos':
        return math.cos(m)
    elif n=='cosin':
        return math.cosine(m)
    elif n=='tan':
        return math.tan(m)
    elif n=='sec':
        return math.sec(m)
    elif n=='cosec':
        return math.cosec(m)
trigo('sin',30)
trigo('cos',90)
trigo('tan',60)

#9. create a basic calculator using if condition only
def calculator():
    print('+')
    print('-')
    print('*')
    print('/')
    print('%')
    print('**')
    operation = input("Select an operator:n")
    print("Enter two numbers")
    number_1 = int(input())
    number_2 = int(input())

    if operation == '+': # To add two numbers
        print(number_1 + number_2)
    elif operation == '-': # To subtract two numbers
        print(number_1 - number_2)
    elif operation == '*': # To multiply two numbers
        print(number_1 * number_2)
    elif operation == '/': # To divide two numbers
        print(number_1 / number_2)
    elif operation == '%': # To remainder two numbers
        print(number_1 % number_2)
    elif operation == '**': # To num1 exponent num2
        print(number_1 ** number_2)
    else:
        print('Invalid Input')
calculator()