import RPi.GPIO as GPIO
import time   

my_pin = 8
x = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(my_pin, GPIO.OUT, initial = 0)
LED_state = False


while x > 0:
    if LED_state:
        input("Light ON!")
        GPIO.output(my_pin, LED_state)
        LED_state = False
        x -= 1
    
    else:
        input("Light OFF!")
        GPIO.output(my_pin, LED_state)
        LED_state = True
        x -= 1
        
GPIO.cleanup()

