#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Name: Carissa Avina-Beltran
# Date: 1/26/2020
# Course: CSC 309
# Assignment #1: Hello World python program 
# Inputs: input from keyboard, i.e. name 
# Outputs: Hello world Python program that will print my name, the date, the time, then exit
# Dependencies: datetime   
# Assumptions: written/tested with Python 3.8.5 on MacOS 11.0

from datetime import datetime as dt

print("Hello World!")
myName = "Carissa"
print("Hello " + myName + "!")

t = dt.today()
print("Today's date is:")
print(t)


# In[ ]:




