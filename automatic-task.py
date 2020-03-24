# Schedule Library imported

import requests
import schedule 
import time 


response = requests.get('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/devices') 
print response.content


# Functions setup 
def sudo_placement(): 
	print("Get ready for Sudo Placement at Geeksforgeeks") 

def good_luck(): 
	print("Good Luck for Test") 

def work(): 
	print("Study and work hard") 

def ledon(): 
	print("It is bed time go rest")
	responseled = requests.put('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/update/5e5574b3421a35568fe20657/1')
	print responseled

def ledoff(): 
	print("It is bed time go rest")
	responseled = requests.put('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/update/5e5574b3421a35568fe20657/0')
	print responseled
	
def geeks(): 
	print("Shaurya says Geeksforgeeks")
	responsegit = requests.get('https://api.github.com')
	print responsegit


# Task scheduling 
# After every 10mins geeks() is called. 
schedule.every(1).minutes.do(geeks) 

# After every hour geeks() is called. 
schedule.every().hour.do(geeks) 

# Every day at 12am or 00:00 time bedtime() is called. 
schedule.every().day.at("13:39").do(ledon) 

# Every day at 12am or 00:00 time bedtime() is called. 
schedule.every().day.at("13:40").do(ledoff) 

# After every 5 to 10mins in between run work() 
schedule.every(5).to(10).minutes.do(work) 

# Every monday good_luck() is called 
schedule.every().monday.do(good_luck) 

# Every tuesday at 18:00 sudo_placement() is called 
schedule.every().tuesday.at("18:00").do(sudo_placement) 

# Loop so that the scheduling task 
# keeps on running all time. 
while True: 

	# Checks whether a scheduled task 
	# is pending to run or not 
	schedule.run_pending() 
	time.sleep(1) 

