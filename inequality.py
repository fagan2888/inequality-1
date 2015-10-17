
# Autor: maximiliano greco
# Version: 0.1
# Fecha: 17-10-2015
# Python version: 3.5

def dist_lorentz(x):
    import numpy as np
    
    y = np.array(x)           # y-axis data
    y = np.sort(y, kind='mergesort')

    x = np.repeat(1, len(y))  # x-axis data

    pct_x = x / sum(x)        # x normalized
    pct_x = np.cumsum(pct_x)  # CDF x

    pct_y = y / sum(y)        # y normalized
    pct_y = np.cumsum(pct_y)  # CDF y

    # starts with (0,0)

    pct_y = np.insert(pct_y, 0, 0) 
    pct_x = np.insert(pct_x, 0, 0)

    return pct_x, pct_y

def gini(x , weight = None):
    '''
    gini(x, weight)

    Calculates the index gini to an array or list given.
    INPUTS:
        x: It is an 1-D array of monetary variable.
        weight: It is an 1-D array of wieghts of x

    RETUNRS: The gini index of x
    
    '''
    import scipy as sp

    # weight case
    
    x, y = dist_lorentz(x)

    B = sp.integrate.trapz(y, x)  # area under lorentz curve
    AB = 0.5                              # area under bisetrix curve
    A = AB - B                            # area between lorentz and bisetrix
    res = A / AB                          # gini index

    return res

def lorentz_curve(x):
    
    import matplotlib.pyplot as plt
    
    # weight case
    
    x, y = dist_lorentz(x)
    
    fig = plt.figure(figsize=(5,5))

    plt.plot(x, y, 'r-', alpha=0.7) # curva de lorentz
    plt.plot([0,1],[0,1], color='black') # line 45º

    plt.xlabel('CDF x (%)')
    plt.ylabel('CDF y (%)')

    plt.suptitle('Lorentz Curve', fontsize=15)
    plt.xlim(0,1)
    plt.ylim(0,1)
    return plt.show()