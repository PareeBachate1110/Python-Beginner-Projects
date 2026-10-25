#Experiment 12: Timer Program

import time

alarm=int(input("Enter Time in Seconds: "))

def timer():
    for x in range(1,alarm+1):
        seconds = x % 60
        minutes = int(x/60) % 60
        hours = int(x/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("TIME'S UP!")    

def countdown():
    for x in reversed(range(1,alarm+1)):
        seconds = x % 60
        minutes = int(x/60) % 60
        hours = int(x/3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("TIME'S UP!")

n=int(input("Enter Number: 1.Timer 2.Countdown: \n"))
if(n==1):
    timer()
elif(n==2):
    countdown()
else:
    print("Please Enter Either 1 or 2.")
