# Main logic of the PyBot
from lib.mBot import mBot
import time

def lost_path():
    print("Robot has lost the path. Attempting to find path...")

"""
Main movement algorithm

"""  
def on_line_follower(value):
    print("status = ", value)
    if(value == 3): 
        bot.doMove(100, 100)
    elif(value == 2):
        bot.doMove(0, 100)
    elif(value == 1):
        bot.doMove(100, 0)
    else:
        bot.doMove(-100, -100)
    
def on_light(value):
    print("Light = ", value)




    """
    Main procedure for the Argonne National Library robot
    
    Robot should go forward while lineFollower gets
    """
if __name__ == '__main__':
    bot = mBot()
    bot.startWithSerial("COM15") or bot.startWithHID()  # replace COM15 with actual port
    running = True
    
    while(running):
        bot.requestLineFollower(1, 2, on_line_follower)
    # ROBOT STARTED
    # Loop
    # if lightSensor == 0
        
    # If lightSensor == 1
    
    # if lightSensor == 2
    
    # if lightSensor == 3



# LIGHT SENSOR EXAMPLE
# def onLight(value):
# 	print "light = ",value
	
# if __name__ == '__main__':
# 	bot = mBot()
# 	#bot.startWithSerial("COM15")
# 	bot.startWithHID()
# 	while(1):
# 		bot.requestLightOnBoard(1,onLight)
# 		sleep(0.5)

# LINE FOLLOWER EXAMPLE
# def onLineFollower(value):
# 	print "status = ",value
	
# if __name__ == '__main__':
# 	bot = mBot()
# 	#bot.startWithSerial("COM15")
# 	bot.startWithHID()
# 	while(1):
# 		bot.requestLineFollower(1,2,onLineFollower)
# 		sleep(0.5)

# MOTOR CONTROLLER EXAMPLE
# bot = mBot()
# #bot.startWithSerial("/dev/ttyUSB0")
# bot.startWithHID()
# while(1):
# 	try:	
# 		bot.doMove(100,100)
# 		print "run forward"
# 		sleep(2)
# 		bot.doMove(-100,-100)
# 		print "run backward"
# 		sleep(2)
# 		bot.doMove(0,0)
# 		print "stop"
# 		sleep(2)
# 	except Exception,ex:
# 		print str(ex)