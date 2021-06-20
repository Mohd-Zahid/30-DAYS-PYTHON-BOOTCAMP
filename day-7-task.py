#Create a function getting two integer inputs from user and print the following
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
print(a,b)

#Addition of two numbers is +value
a=input("Enter the first number:")
b=input("Enter the second number:")
sum=int(a)+int(b)
print('The addition of {0} and {1} is {2}'.format(a,b,sum))

#Subtraction of two numbers is +value
a=input("Enter the first number:")
b=input("Enter the second number:")
sub=int(a)-int(b)
print("The subtraction of {0} and {1} is {2}".format(a,b,sub))

#Division of two numbers is +value
a=input("Enter the first number:")
b=input("Enter the second number:")
div=int(a)/int(b)
print("The division of {0} and {1} is {2}".format(a,b,div))

#Multiplication of two numbers is +value
a=input("Enter the first number:")
b=input("Enter the second number:")
mul=int(a)*int(b)
print("The multiplication of {0} and {1} is {2}".format(a,b,mul))

#Create a function covid() and it should accept patient name and body temperature, by default the body temperature should be 98 degree
def covid(name,temp):
    print("Name of patient is",name)
    if temp == '':
        print("Body temperature : 98")
    else:
        print("Body temperature :",temp)
name=input("Enter the patient name :")
temp=input("Enter the body tenperature :")
covid(name,temp)