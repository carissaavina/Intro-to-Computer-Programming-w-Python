#!/usr/bin/env python
# coding: utf-8

# In[62]:


# Carissa Avina-Beltran
# 4/15/2021, CSC 309, HW7 
#
# Demonstrates understanding of generating noise and use of matplotlin subplots. 
# Generates a white noise and gaussian noise. Plots white noise in line plot and histogram. 
# Plots gaussian noise in line plot and histogram. 
#
# Inputs: none
# Outputs: Figure with 4 subplots
# Dependencies: numpy, time, matplotlib
# Assumptions: written/tested with Python 3.8.5 on MacOS 11.0

import numpy as np
import random
import time
import matplotlib.pyplot as plt 

#fcn to make white noise using numpy linspace
def make_white_noise(nSamples, wn_min=-1.0, wn_max=1.0):  
    wn = np.zeros(nSamples, dtype=float)
    for i in range(nSamples):
        wn[i] = np.random.uniform(wn_min, wn_max)
    return wn
#end fcn to make white noise

#fcn to make gaussian noise
def make_gaussian_noise(nSamples, mu=0.0, sigma=0.34):
    gn = np.zeros(nSamples, dtype=float)
    for i in range(nSamples):
        gn[i] = random.gauss(mu, sigma)
    return gn
#end fcn to make gaussian noise

#establish inputs values for noise fcns
nSamples = 1001

wn_min = -1.0
wn_max = 1.0
wn = make_white_noise(nSamples, wn_min, wn_max)
#print("wn = ", wn)

mu = 0.5
sigma = 0.125
gn = make_gaussian_noise(nSamples, mu, sigma )
#print("gn = ", gn)
 
    
#start of main
def main():
    
#print name and intro    
    myName = "Carissa"
    print("Hello " + myName + "!") 
    print("Today's date is:", time.asctime())
    print("")    
    
#call and plot wn fcn    
    make_white_noise(nSamples)
    
    #create top level figure and 2 subplots for white noise
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12,6))
    
    axs[0, 0].set_title('White Noise: min=0, max=1')
    axs[0, 1].set_title('White Noise Histogram')
    axs[1, 0].set_title('Gaussian Noise: mu=0.5, sigma=0.125')
    axs[1, 1].set_title('Gaussian Noise Histogram')
    
    fig.suptitle("Noise Samples & Distributions (N = 1001)".format(), fontsize=18)
    
    #plot noise samples using a line plot
    axs[0, 0].plot(wn, c='plum')
    
    #compute histogram for white noise values
    nBins = 5
    wnh_bins, wnh_edges = np.histogram(wn, nBins)
    
    #axis labels for histogram plt with each label showing bin edges
    wnh_axis_labels = list()
    for i in range(len(wnh_edges)-1):
        wnh_axis_labels.append("%4.2f-%4.2f" % (wnh_edges[i], wnh_edges[i+1])) 
    
    axs[0, 1].set_xticklabels(wnh_axis_labels)
    axs[0, 1].set_xticks(np.arange(nBins+1))
    axs[0, 1].bar(np.arange(nBins), wnh_bins, facecolor='plum')

#call and plot gn fcn
    make_gaussian_noise(nSamples)
    
    #plot noise samples using a line plot
    axs[1, 0].plot(gn, c='darkmagenta')
    
    #compute bins for gaussian noise 
    gnh_bins, gnh_edges = np.histogram(gn, nBins)
    
    #axis labels for histogram plt with each label showing bin edges
    gnh_axis_labels = list()
    for i in range(len(gnh_edges)-1):
        gnh_axis_labels.append("%4.2f-%4.2f" % (gnh_edges[i], gnh_edges[i+1])) 
    
    #plot labels for gaussian
    axs[1, 1].set_xticklabels(gnh_axis_labels)
    axs[1, 1].set_xticks(np.arange(nBins+1))
    axs[1, 1].bar(np.arange(nBins), gnh_bins, facecolor='darkmagenta')
    
    plt.tight_layout()
    plt.show()
    return

    
if __name__ == "__main__":
    main()
    


# In[ ]:




