# Используя построенный в предыдущем задании график кривой, построить пользовательский интерфейс, содержащий следующее:
# I. Слайдер, перемещение которого приводит в движение точку на кривой;
# II. Флажок, включающий/выключающий касательную к точке;
# III. Кнопка, возвращающая точку в начальное положение;
# IV. Радиокнопка, меняющая цвет и стиль линии графика.

import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.widgets import CheckButtons, Slider, Button, RadioButtons


x = 0
x_array = []
y_array = []
while True:
    f = math.sin(x) * math.cos(x**2 + 5)
    x_array.append(x)
    y_array.append(f)
    x = x + 0.1
    if x > 5:
        break

x0 = 3
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

fig, ax = plt.subplots()
main_line, = ax.plot(x_array, y_array,  lw=2, color='red', label='graph')
kasat, = ax.plot(x_array2, y_array2, lw=2, color='red', label='kasat')
point, = ax.plot(1, 1, linewidth=2, color="orange", marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")

fig.subplots_adjust(left=0.25, bottom=0.25)

# Radio buttons to change line color
color_area = fig.add_axes((0.025, 0.5, 0.15, 0.15))
color_buttons = RadioButtons(color_area, ('red', 'blue', 'green'), active=0)

style_area = fig.add_axes((0.025, 0.25, 0.15, 0.15))
style_buttons = RadioButtons(style_area, ('solid', 'dotted'), active=0)


ax.set_xlim([0, 5])
ax.set_ylim([-1, 1])

# Slider for Amplitude
amp_slider_area = fig.add_axes((0.25, 0.15, 0.65, 0.03))
amplitude_slider = Slider(amp_slider_area, 'Amplitude', 0.1, 10.0)

# Reset button for sliders
reset_area = fig.add_axes((0.6, 0.025, 0.1, 0.04))
reset_button = Button(reset_area, 'Reset', hovercolor='0.975')


# Make checkbuttons with all plotted lines with correct visibility
rax = ax.inset_axes([0.0, 0.0, 0.12, 0.2])
check = CheckButtons(
    ax=rax,
    labels=["kasat",],
    actives=[True,]
)

def update_plot(val):
    if amplitude_slider.val < 10:
        amount_of_x = len(x_array)
        index_of_point = round(amount_of_x * amplitude_slider.val // 10)
        current_x = x_array[index_of_point]
        current_y = y_array[index_of_point]
        point.set_ydata([current_y])
        point.set_xdata([current_x])


amplitude_slider.on_changed(update_plot)

def callback(label):

    kasat.set_visible(not kasat.get_visible())
    kasat.figure.canvas.draw_idle()

check.on_clicked(callback)

def reset_sliders(event):
    amplitude_slider.reset()
reset_button.on_clicked(reset_sliders)


def change_color(label):
    main_line.set_color(label)
    fig.canvas.draw_idle()

def change_style(label):
    main_line.set_linestyle(label)
    fig.canvas.draw_idle()

style_buttons.on_clicked(change_style)


color_buttons.on_clicked(change_color)


plt.show()