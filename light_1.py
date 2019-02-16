# Write your code here :-)
from microbit import *
while True:
    reading = pin2.read_analog()
if (reading > 300):
    display.show(Image.SAD)
else:
    display.off()