#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:40:27 2023

@author: merlin
"""
#importing required packages

import pandas as pd
import matplotlib.pyplot as plt

# read file into dataframe and print
df_mcs = pd.read_excel("popular.xlsx")
print(df_mcs)


# line plot

#defining figure size
plt.figure(figsize=(15,10))
# plot the four countries with labels
plt.plot(df_mcs["YEAR"], df_mcs["Cyprus"], label="Cyprus",color = 'violet')
plt.plot(df_mcs["YEAR"], df_mcs["India"], label="India",color = 'green')
plt.plot(df_mcs["YEAR"], df_mcs["Malaysia"], label="Malaysia",color = 'red')
plt.plot(df_mcs["YEAR"], df_mcs["Philippines"], label="Philippines",color = 'black')
plt.plot(df_mcs["YEAR"], df_mcs["Sri Lanka"], label="Sri_Lanka",color = 'blue')
plt.plot(df_mcs["YEAR"], df_mcs["Argentina"], label="Argentina",color = 'brown')
# plotting the  labels and show the legend
#Removing white space from left and right
plt.xlim(2000,2015)
plt.xlabel("YEAR")
plt.ylabel("MOBILE CELLULAR SUBSCRIPTION(weighed average)")
#assigning the title of the graph
plt.title("MOBILE CELLULAR SUBSCRIPTION")
plt.legend() #it will show the index value of the graph
plt.show()
plt.savefig('plot1.png')#saving the image
#This function will plot line graph of Mobile Cellulalar Subscription (per 
#100 people) of four countries from 2000-2015. 

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
# read file into dataframe and print
df_ex = pd.read_excel("LIFE_EXPECTANCY.xlsx")

print(df_ex)

#setting the figure size 
plt.figure(figsize=(10,10))
#plotting the scatter plot for four different countries
plt.scatter(df_ex["YEAR"],df_ex['South Asia'] ,label= "South Asia", color= "g", 
           marker= "*",s=120)


plt.scatter(df_ex["YEAR"],df_ex['European Union'],label= "European Union",marker= "D", s=85)


plt.scatter(df_ex["YEAR"],df_ex['Russian Federation'] ,label= "Russian Federation",color ='r' ,
            marker= ">", s=120)

plt.scatter(df_ex["YEAR"],df_ex['Syrian Arab Republic'] ,label= "Syrian Arab Republic" ,
            marker= "o", s=150)

plt.ylim(40,80)
#labelling x axis
plt.xlabel('NO OF YEARS')
#labelling y axis
plt.ylabel('LIFE EXPECTANCY AT BIRTH')
# plotting the title of the plot
plt.title('LIFE EXPECTANCY IN 1965-1973')
#plotting legend and locating the index
plt.legend(loc = "upper right", framealpha = 0.1)

 
# function to show the plot
plt.show()
plt.savefig('plot2.png')

#this function will plot the scatter plot for the life expectancy at birth, total (years)

#importing required packages
import pandas as pd
import matplotlib.pyplot as plt
#Read the files into dataframes
Exports= pd.read_excel("export_of_goods_and_services.xlsx")
print(Exports)


# pie chart for the seven countries

plt.pie(Exports['export_of_goods_and_services'], labels = Exports['country'], autopct='%1.1f%%' , pctdistance = 0.5 , 
   labeldistance = 1.1,wedgeprops = {'linewidth' : 1.0,'edgecolor' : 'white'} )
plt.title("export_of_goods_and_services in 2018")
plt.show()
plt.figure()

#plt.pie(Exports['year'], labels=Exports['country name'], normalize=False)
plt.show()
plt.savefig('plot3.png')

#this pie chart shows the percentage of goods and services in 2018 between five different countries.

