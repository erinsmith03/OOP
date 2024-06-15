import CoinClass as c #program where we actually create those objects and instances of them
 #coinclass is the FILE name, so when u import it u are importing all the code in it
 


# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

#when we say 'c', it is saying go to this file, and look for the class name "Coin"
#so when we run it, it runs the initilization of that object
#my_coin is the actual object or instance of the coin object from this coin class we are creating

#going forward, we need to use my_coin bc that is the object/instance created 

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter
#we have to call the method that would display the value
#so my_coin.get_sideup looks for a method called get_sideup and executes any code thats in there
#so it returns the value of 'heads' bc we initialized it as heads


       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

#everytime it repeats, we execute toss method 10 times
#bc of the self paramter, it knows to keep it separate with separate instances

           

#theres nothing in this code that prevents us from changing attribute or calling heads/tails directly

       

# Call the main function.

main()
