import random #instructions on how to create the object

# The Coin class simulates a coin that can
# be flipped.

class Coin: #uppercase for class name always
    # The _ _init_ _ method initializes the object
    # sideup data attribute with 'Heads'.

    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self): #this simulates the tossing of the coin
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads' 
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self): #returning the value of ur attribute
            return self.sideup
#for objects, you have either an ACCESSOR METHOD or MUTATOR METHOD
#Accessor: gives u access to an attribute
#mutator: changes the value of an attribute 



#bc we are using self paramter, we use .sideup bc we are defining that atrribute
# the init is always the FIRST method in class definition file, bc it is where we list out ALL attributes
#its the first thing thats run
