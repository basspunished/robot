# import curses, GPIO, os, and time
import curses
import RPi.GPIO as GPIO
import time
import os
from subprocess import call
#set GPIO pins as output using the GPIO.BOARD layout. 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

# allows keyboard buttons to be used to control the robot. Echo is turned off from the terminal.
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_DOWN:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == curses.KEY_UP:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == ord('d'): #Robot will shake its tail feather
                GPIO.output(11,True)
                GPIO.output(15,True)
                time.sleep(.5)
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
                time.sleep(.5)
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
                time.sleep(.5)
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
                time.sleep(.5)
                GPIO.output(11,False)
                GPIO.output(13,False)
            elif char == 10: #stops robot movement
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
            elif char == ord('t'):
                curses.nocbreak(); screen.keypad(0); curses.echo()
                curses.endwin()
                speak = (input("What should i say: "))
                os.system("espeak '"+speak+"' -s 110")
                screen = curses.initscr()
                curses.noecho()
                curses.cbreak()
                screen.keypad(True)
            elif char == ord('h'):
                speak = str("()if he dies he dies")
                os.system("espeak '"+speak+"' -s 110")
            elif char == ord('S'): # use 'S' to shutdown the robot without a monitor or in a headless OS
                os.system("sudo shutdown -h 0")
                
#the code below can be commented out after initial set up and testing if desired.              
finally:
    #quit the program with q
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
