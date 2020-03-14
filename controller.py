# import curses and GPIO
import curses
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT) #trigger
GPIO.setup(18,GPIO.IN) #echo
GPIO.setup(23,GPIO.OUT) #buzzer
GPIO.setup(7,GPIO.OUT) #car1
GPIO.setup(11,GPIO.OUT) #car2
GPIO.setup(13,GPIO.OUT) #car 3
GPIO.setup(15,GPIO.OUT) #car 4
GPIO.setup(12,GPIO.IN) #ir-left
GPIO.setup(21,GPIO.IN) #ir-right
GPIO.setup(33, GPIO.OUT) #servo up$down
GPIO.setup(35, GPIO.OUT) #claw
q = GPIO.PWM(33, 50)
r = GPIO.PWM(35, 50) 
# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
'''
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
'''
i=1
q.start(9.5)
r.start(2.5)
def distance():
    
    # set Trigger to HIGH
    GPIO.output(16,True)
    #GPIO.output(GPIO_TRIGGER, True)
 
        # set Trigger after 0.01ms to LOW
    time.sleep(0.1)
    GPIO.output(16,False)
    #GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
        # save StartTime
    while  GPIO.input(18)== False:
        StartTime = time.time()
 
        # save time of arrival
    while GPIO.input(18)== True:
        StopTime = time.time()
 
        # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

try:
        while True:
            if i==1:
            
                dist = distance()
                
                if dist>13.0 and dist<=20:
                        #GPIO.output(23,True)
                        
                        GPIO.output(7,False)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,False)

                        #stop
                elif GPIO.input(12)==True and GPIO.input(21)==True:
                        GPIO.output(23,False)
                        GPIO.output(7,False)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,False)
                        i=i+1         
                        #if (dist<=13.0 and dist>=7)and i==1:
                           
                        q.ChangeDutyCycle(9.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(8.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(7.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(6.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(5.5) # turn towards 90 degree
                        time.sleep(3)
                        r.ChangeDutyCycle(12.5) # turn towards 90 degree
                        time.sleep(2)
                        q.ChangeDutyCycle(6.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(7.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(8.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(9.5) # turn towards 90 degree
                        time.sleep(1)
                        GPIO.output(7,True)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,True)
                        time.sleep(3.38)
                        GPIO.output(7,False)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,False)
                        time.sleep(5)
                        print("111")
                        pass
                        #turn right
                elif GPIO.input(12)==False and GPIO.input(21)==True:
                        GPIO.output(7,False)
                        GPIO.output(11,True)
                        GPIO.output(13,True)
                        GPIO.output(15,False)
                        GPIO.output(23,False)
                       
                        #Turn left
                elif GPIO.input(21)==False and GPIO.input(12)==True:
                        GPIO.output(7,True)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,True)
                        GPIO.output(23,False)
                       
                elif GPIO.input(21)==False and GPIO.input(12)==False:
                        #Front
                        GPIO.output(7,True)
                        GPIO.output(11,False)
                        GPIO.output(13,True)
                        GPIO.output(15,False)
                        GPIO.output(23,False)
                        if dist<7.0:
                            GPIO.output(23,False)
                            
                            GPIO.output(7,False)
                            GPIO.output(11,False)
                            GPIO.output(13,False)
                            GPIO.output(15,False)
            elif i==2:
                dist = distance()
                
                if dist>13.0 and dist<=20:
                        #GPIO.output(23,True)
                        
                        GPIO.output(7,False)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,False)

                        #stop
                elif GPIO.input(12)==True and GPIO.input(21)==True:
                        GPIO.output(23,False)
                        GPIO.output(7,False)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,False)
                        print(i)
                        q.ChangeDutyCycle(9.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(8.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(7.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(6.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(5.5) # turn towards 90 degree
                        time.sleep(3)
                        r.ChangeDutyCycle(2.5) # turn towards 90 degree
                        time.sleep(2)
                        q.ChangeDutyCycle(6.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(7.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(8.5) # turn towards 90 degree
                        time.sleep(1)
                        q.ChangeDutyCycle(9.5) # turn towards 90 degree
                        time.sleep(1)
                        GPIO.output(7,True)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,True)
                        time.sleep(3.5)
                        print("222")
                        
                        break
                        
                        #turn right
                elif GPIO.input(12)==False and GPIO.input(21)==True:
                        GPIO.output(7,False)
                        GPIO.output(11,True)
                        GPIO.output(13,True)
                        GPIO.output(15,False)
                        GPIO.output(23,False)
                       
                        #Turn left
                elif GPIO.input(21)==False and GPIO.input(12)==True:
                        GPIO.output(7,True)
                        GPIO.output(11,False)
                        GPIO.output(13,False)
                        GPIO.output(15,True)
                        GPIO.output(23,False)
                       
                elif GPIO.input(21)==False and GPIO.input(12)==False:
                        #Front
                        GPIO.output(7,True)
                        GPIO.output(11,False)
                        GPIO.output(13,True)
                        GPIO.output(15,False)
                        GPIO.output(23,False)
                        if dist<7.0:
                            GPIO.output(23,False)
                            
                            GPIO.output(7,False)
                            GPIO.output(11,False)
                            GPIO.output(13,False)
                            GPIO.output(15,False)    
    
    
         
             
finally:
    print("done")
    GPIO.cleanup()
               
