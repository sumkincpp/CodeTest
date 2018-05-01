import RPi.GPIO as GPIO
import time
import sys

def print_state(state):
        state_str = "MOVEMENT" if state == 1 else "SILENCE"
        print "%s|%s|%s" % (time.time(), time.strftime("%Y-%m-%d %H:%M:%S"), state_str)
        sys.stdout.flush()

#motion_pin = int(sys.argv[1])

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

pin = 7

GPIO.setup(pin, GPIO.IN)         #Read output from PIR motion sensor

previous = GPIO.input(pin)

print_state(previous)

#GPIO.setup(3, GPIO.OUT)         #LED output pin

while True:
        current = GPIO.input(pin)
        if current != previous:
                previous = current
                print_state(current)
        time.sleep(0.1)
