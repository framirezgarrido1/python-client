import requests
import schedule 
import time


response = requests.get('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/devices') 
print response.content


def rainactive(): 
	response = requests.put('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/update/5e5574b3421a35568fe20657/0')
	if response.status_code == 200:
    	print('Rain Active')

def raininactive(): 
	response = requests.put('http://ec2-3-17-162-210.us-east-2.compute.amazonaws.com:3002/api/update/5e5574b3421a35568fe20657/1')
	if response.status_code == 200:
    	print('Rain Inactive')


#Martes
schedule.every().tuesday.at("22:10").do(rainactive)
schedule.every().tuesday.at("22:12").do(raininactive) 

#Jueves
schedule.every().thursday.at("22:10").do(rainactive)
schedule.every().thursday.at("22:12").do(raininactive)

#Sábado
schedule.every().saturday.at("22:10").do(rainactive)
schedule.every().saturday.at("22:12").do(raininactive) 