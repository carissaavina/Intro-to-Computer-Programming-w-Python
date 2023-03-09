#!/usr/bin/env python
# coding: utf-8

# In[26]:


# Name: Carissa Avina-Beltran
# Date: 2/15/2021
# Course: CSC 309
# Assignment #3 
# Inputs: 2 values from user, N and S
# Outputs: Hello world Python program that will print my name, the date, the time, take
#          in values for list size N and seed value S. A list is created of list number
#          N with random values between a min and max value. The unsorted list is 
#          printed out with 10 items per list. Then a bubble sorted list is printed with
#          10 items per list. 
# Dependencies: datetime, random    
# Assumptions: written/tested with Python 3.8.5 on MacOS 11.0

from datetime import datetime as dt
import random 

#print out name
print("Hello World!") 
myName = "Carissa"
print("Hello " + myName + "!") 

#print date from import datetime(dependency)
t = dt.today()
print("Today's date is:") 
print(t)

#beginning assignment2

#prompt user for two values 
#get input from user for list size
N = int(input("Enter a number for N: "))
print("You chose to make the size of the list N:", N)

#initialize random number generator with seed value input from user
S = input("Enter a number or seed value for S: ") 
random.seed(S)

#set range for random numbers 
listMin = 0
listMax = 99

#create empty list
L = list()

#create loop that builds list 
for i in range(N): 
    L.append(random.randint(listMin, listMax))

#print unsorted list
print("Unsorted list is: ") 

#print 10 items per line
k=0
for i in L: 
    print(L[k], end= ' ')
    k = k+1
    if ((k%10)==0):
        print(" \n ", end= ' ')

#bubble sort
for j in range(N-1):
    for i in range(N-j-1):
        if (L[i+1] < L[i]):
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp
            
#print sorted list  
print("\n")
print("List after bubble sort: ")

#print 10 items per line after bubble sort 
k=0
for i in L: 
    print(L[k], end= ' ')
    k = k+1
    if ((k%10)==0):
        print(" \n ", end= ' ')


   


# In[6]:


# Name: Carissa Avina-Beltran
# Date: 2/15/2021
# Course: CSC 309
# Assignment #3 
# Inputs: 2 values from user, N and S
# Outputs: Hello world Python program that will print my name, the date, the time, take
#          in values for list size N and seed value S. A list is created of list number
#          N with random values between a min and max value. The unsorted list is 
#          printed out with 10 items per list. Then a bubble sorted list is printed with
#          10 items per list. 
# Dependencies: datetime, random    
# Assumptions: written/tested with Python 3.8.5 on MacOS 11.0

from datetime import datetime as dt
import random 

#print out name
print("Hello World!") 
myName = "Carissa"
print("Hello " + myName + "!") 

#print date from import datetime(dependency)
t = dt.today()
print("Today's date is:") 
print(t)

#beginning assignment2

#prompt user for two values 
#get input from user for list size
N = int(input("Enter a number for N: "))
print("You chose to make the size of the list N:", N)

#initialize random number generator with seed value input from user
S = input("Enter a number or seed value for S: ") 
random.seed(S)

#set range for random numbers 
listMin = 0
listMax = 99

#create empty list
L = list()

#create loop that builds list 
for i in range(N): 
    L.append(random.randint(listMin, listMax))

#print unsorted list
print("Unsorted list is: ") 

#print 10 items per line
k=0
for i in L: 
    print(L[k], end= ' ')
    k = k+1
    if ((k%10)==0):
        print(" \n ", end= ' ')

#bubble sort
i=0
while (i < len(L)-1):
    if (L[i+1] > L[i]):
        temp = L[i]
        L[i+1] = L[i]
        L[i] = temp
    i +=1
            
#print sorted list  
print("\n")
print("List after bubble sort: ")

#print 10 items per line after bubble sort 
k=0
for i in L: 
    print(L[k], end= ' ')
    k = k+1
    if ((k%10)==0):
        print(" \n ", end= ' ')


# In[ ]:




