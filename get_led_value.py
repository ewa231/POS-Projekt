from machine import Pin
from time import sleep

led = Pin(28, Pin.OUT)

led.off()
led.on()
sleep(2)

f = open(r"C:\Users\ewa_1\PycharmProjects\GUI\led_value.txt", "w")
f.write(str(led.value()))
f.close()
led.off()