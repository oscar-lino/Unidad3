#Proxy.py
import time

class Producer:
    """"Defines the 'resouerce-intensive' object to instantiate"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:
    """Define teh 'relatively less resource-intensive' proxyton instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if producer is available...")

        if self.occupied == 'No':
            #if the roducer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            #make the producer meet the guest!
            self.producer.meet()

        else:
            #Otherwise, don´t instantiate a producer
            time.sleep(2)
            print("Producer is busy!")

#Instantiate a proxy
p = Proxy()

#make the proxy: Artist produce until producer is available
p.produce()

#Change the state to´ocuped´
p.occupied = 'Yes'

#Lake the producer produce
p.produce()
