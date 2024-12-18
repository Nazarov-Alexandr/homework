# Вывести первую и вторую производную и построить их графики
import math
import matplotlib.pyplot as plt
x = 0
x_array = []
y_array = []
min_y = 0
max_y = 0
x_of_min_y = 0
x_of_max_y = 0
while True:
    f = math.sin(x) * math.cos(x**2 + 5)
    x_array.append(x)
    y_array.append(f)
    x = x + 0.1
    if x > 5:
        break
print(max_y, x_of_max_y, min_y, x_of_min_y)
x = 0
x_array2 = []
y_array2 = []
while True:
    f = math.cos(x)*math.cos(x**2 + 5) - math.sin(x)*math.sin(x**2 + 5)*2*x
    x_array2.append(x)
    y_array2.append(f)
    x = x + 0.1
    if x > 5:
        break
x = 0
x_array3 = []
y_array3 = []
while True:
    f = -math.sin(x)*math.cos(x**2 + 5) - math.cos(x)*math.sin(x**2 + 5) - (math.cos(x)*math.sin(x**2+5)*2*x + math.sin(x)*math.cos(x**2+5)*2*x*2*x + math.sin(x)*math.sin(x**2+5)*2)
    x_array3.append(x)
    y_array3.append(f)
    x = x + 0.1
    if x > 5:
        break

# plotting the points
plt.plot(x_array, y_array, label="f")
plt.plot(x_array2, y_array2, label="f'")
plt.plot(x_array3, y_array3, label="f''")
plt.legend()
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()