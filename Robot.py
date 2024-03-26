# Main logic of the PyBot
from lib.mBot import mBot
import time

def on_line_follower(value):
    print("status = ", value)


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
        time.sleep(0.25)
    # ROBOT STARTED
    # Loop
    # If lightSensor == 1
    
    # if lightSensor == 2
    
    # if lightSensor == 3
