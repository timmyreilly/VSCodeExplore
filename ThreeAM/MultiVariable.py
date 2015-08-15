import time
import threading

'''
I'm trying to figure out some way to represent two seperate lights to blink...
If they blink at the same time we should get red. 
They should create some sort of multivariable phenomenon. 

I'm not really sure how to do this...

Blink wait Blink Wait Blink Wait
blink waitt blink waitt blink waitt

When you have two cars turn signals on and you get the oscialating effect. Syncapation, then I want to play a song. 

But we can't really do it discretely.

So Threading... 

'''

class Blinker(threading.Thread):
	def __init__(interval, color):
		print 'Initializing'
		super(Blinker, self).__init__()
		self.interval = interval
		self.color = color 
		
	def run(self):
		print 'running'
		while True:
			time.sleep(self.interval)
			return 
			

def blinkOne():
	return 'blue'
	
def blinkTwo():
	

if __name__ == '__main__':
	while True:
		print 'uhh'
	print 'yeppers'
	print blinkOne()