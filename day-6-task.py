# 1)Write a python script to merge two python dictionaries
from typing import KeysView


X={'a':10,'b':20}
Y={'c':5,'d':15}
def Merge(X,Y):
    return(Y.update(X))
print(Merge(X,Y))
print(Y)

# 2)Write a python program to remove a key from dictionary
X={'a':'regret','b':'readme','c':'landing','d':'regarding'}
print(X)
Y=X.pop('d')
print(X)
print('Removed elements:',Y)

# 3)Write a python program to map two lists into a dictionary
Keys=['red','pink','black']
values=['1','2','3']
color_dictionary=dict(zip(Keys,values))
print(color_dictionary)

# 4)Write a python program to find length of the set
a={'a','b','c','d'}
print(len(a))

# 5)Write a python program to remove the intersection of a second set from the first set
a={1,2,3,4,5}
b={4,5,6,7,8}
print("Original sets:")
print(a)
print(b)
print("\nRemove the intersection of 2nd set from the 1st set using difference_update():")
a.difference_update(b)
print("a: ",a)
print("b: ",b)
sn1={1,2,3,4,5}
sn2={4,5,6,7,8}
print("\nRemove the intersection of 2nd set from the 1st set using -= operator:")
a-=b
print("a: ",a)
print("b: ",b)