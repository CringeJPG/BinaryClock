from sense_hat import SenseHat
import time, datetime

hat = SenseHat()

hour_color = (255, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
off = (0, 0, 0)

hat.clear()
# hat.show_message("Programmet starter")

def display_binary_horizontal(value, row, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)

def display_binary_vertical(value, column, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(column, x, color)
        else:
            hat.set_pixel(column, x, off)

def horiClock():
    while True:
        t = datetime.datetime.now()
        x = t.hour
        if x > 12:
            x -= timeC
        display_binary_horizontal(x, 3, hour_color)
        display_binary_horizontal(t.minute, 5, minute_color)
        display_binary_horizontal(t.second, 7, second_color)

        time.sleep(0.0001)

def vertClock():
    while True:
        t = datetime.datetime.now()
        x = t.hour
        if x > 12:
            x -= timeC
        hourI = list(map(int, str(x)))
        if len(hourI) > 1:
            display_binary_vertical(hourI[0], 0, hour_color)
            display_binary_vertical(hourI[1], 1, hour_color)
        else:
            display_binary_vertical(hourI[0], 1, hour_color)

        minI = list(map(int, str(t.minute)))
        if len(minI) > 1:
            display_binary_vertical(minI[0], 3, minute_color)
            display_binary_vertical(minI[1], 4, minute_color)
        else:
            display_binary_vertical(minI[0], 4, minute_color)

        secI = list(map(int, str(t.second)))
        if len(secI) > 1:
            display_binary_vertical(secI[0], 6, second_color)
            display_binary_vertical(secI[1], 7, second_color)
        else:
            display_binary_vertical(secI[0], 7, second_color)

        time.sleep(0.0001)

def tweHourClock():
    global timeC
    timeC = 12

def twe4HourClock():
    global timeC
    timeC = 0

tweHourClock()
vertClock()