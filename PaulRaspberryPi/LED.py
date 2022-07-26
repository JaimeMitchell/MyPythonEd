
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
ON=True
OFF=False
cont='Y'
while cont=='Y':
        x=int(input('Please enter your number: '))
        if x>0:
                for i in range(x):
                        GPIO.output(11,ON)
                        time.sleep(.5)
                        GPIO.output(11,OFF)
                        time.sleep(.5)
                cont=input('Continue: (Y for Yes):  ')
GPIO.cleanup()


