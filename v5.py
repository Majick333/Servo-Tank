#v5 servoTank control interface

import curses
from gpiozero import Motor
from gpiozero import AngularServo
from gpiozero import LED

led1 = LED(21, active_high=True, initial_value=False)
led2 = LED(20, active_high=True, initial_value=False)
motor1 = Motor(5,6)
motor2= Motor(19, 26)
pan = AngularServo(23, min_angle=-90, max_angle=90)
tilt = AngularServo(25, min_angle=-90, max_angle=90)

#Set screen, turn off echo of keyboard
# Set key response to instant, use special vals for cursor keys

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)



try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            motor1.forward()
            motor2.forward()
            print('DRIVE')
        elif char == curses.KEY_DOWN:
            motor1.backward()
            motor2.backward()
            print('REVERSE')
        elif char == curses.KEY_RIGHT:
            motor1.backward()
            motor2.forward()
            print('RIGHT')
        elif char == curses.KEY_LEFT:
            motor1.forward()
            motor2.backward()
            print('RIGHT')
        elif char == ord('w'):
            tilt.min()
        elif char == ord('s'):
            tilt.max()
        elif char == ord('a'):
            pan.min()
        elif char == ord('d'):
            pan.max()
        elif char == ord('c'):
            pan.mid()
            tilt.mid()
            print('Centered')
        elif char == ord('m'):
            tilt.angle = 45
        elif char == ord('n'):
            tilt.angle = -45
        elif char == ord('i'):
            motor1.forward
            print('SOLO: Motor1')
        elif char == ord('o'):
            motor2.forward
            print('SOLO: Motor2')
        elif char == ord('k'):
            motor1.reverse
            print('SOLO:REVERSE Motor1')
        elif char == ord('l'):
            motor2.reverse
            print('SOLO:REVERSE Motor2')
        elif char == ord('g'):
            led1.on()
            print('WHITE LEDS ON')
        elif char == ord('h'):
            led2.on()
            print('IR LEDS ON')
        elif char == ord('x'):
            led1.off()
            led2.off()
        elif char == 10:
            pan.detach()
            tilt.detach()
            motor1.stop()
            motor2.stop()
            print('HALT')

finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()