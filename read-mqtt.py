import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("devices/esp8266/#")

def on_message(client, userdata, msg):

	message = msg.payload.decode()
	print("")
	x = message.split("-")
	print("id | "+ x[0] + " - state | " + x[1])

	state = x[1]
	gpio = x[0]
	
	if state == "0":
		print(gpio + " OFF")
		response = "Update GPIO " + gpio
		client.publish("devices/response/", response)
		#LED(gpio).off

	if state == "1":
		print(gpio + " ON")
		client.publish("devices/response/", response)
		#LED(gpio).on

   	#client.disconnect()

client = mqtt.Client()
client.connect("broker.hivemq.com",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
