#! /bin/python

from sense_hat import SenseHat
import time, datetime
import RPi.GPIO as GPIO
import getopt, sys

hat = SenseHat()

def tweHourClock():
    global timeC
    timeC = 12

def twe4HourClock():
    global timeC
    timeC = 0

hour_color = (255, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
off = (0, 0, 0)

hat.clear()

# hat.show_message("Programmet starter")

def display_binary(value, row, color):
    binary_str = "{0:8b}".format(value)
    if direction == 'hori':
        for x in range(0, 8):
            if binary_str[x] == '1':
                hat.set_pixel(x, row, color)
            else:
                hat.set_pixel(x, row, off)
    else: 
        for x in range(0, 8):
            if binary_str[x] == '1':
                hat.set_pixel(row, x, color)
            else:
                hat.set_pixel(row, x, off)

def clockLoop():
    try:
        while True:
            t = datetime.datetime.now()
            x = t.hour+2
            if x > 12:
                x -= timeC
            if direction == 'hori':
                display_binary(x, 3, hour_color)
                display_binary(t.minute, 5, minute_color)
                display_binary(t.second, 7, second_color)

            elif direction == 'verti':
                hourI = list(map(int, str(x)))
                if len(hourI) > 1:
                    display_binary(hourI[0], 0, hour_color)
                    display_binary(hourI[1], 1, hour_color)
                else:
                    display_binary(hourI[0], 1, hour_color)

                minI = list(map(int, str(t.minute)))
                if len(minI) > 1:
                    display_binary(minI[0], 3, minute_color)
                    display_binary(minI[1], 4, minute_color)
                else:
                    display_binary(minI[0], 4, minute_color)

                secI = list(map(int, str(t.second)))
                if len(secI) > 1:
                    display_binary(secI[0], 6, second_color)
                    display_binary(secI[1], 7, second_color)
                else:
                    display_binary(secI[0], 7, second_color)

            time.sleep(0.0001)
    except KeyboardInterrupt:
        hat.show_message("Programmet slutter")
        GPIO.cleanup()   

def UnD():
    hat.clear()
    global direction
    direction = 'verti'

def LnR():
    hat.clear()
    global direction
    direction = 'hori'

def pre(event):
    if event[2] == 'released':
        if timeC == 12:
            twe4HourClock()
        else:
            tweHourClock()
    
hat.stick.direction_up = UnD
hat.stick.direction_down = UnD
hat.stick.direction_left = LnR
hat.stick.direction_right = LnR
hat.stick.direction_middle = pre

def main(argv):
    global direction
    print(argv)
    if argv == []:
        direction = 'hori'
        twe4HourClock()
        clockLoop()

    else:
        opts, args = getopt.getopt(argv,"tmhv")
        # checking each argument
        for opt, arg in opts:
            print(opt)
            if opt in '-t':
                tweHourClock()
                
            if opt in "-m":
                twe4HourClock()

            if opt in "-h":
                direction = 'hori'

            if opt in "-v":
                direction = 'verti'

        clockLoop()
    
if __name__ == '__main__':
    main(sys.argv[1:])