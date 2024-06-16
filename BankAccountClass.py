# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal): #balance is the only attribute
        self.balance = bal #value is set based on whatever user puts for the instance 


      # The deposit method makes a deposit into the
      # account.

    def deposit(self, amount):
        self.balance += amount
#this is a MUTATOR method because we are changing the value of an attribute
#when the user calls this method, they have to put in some value

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance-=amount
        else:
            print("Insufficient funds")
    

      # The get_balance method returns the
      # account balance.

    def get_balance(self):
        return self.balance
#this just returns the value of the attribute, 
#this method is ACCESSOR method, also known as a GET method

    def __str__(self):
        return 'The balance is $' + format(self.balance, ',.2f')
#when you have string, this helps format the object