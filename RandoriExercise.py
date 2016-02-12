# Use the classes below for this exercise

# The vending machine takes Quarters(Q), Dollars($), Nickles(N) and Dimes(D).
# The vending machine lets the user pick an Apple(.65), Orange(.75) or Banana(1.00)
# Write a test to fake the response from Cash.calculate
# Write a test to fake the response from Purchase.price
# Write a test that mocks the constructor of Cash, replaceing Cash with a Mock
# Write a test that mocks the constructor of Purchase, replacing Purchase with a Mock
# Write a test that detects the arguments of Cash.calculate
# Write a test that detects the arguments of Purchase.price
# Write a test that validates money in vs price in Vending_Machine.validate
# Vending_Machine.validate returns true or false
# Write a test that detects the arguments of Cash.calculate
# Write a test that fakes the response of Cash.calculate for any call
# Write a test that fakes the response of Cash.calculate for a specific call (say 1 + 1 = 2)
# Write a test that fakes the response of Cash.calculate to throw an exception


class VendingMachine(object):
  def __init__(self):
    self.cash = Cash()
    self.purchase = Purchase()
		
  def get_calculate(self):
    return self.cash.calculate()

  def get_price(self):
    return self.purchase.price()

  def coin_drop(self, coin):
      return True

class Cash(object):
   
   def calculate(self):
     pass
   
class Purchase(object):
  
    def price(self):
      pass
    
