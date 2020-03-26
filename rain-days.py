# Schedule Library imported

import requests
import schedule 
import time 

## representacion de la hora
print "Hora " + time.strftime("%X")

response = requests.get('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/devices') 
print response.content

def rainactive(): 
    requests.put('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/update/5e5574e9421a35568fe20658/0')
    print("Rain Active")

def raininactive(): 
    requests.put('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/update/5e5574e9421a35568fe20658/1')
    print("Rain Inactive")


#Martes
schedule.every().tuesday.at("22:00").do(rainactive)
schedule.every().tuesday.at("22:02").do(raininactive) 

#Jueves
schedule.every().thursday.at("22:00").do(rainactive)
schedule.every().thursday.at("22:02").do(raininactive)

#Sabado
schedule.every().saturday.at("22:00").do(rainactive)
schedule.every().saturday.at("22:02").do(raininactive) 

while True: 

    # Checks whether a scheduled task 
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1) 
