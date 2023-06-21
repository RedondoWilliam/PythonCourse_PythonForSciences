# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:28:28 2023

@author: william
"""

#  1.1.4 Writing and Running Your First Python Program
# Pag 4




print(" ---------------------------------------------------")
print("Name requiered in book for file: ball1.py")



# Name requiered in book for file: ball1.py


# Fórmula para el movimiento en caida libre 

print(5*0.6 - 0.5*9.81*0.6**2)

print(1*0.1 - 0.5*9.81*0.1**2)


print(" ---------------------------------------------------")
print("Name requiered in book for file: ball12.py")

# Name requiered in book for file: ball12.py

# Fórmula para el movimiento en caida libre 
# using variables:: 
v0 = 5          #initial velocity
g = 9.81        #gravity aceleration
t = 0.6         #time
y = v0*t - 0.5*g*t**2   #position
print("this is y with variables", y)



print(" ---------------------------------------------------")
print("1.1.11 Formatting Text and Numbers")



# 1.1.11 Formatting Text and Numbers

print("At t =%g s, the height of the ball is %.2f m." %(t,y))


#Source for next  code: https://github.com/hplgit/scipro-primer/blob/master/src/formulas/printf_demo.py

# other ways for write number in different formats are: 

i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print ('"%d"' % i  )     # minimum field
print ('"%5d"' % i  )    # field of width 5 characters
print ('"%05d"' % i )    # pad with zeros

print ('"%g"' % r   )    # r is big number so this is scientific notation
print ('"%G"' % r   )    # E in the exponent
print ('"%e"' % r   )    # compact scientific notation
print ('"%E"' % r   )    # compact scientific notation
print ('"%20.2E"' % r )   # 2 decimals, field of width 20
print ('"%30g"' % r   )  # field of width 30 (right-adjusted)
print ('"%-30g"' % r  )  # left-adjust number
print ('"%-30.4g"' % r )  # 3 decimals

print ('%s' % i  ) # can convert i to string automatically
print ('%s' % r )

# Use %% to print the percentage sign
print ('%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346) )

#finished cited code,https://github.com/hplgit/scipro-primer/blob/master/src/formulas/printf_demo.py 

# more number formats 


print ('"%s"' % i  )
print ('"%d"' % i  )
print ('"%0xd"' % i  )
print ('"%f"' % i  )
print ('"%e"' % i  )
print ('"%E"' % i  )
print ('"%g"' % i  )
print ('"%G"' % i  )
print ('"%xz"' % i  )
print ('"%-xz"' % i  )
# print ('"%.yz"' % i  )
print ('"%x.yz"' % i  )
# print ('"%%"' % i  )





print(" ---------------------------------------------------")
print("practice using ball1.py for triple-qouted")



# practice using ball1.py for triple-qouted

# Fórmula para el movimiento en caida libre 
# using variables:: 
# v0 = 5          #initial velocity
# g = 9.81        #gravity aceleration
# t = 0.6         #time
# y = v0*t - 0.5*g*t**2   #position

print("""At t = %f, a ball with initial velocity v0 = %.3E m/s is 
      located at the height %.2f m.""" % (t, v0, y))


# other format for strings in python is:
    
print("At t = {t:g} s, the height of the ball is {y:.2f} m." .format(t=t, y=y))


print(" ---------------------------------------------------")






















print(" ---------------------------------------------------")
print(" ---------------------------------------------------")
print(" ---------------------------------------------------")
print(" ---------------------------------------------------")
print(" ---------------------------------------------------")
print(" ---------------------------------------------------")
print(" ---------------------------------------------------")
print(" ---------------------------------------------------")







