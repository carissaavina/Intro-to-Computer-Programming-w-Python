#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Name: Carissa Avina-Beltran
# Date: 3/31/2021
# Course: CSC 309
# Extra Credit Assignment
# Inputs: none
# Outputs: Hello world Python program that will print my name, the date, lists of various element sizes will 
#          be created, sorted, and verified for descending order. The amount of time it takes to sort the each 
#          list will be collected into a new list. After all lists are run through, we will plot a graph 
#          of the time elapsed  vs the elements in a problem size. 
# Dependencies: random, time, matplotlib
# Assumptions: written/tested with Python 3.8.5 on MacOS 11.0

import random 
import time # takes time when called
import matplotlib.pyplot as plt

# fcn checks that items in list L are in ascending order, while loop
# first done with for statement then with while loop
# returns True if sorted, False otherwise
#def isSorted(L):
#    for i in range(len(L)-1):
#       if (L[i] < L[i+1]):
#           return False
#   return True

def isSortedWhile(L):
    i=0
    while (i < len(L)-1):
        if (L[i] < L[i+1]):
            return False
        i += 1
    return True
# end of isSorted fcns

# fcn Bubble sort sorts code in ascending order
# inputs a list, nothing returned, list is adjusted
def BubbleSort(L):
    i=0
    while (i < len(L)-1):
        if (L[i+1] > L[i]): #checking L[i+1] 
            temp = L[i]
            L[i+1] = L[i] #switch from og code
            L[i] = temp
        i +=1
    return # void return value
# end of BubbleSort() fcn


# start of main()

# define problem sizes, in list N
problemSizes = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]

seedValue = 4 # seed value
listMin = 0 # set range for random numbers
listMax = 9999

# print out name
print("Hello World!") 
myName = "Carissa"
print("Hello " + myName + "!") 

# print date from import datetime(dependency)
print("Today's date is:", time.asctime()) 

listTiming = list()

# for all problem sizes
for i in problemSizes: 
    print("Main: Problem Size = ", i)
    print("")
    
    random.seed(seedValue) # reset seed: want same random sequence each time 

    # generate list of random numbers 
    sortList = list()
    
    for j in range(i):
        sortList.append(random.randint(listMin, listMax))
    print("List sort status: ", isSortedWhile(sortList))
    t1 = time.monotonic() # take time 1
    BubbleSort(sortList) #list is sorted
    t2 = time.monotonic() # take time again
    listTiming.append((t2-t1)*1000) # get time passed in milliseconds
    
    print("List is sorted: ", isSortedWhile(sortList))
print("List Timings: ", listTiming)
# end of loop of problem sizes 

# create plot
problemSizeString = list(map(str, problemSizes))

problemSizes = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]
 
plt.xlabel('Problem Size')
plt.ylabel('Elapsed Time (ms)')
plt.title('Bubble Sort Runtime vs. Problem Sizes')
plt.xscale("log")
plt.xticks(problemSizes, problemSizeString)
plt.scatter(problemSizes, listTiming)
plt.plot(problemSizes, listTiming)

# show plot
plt.show()

#end of main + file


# In[ ]:




