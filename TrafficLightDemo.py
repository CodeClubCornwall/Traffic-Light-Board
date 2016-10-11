from gpiozero import LED
from time import sleep

north_green = LED(7)
north_amber = LED(8)
north_red = LED(25)

west_green = LED(22)
west_amber = LED(27)
west_red = LED(17)

def north_off():
    north_green.off()
    north_amber.off()
    north_red.off()

def west_off():
    west_green.off()
    west_amber.off()
    west_red.off()

def north_red_only():
    north_off()
    north_red.on()

def north_red_amber():
    north_off()
    north_red.on()
    north_amber.on()

def north_green_only():
    north_off()
    north_green.on()

def north_amber_only():
    north_off()
    north_amber.on()

def west_red_only():
    west_off()
    west_red.on()

def west_red_amber():
    west_off()
    west_red.on()
    west_amber.on()

def west_green_only():
    west_off()
    west_green.on()

def west_amber_only():
    west_off()
    west_amber.on()

while True:
    north_off()
    west_off()
    north_red_only()
    west_green_only()
    sleep(3)
    west_amber_only()
    sleep(1)
    west_red_only()
    north_red_amber()
    sleep(1)
    north_green_only()
    sleep(3)
    north_amber_only()
    sleep(1)
    west_red_amber()
    sleep(1)
