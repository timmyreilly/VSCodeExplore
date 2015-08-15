import time

def foo(color, result, index):
    print 'hello {0}'.format(color)
    result[index] = time.time()

def blink(color, hue, time, index, wait):
	time[index] = time.time()
	color[index] = hue 
	

from threading import Thread

threads = [None] * 2
results = [None] * 2

print threads

for i in range(len(threads)):
    threads[i] = Thread(target=foo, args=("blue", results, i))
    threads[i].start()

# do some other stuff

colors = [None] * 2
hues = [None] * 2



for j in range(len(threads))

for i in range(len(threads)):
    threads[i].join()

print results

#print " ".join(results)  # what sound does a metasyntactic locomotive make?
