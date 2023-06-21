# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:28:28 2023

@author: william
"""

#  1.1.4 Writing and Running Your First Python Program
# Pag 4



# ----------------------------------------------------
# Name requiered in book for file: ball1.py


# Fórmula para el movimiento en caida libre 

print(5*0.6 - 0.5*9.81*0.6**2)

print(1*0.1 - 0.5*9.81*0.1**2)

# ----------------------------------------------------
# Name requiered in book for file: ball12.py

# Fórmula para el movimiento en caida libre 
# using variables:: 
v0 = 5          #initial velocity
g = 9.81        #gravity aceleration
t = 0.6         #time
y = v0*t - 0.5*g*t**2   #position
print("this is y with variables", y)


# ---------------------------------------------------
# 1.1.11 Formatting Text and Numbers

print("At t =%g s, the height of the ball is %.2f m." %(t,y))




# ---------------------------------------------------