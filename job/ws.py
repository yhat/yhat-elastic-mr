from threading import Thread, Condition
import random
import time
import sys

condition = Condition()
queue = []

class ProducerThread(Thread):
    def run(self):
        global queue
        for line in sys.stdin:
            condition.acquire()
            queue.append(line)
            condition.notify()
            condition.release()
        sys.exit(0)

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print "Nothing in queue, consumer is waiting"
                condition.wait()
                print "Producer added something to queue and notified the consumer"
            item = queue.pop(0)
            condition.release()


ProducerThread().start()
ConsumerThread().start()
