# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:30:00 2022

@author: somu 
"""

import pandas as pd
from scipy import stats

dataBeforeAd = pd.read_excel("C:/Users/raman/Documents/kissanSalesBeforeAd.xlsx")
dataAfterAd = pd.read_excel("C:/Users/raman/Documents/kissanSalesAfterAd.xlsx")

alpha = 0.05

s,p=stats.ttest_ind(dataBeforeAd['Below_10'],dataBeforeAd['11_to_20'])

print()
print("Comparing sales between age group below 10 and Age(11 to 20) Before Ad")
print()
print("Average:")
print("Age(Below 10) | Age(11 to 20)")
print("  ",round(dataBeforeAd["Below_10"].mean(),2),"      ",round(dataBeforeAd["11_to_20"].mean(),2))
print()
print("-",40*"-","-")
print("| Hypothesis Test Result:                  |")
print("-",40*" ","-")
if (p < alpha):
    print("| P Value is Low, Null Rejected (Not Same) |")
    print("-",40*"-","-")
else:
    print("| P Value is High, Null Accepted (Same)    |") 
    print("-",40*"-","-")
print()
print(23*"-->")    
print()
s1,p1 = stats.ttest_ind(dataAfterAd['Below_10'],dataAfterAd['11_to_20'])

print("Comparing sales between age group below 10 and Age(11 to 20) After Ad")
print()
print("Average:")
print("Age(Below 10) | Age(11 to 20)")
print("  ",round(dataAfterAd["Below_10"].mean(),2),"      ",round(dataAfterAd["11_to_20"].mean(),2))
print()
print("-",40*"-","-")
print("| Hypothesis Test Result:                  |")
print("-",40*" ","-")
if (p1 < alpha):
    print("| P Value is Low, Null Rejected (Not Same) |")
    print("-",40*"-","-")
else:
    print("| P Value is High, Null Accepted (Same)    |")  
    print("-",40*"-","-")


