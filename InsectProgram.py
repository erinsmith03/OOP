import InsectClass as c

def main():
    mosquito=c.Insect('mosquito',2,4) #you'll need to put in the wing and leg values here
    housefly=c.Insect('housefly',2,4)



    mosquito.fly_length()
    housefly.fly_length()

    print(f'the {mosquito.get_name()} can fly up to {mosquito.get_miles()} miles')
    print(f'the {housefly.get_name()} can fly up to {housefly.get_miles()} miles')



main()
