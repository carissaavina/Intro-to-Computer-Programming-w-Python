#!/usr/bin/env python
# coding: utf-8

# In[67]:


# Name: Carissa Avina-Beltran
# Date: 3/12/2021
# Course: CSC 309
# Assignment #5
# Inputs: none
# Outputs: Hello world Python program that will print my name, the date, lists of various elementsizes will 
#          be created, sorted, and verified for ascending order. The amount of time it takes to sort the each 
#          list will be collected into a new list. After all lists are run through, we will plot a graph 
#          of the time elapsed  vs the elements in a problem size. 
# Dependencies: random, time, matplotlib
# Assumptions: written/tested with Python 3.8.5 on MacOS 11.0

import random 
import time #takes time when called
import matplotlib.pyplot as plt
import numpy as np
import array

#fcn checks that items in list L are in ascending order, returns True if sorted, False otherwise
def isSorted(L):
    for i in range(len(L)-1):
        if (L[i] > L[i+1]):
            return False
    return True
#end of isSorted fcn

#fcn Bubble sort sorts code in ascending order, inputs a list, nothing returned, list is adjusted
def BubbleSort(L):
    n = len(L)
    for j in range(n-1):
        for i in range(n-j-1):
            if (L[i+1] < L[i]):
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
    return #void return value
#end of BubbleSort() fcn

#doListProblems takes in problemSizes, seed, randomMin, randomMax
#returns list with runtime of Bubblesort of each problem size
def doListProblems(problemSize, seedValue, randomMin, randomMax):
    returnTime = list() #empty list of times
    for i in problemSize: 
        print("doListProblems, doing problem size=", i)
        random.seed(seedValue)
        toSort = random.sample(range(randomMin, randomMax), randomMax)
        t1 = time.monotonic()
        BubbleSort(toSort)
        t2 = time.monotonic()
        returnTime.append((t2-t1)*1000)
        print("doListProblems size=", i, "list sorted status after sort = ", isSorted(toSort))
        print("")
    return returnTime
#end of doListProblems()

#doArrayProblems takes in problemSize, seed, randomMin, randomMax, returns list with BubbleSort time
#for sizes of arrays
def doArrayProblems(problemSize, seedValue, randomMin, randomMax): 
    returnTime = list()
    for i in problemSize:
        print("doArrayProblems, doing problem size = ", i)
        random.seed(seedValue)
        toSort = array.array("I")
        for j in range(i):
            toSort.append(random.randint(randomMin, randomMax))
        t1 = time.monotonic()
        BubbleSort(toSort)
        t2 = time.monotonic()
        returnTime.append((t2-t1)*1000)
        print("doArrayProblems size=", i, "list sorted status after sort = ", isSorted(toSort))
        print("")
    return returnTime
#end of doArrayProblems()

#doNumpyProblems takes in problemSize, seed, randomMin, randomMax, returns list with BubbleSort time
#for sizes of arrays in numpy
def doNumpyProblems(problemSize, seedValue, randomMin, randomMax):
    returnTime = list()
    for i in problemSize: 
        print("doNumpyProblems, doing problem size = ", i)
        random.seed(seedValue)
        toSort = np.zeros(i, dtype=int)
        for j in range(i):
            toSort[j] = random.randint(randomMin, randomMax)
        t1 = time.monotonic()
        BubbleSort(toSort)
        t2 = time.monotonic()
        returnTime.append((t2-t1)*1000)
        print("doNumpyProblems size=", i, "list sorted status after sort = ", isSorted(toSort))
        print("")
    return returnTime
#end of doNumpyProblems
 
#create plot
def BarChart(labels, variableNames, listTime, arrayTime, numpyTime):
    xcoords = np.arange(len(labels)) #bars on x-axis
    width = 0.25

    plt.xlabel('Problem Size') #start of labels
    plt.ylabel('Elapsed Time (ms)')
    plt.title('Bubble Sort Runtimes: Lists vs Arrays vs Numpy Arrays')
    plt.xscale("log")
    plt.yscale("log")
    plt.xticks(xcoords, labels) #problem sizes
    #plt.yticks()
    plt.bar(xcoords-width, listTime, width, label= "Lists")
    plt.bar(xcoords, arrayTime, width, label="Arrays")
    plt.bar(xcoords+width, numpyTime, width, label="NumPy")

    plt.legend(variableNames, loc=2) #plot legend

    plt.show() #show plot
    return
#end of create plot

#main()

print("Hello World!") #print out name
myName = "Carissa"
print("Hello " + myName + "!") 
print("Today's date is:", time.asctime())
print("")

#set problem sizes
problemSize = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]
problemSizeString = list(map(str, problemSize))

seedValue = 4 # seed value
randomMin = 0 # set range for random numbers
randomMax = 9999

listTime = doListProblems(problemSize, seedValue, randomMin, randomMax)
arrayTime = doArrayProblems(problemSize, seedValue, randomMin, randomMax)
numpyTime = doNumpyProblems(problemSize, seedValue, randomMin, randomMax)

print("Back in main()...")
print("")
for i in range(len(listTime)):
    print("listTime[i]=", listTime[i], "arrayTime[i]=", arrayTime[i], "numpyTime[i]=", numpyTime[i])

labels = list(map(str, problemSize))
print("Labels are: ", labels)
variableNames = ["Lists", "Arrays", "NumPy"]
BarChart(labels, variableNames, listTime, arrayTime, numpyTime)

#end of main


# In[ ]:





# In[ ]:




