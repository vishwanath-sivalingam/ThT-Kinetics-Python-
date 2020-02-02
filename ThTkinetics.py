# a = top reading
# b = bottom reading
# c = rate
# d = time50    
# x = time

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

thtdata = pd.read_excel('ThTkinetics.xlsx')
xdata = thtdata.iloc[:,0]
ydata = thtdata.iloc[:,1]

# Explain logistic function using four parameters
def func(x,a,b,c,d):
    return (a-b)/(1 + np.exp(-c*(x-d))) + b

popt, pcov = curve_fit(func, xdata, ydata)
print(popt)
p0 = [10000, 8000, 8 , -1]
plt.figure()
plt.plot(xdata, ydata, 'o', label ='ThT fluorescence')
plt.plot(xdata, func(xdata, *popt), 'g-',label='fit')
plt.xlabel('Time (hrs)')
plt.ylabel('Fluorescence units')
plt.legend()
plt.show()

