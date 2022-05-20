#18/05/2022. A script to plot a figure that tentatively simulates the relation of eDAR and Temperateness

#Import libraries
#++++++++++++++++++++++++++++++++++++++++++++
import seaborn as sns
import numpy as np
from scipy.integrate import odeint
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from decimal import Decimal
import math
from scipy.integrate import solve_ivp
import pandas as pd
from matplotlib.pyplot import figure
import copy
#from Metamodel_Functions import *
import sys
#++++++++++++++++++++++++++++++++++++++++++++ 


#1. MAIN
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#eDAR as a vector
Min_edar=0;Max_edar=1e6
Resolution=100;Steps=Resolution*Max_edar + 1;
edar=np.arange(Min_edar,Max_edar,Resolution)

print(edar)
#Hill function of temperateness as a function of eDAR
K_edar=0.05*Max_edar;exponent=1
Temperateness=edar**exponent/(edar**exponent+K_edar)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#PLOTS
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Path to save figures
Output_Path='../Results/Figures/'
#Extensions
Extensions=['.pdf','.eps','.png','.svg']

#Fontsizes
size_axis=7;size_ticks=5;size_title=5
#Figure Size
cm = 1/2.54  # centimeters in inches
Width=8*cm;Height=7*cm #Width and height of plots
figure(figsize=(Width, Height), dpi=300)

#Colors
cmap='BrBG';cmap_pieces= matplotlib.cm.get_cmap(cmap)
color_plot=cmap_pieces(0.1)

#Plot Figure
plt.plot(edar,Temperateness,color=color_plot,linewidth=2)

print(Temperateness)
#Axes, title, and ticks
plt.ylabel('Temperateness', fontsize=size_axis)
plt.xlabel('e-DAR (J/g)', fontsize=size_axis)
plt.ylim([0,1])
yticks_labels=[0, 0.5, 1]
plt.yticks(yticks_labels, fontsize=size_ticks)

xticks_labels=[Min_edar, 0.5*(Min_edar + Max_edar), Max_edar]
plt.xticks(xticks_labels, fontsize=size_ticks)
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

sns.despine(top=True, right=True, left=False, bottom=False) 

Name_Fig='Figure_2'
[plt.savefig(Output_Path+Name_Fig+ext,dpi=300) for ext in Extensions]
plt.show()
