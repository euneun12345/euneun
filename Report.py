import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

led = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

client = mqtt.Client()
client.connect("172.16.14.7", 1883, 60)
client.loop_start()
client.subscribe("led")

def on_message(client, userdata, message):
   if str(message.payload.decode("utf-8")) == "1":
       GPIO.output(led, 1)

   else:
       GPIO.output(led, 0)

while True:
   client.on_message = on_message

GPIO.cleanup()
