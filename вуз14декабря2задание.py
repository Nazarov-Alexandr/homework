# Найти наибольшее и наименьшее значение функции на отрезке и отобразить точкой
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
# plotting the points
plt.plot(x_array, y_array, label="f")
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