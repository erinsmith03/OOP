import CellPhoneClass as c

def main():

    #get phone data
    man=input('Enter the manucturer:')
    mod=input('Enter the model number:')
    retail=float(input('Enter the retail price:'))

    #create an instance of cellphone class
    phone=c.Manufacturer(man,mod,retail)

    phone.set_retail_price(1500)
    #display the data that was entered
    print('Here is the data you entered:')
    print('Manufacturer:',phone.get_manufact())
    print('Model Number:',phone.get_model())
    print('Retail Price:$',phone.get_price())

    #call main function
main()