import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import seaborn as sns
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
sns.set(style ='dark')
fig, bx = plt.subplots()
bx.scatter(x_values,y_values,s=10)

# Set chart title and label axis
bx.set_title("Square Numbers", fontsize=24)
bx.set_xlabel("Value", fontsize=14)
bx.set_ylabel("Square of Value", fontsize=14)

# Set size of the tick labels.
bx.tick_params(axis='both',which='major', labelsize=14)

# Set the range of each axis
bx.axis([0,1100, 0, 1100000])

plt.show()
