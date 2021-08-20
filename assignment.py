                            #Question 1) To calculate area and perimeter of a circle
'''
from math import pi
r = int(input("Enter the radius of the Circle"))
A = pi*(r^2)
P = 2*pi*r
'''

                            #Question 2) To find largest of the 3 numbers entered by user
'''
ar = []
max_nos = int(input('How many numbers do you want to add?\n'))
for numbers in range(0,max_nos):
    number = int(input(f"Enter your {numbers} number -->\n"))
    ar.append(number)

maximum = 0
for x in ar:
    if x>maximum:
        maximum = x
print(maximum)
'''
                            #Question 3) To calculate area and perimeter of a circle
'''
ar = []
max_nos = int(input('How many numbers do you want to add?\n'))
for numbers in range(0,max_nos):
    number = int(input(f"Enter your {numbers} number -->\n"))
    ar.append(number)

ar.sort(reverse=True)
print(ar)

'''
                            #Question 4) To calculate area and perimeter of a circle
'''
n = int(input("enter the Number\n"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
'''
'''
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    
'''



                       #Question 5) To calculate area and perimeter of a circle
'''
ar = []
max_nos = int(input('How many numbers do you want to add?\n'))
for numbers in range(0,max_nos):
    number = int(input(f"Enter your {numbers} number -->\n"))
    ar.append(number)

ar.sort()
a = ar[0]
b = ar[-1]
print(a, b)
'''

'''

arr = []
n = None

while n != 0:
    n = int(input("Enter a number: "))
    arr.append(n)
print(arr)
'''