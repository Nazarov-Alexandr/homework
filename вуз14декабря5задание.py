# Найти длину кривой через интеграл
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
x0 = 0
while True:
    x = 0
    x_array2 = []
    y_array2 = []
    f_x0 = math.sin(x0) * math.cos(x0 ** 2 + 5)
    der_f_x0 = math.cos(x0) * math.cos(x0 ** 2 + 5) - math.sin(x0) * math.sin(x0 ** 2 + 5) * 2 * x0
    while True:
        f = f_x0 + der_f_x0 * (x - x0)
        x_array2.append(x)
        y_array2.append(f)
        x = x + 0.1
        if x > 5:
            break
    plt.plot(x_array2, y_array2, color="r")
    x0 = x0 + 1.5
    if x0 > 5:
        break
# plotting the points
plt.plot(x_array, y_array, label="f")
plt.legend()
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()

L = 0
x = 0
while True:
    der_f_x = math.cos(x) * math.cos(x ** 2 + 5) - math.sin(x) * math.sin(x ** 2 + 5) * 2 * x
    L = L + (1 + der_f_x**2)**0.5 * 0.1
    x = x + 0.1
    if x > 5:
        break
print(L)