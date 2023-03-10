#!/usr/bin/env python
# coding: utf-8

# In[65]:


# Name: Carissa Avina-Beltran
# Date: 2/3/2021
# Course: CSC 309
# Assignment #2: 
# Inputs: 2 values from user, N and S
# Outputs: Hello world Python program that will print my name, the date, the time, 
#          then take in input values for program's list size and seed value. 
#          Program will then print the unsorted list, sort the list in ascending order
#          then print the sorted list
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
print("You chose to make the size of the list N: ", N)

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

j=0
for i in L: 
    print(L[j], end='')
    j = j+1
    if ((j%10)==0):
        print("\n", end='')     

#print list unsorted
print('\n')
print("Unsorted list: ", L)

#sort low to high
L.sort()     

#print list sorted, 10 values per row
print("Sorted list: ", L)


# In[ ]:





# In[ ]:




