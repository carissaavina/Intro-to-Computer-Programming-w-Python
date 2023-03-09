#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Carissa Avina-Beltran
# 4/29/2021, CSC 309, HW9
#
# Plot Fractal Skyline using recursive fcn. Midpoints are computed with some 
# scaled offset. User is asked for inputs in main to dictate recursive depth.
# Program checks that input is less than or equall to and greater than 0. Else 
# program ends. 
#
# Inputs: User input in main asks for integer from user in range 0 to 20  
# Outputs: Plot fractal skyline slightly offset.  
# Dependencies: numpy, time, matplotlib, random, datetime
# Assumptions: written/tested with Python 3.8.5 on MacOS 11.0

import numpy as np
import random
import time
import datetime
import matplotlib.pyplot as plt 


# fcn gets midpoint of (x1, y1) and (x2, y2) at location i and gets y offset
def get_midpoint(x1, y1, x2, y2, scale):
    x_not = (x2-x1)*0.5 + x1
    y_not = (y2-y1)*0.5 + y1
    scale = random.uniform(0,1)
    
    offset = scale *(x2-x1)*random.uniform(0,1) # modify y_not with an offset
    y_not += offset
    
    return x_not, y_not    
# return x and y of midpoint to caller 


# recursive fcn computes a midpoint of (x1,y1),(x2,y2), insert into a list, w. offset in y that is a fcn of x-magnitude and some randomness
def calc_midpoint(xvals, yvals, i, scale, recursion_depth):   
    x_not, y_not = get_midpoint(xvals[i], yvals[i], xvals[i+1], yvals[i+1], scale)
    xvals.insert(i+1, x_not)
    yvals.insert(i+1, y_not)
    
    #print("calc_midpoint: recursion_depth={}".format(recursion_depth))
    
    if (recursion_depth==1):
        #print("Congrats! You reached the bottom of the barrel!")
        return
    else:           # recurse to the right, then left
        calc_midpoint(xvals, yvals, i+1, scale, recursion_depth-1)
        calc_midpoint(xvals, yvals, i, scale, recursion_depth-1)
        # print("X-Vals: ", xvals)
        # print("Y-Vals: ", yvals)
        return 
# returns to main
                                           
                                           
# start of main
def main():
    
    
    #print name and intro     
    print("Name: Carissa. Today's date is:", time.asctime())
    print("\n")  
    
    # controls how "bumpy" or "smooth" your terrain will be
    scale_parameter = 0.1 # can range from 0.0 to 1.0
    
    while True: 
        try:
            recursion_depth = int(input("Please enter a positive integer from 0 and 20 for the recursion depth: "))
            if 20 >= recursion_depth > 0:      # verifies that user input falls within range
                pass
            else: raise ValueError
        except ValueError:                      # ends program if user input is not in range
            print("Not valid. Please try again.")
            return
            
        
        for r in range(1, recursion_depth+1): 
            
            split_index = 0
    
            # set up the problem
            recursion_depth = 0
            xvals = [0.0, 10.0]   # [x1, x2]
            yvals = [0.0, 1.0]    # [y1, y2]
        
            plt.title('Fractal Skyline Using Recursion, depth = {}'.format(r)) # fix this to print recursion depth                                        

            # call/initiate recursive fcn to update xvals, yvals
            calc_midpoint(xvals, yvals, split_index, scale_parameter, r)
                 
            # plot fractal skyline 
            plt.plot(xvals, yvals, color = "hotpink")
            plt.scatter(xvals, yvals, color = 'purple')
            plt.show()                                       
                                           
            time.sleep(2) # program sleeps for 2 seconds before next loop iteration
    
    return
    
# end of main

 
if __name__ == "__main__":
    main()

# end of file     


# In[ ]:




