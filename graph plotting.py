#graph plotting 

import matplotlib.pyplot as plt                      # Importing the data visualization and graphical plotting library 

x = [ 1,2,3,4,5]

y = [ 12,11,31,23,24,]

plt.plot(x,y,label= 'first line')                    # label is to name the line 

w = [4,5,6,1,2]

z = [15,23,19,26,35]

plt.plot(w,z, label = ' second line')

plt.xlabel = 'x - axis'                              # xlabel is to name the x axis 
plt.ylabel = 'y - axis'                              # Similarly y label

plt.title = 'Comparing 2 graphs'

plt.legend()                                         # It is used to show different lines in a different color 

plt.show()

