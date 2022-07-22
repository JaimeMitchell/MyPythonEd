from threading import Thread
from time import *


def myBox(delayT, color):
    while True:
        print('OPEN.........')
        sleep(delayT)
        print('CLOSED........')
        sleep(delayT)


def myLED(delayT):  # delayT is a parameter being called below by args=(delayLED )
    while True:
        print('ON.........')
        sleep(delayT)
        print('OFF..........')
        sleep(delayT)


# Time arguments
delayBox = 5
delayLED = 1
# Setup. If i use arguments 'args' and only pass one argument i need a trailing comma. but not if i have two arguments.
boxThread = Thread(target=myBox, args=(delayBox, 'blue'))
LEDThread = Thread(target=myLED, args=(delayLED,))
# this kills the program so it doesn't run in the background. dismount?
boxThread.daemon = True
LEDThread.daemon = True
# this invokes the threads
boxThread.start()
LEDThread.start()
# an infinite loop makes sure the program doesn't stop after the first run and then dismount from the deamon.
j = 0
while True:
    print(j)
    j = j+1
    sleep(.1)
