import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

#
# Filename: interpolate.py
# Author: Saverio Simonelli <saverio.simonelli.95@gmail.com>
# Copyright: 2021 Saverio Simonelli 
# License: MIT license
#


def data(infile):
    df = pd.read_csv(infile)
    listex = df["t"]
    listey = df["maf"]
    #print (listex,listey)
    return listex,listey
infile = "pz.csv"

x, y = data (infile)
x = np.array(x)
y = np.array(y) 
X_Y_Spline = (x, y)
#X_Y_Spline = make_interp_spline(x,y)
X_Y_Spline = CubicSpline(x, y)
print(X_Y_Spline.c)

xx = np.linspace(1, 2, 500)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# Plotting the Graph
fig, ax = plt.subplots()
afont = {'fontname':'Arial'}
tfont = {'fontname':'Times New Roman'}
my_xticks = ['$t_a$', '$t_b$', '$t_c$', '$t_d$', '$t_e$']
plt.xticks(x, my_xticks)
ax.plot(x,y,"s", color= "brown", label ='MAF = "Mutant allele fraction"\n$t_a$ = "blood sample from $t_0$-$t_1$"\n$t_b$ = "blood sample from $t_1$" \n$t_c$ = "blood sample from $t_1$-$t_2$"\n$t_d$ = "blood sample from $t_1$-$t_2$"\n$t_e$ = "blood sample from $t_3$-$t_4$"')
ax.plot(X_, Y_, "y", label = "Spline interpolating empiric points")
legend = ax.legend(bbox_to_anchor=[0.4, 0.05], loc="lower center", shadow=True, fontsize='small')
plt.title("Title", style = 'italic', fontsize = 'medium', **tfont)
plt.xlabel("TIME", **tfont)
plt.ylabel("MAF(%)", **tfont)
plt.savefig("img.png")
plt.show()
