# Составить уравнение касательной и нормали к точке, а затем построить их
import math
import matplotlib.pyplot as plt
x = 0
x_array = []
y_array = []
min_y = 0
max_y = 0
x_of_min_y = 0
x_of_max_y = 0
x0 = 1
while True:
    f = math.sin(x) * math.cos(x**2 + 5)
    x_array.append(x)
    y_array.append(f)
    if f > max_y:
        max_y = f
        x_of_max_y = x
    if f < min_y:
        min_y = f
        x_of_min_y = x
    x = x + 0.1
    if x > 5:
        break
print(max_y, x_of_max_y, min_y, x_of_min_y)
x = 0
x_array2 = []
y_array2 = []
f_x0 = math.sin(x0) * math.cos(x0**2 + 5)
der_f_x0 = math.cos(x0)*math.cos(x0**2 + 5) - math.sin(x0)*math.sin(x0**2 + 5)*2*x0
while True:
    f = f_x0 + der_f_x0*(x - x0)
    x_array2.append(x)
    y_array2.append(f)
    x = x + 0.1
    if x > 5:
        break
x = 0
x_array3 = []
y_array3 = []
while True:
    f = f_x0 - 1/der_f_x0 * (x - x0)
    x_array3.append(x)
    y_array3.append(f)
    x = x + 0.1
    if x > 5:
        break

# plotting the points
plt.plot(x_array, y_array, label="f")
plt.plot(x_array2, y_array2, label="Касательная")
plt.plot(x0, f_x0, 'ro')
plt.plot(x_array3, y_array3, label="Нормаль")
plt.legend()
plt.plot(x_of_max_y, max_y, 'ro')
plt.plot(x_of_min_y, min_y, 'ro')
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()