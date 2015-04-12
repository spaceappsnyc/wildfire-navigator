############################################################
# Program to monitor light sensor reading
# verify that readings are above 900 for 3 consecutive times
# Send an alert that High temperature is detected
__author__ = 'Kishore Kudipudi'
############################################################
import mraa
import time
import os
from collections import deque

######################################################
# Function to read light server data with AIO argument
# Returns the value of the reading
######################################################
def monitor_light(lightSense_Aio):
    lightSense = mraa.Aio(lightSense_Aio)
    reading=lightSense.read()
    return reading

# Sample is created using deque data structure in order to be able to remove reading from beginning of the queue.
sample = deque()


#Infinite loop with sleep time in between.
while True:
    sample.append(monitor_light(0))
    if len(sample)>3:
        sample.popleft()
    alert=True
    for n in sample:
        if n < 900:
            alert=False
    if alert:
        x=os.system('curl http://192.168.0.112:5000/msg1 -d "data=alert" -X PUT')
        #print "High temperature detected!!!!!"
    else:
        x=os.system('curl http://192.168.0.112:5000/msg1 -d "data=norm" -X PUT')
    time.sleep(0.5)
