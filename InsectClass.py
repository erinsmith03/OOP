
import random
class Insect:

    def __init__(self,n,w,l):
        self.name=n
        self.wings=w #to create an object, you'll need to specify these measures
        self.legs=l
        self.flight=0 


    def fly_length(self): #need a function to calculate flight length
        self.flight=random.randint(1,10) #the flight attribute will reset the value to a random one 1-10

    def get_name(self):
        return self.name

    def get_miles(self): 
        return self.flight
    #this returns the attribute to self.flight

    