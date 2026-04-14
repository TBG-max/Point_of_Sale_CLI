# You will need to add code in this module to make teh Point of Sale Application functional.
from os import system

class PointOfSale:
  def __init__(self):
    self.cart = []
    self.prices = []
    system("clear")
    print("Initializing POS system...")
    
    
  def start(self): # This is the function that should be used to start the application.
    print("\nWelcome to Smith LLC POS System...")
    while(True):
      self.showMenu()
      choice = input("Please select an option 1-5: ")
      system("clear")
      if choice == "1":
        self.showCart()
      elif choice == "2":
        self.addItem()
      elif choice == "3":
        print("Total:", self.getTotal())
      elif choice == "4":
        self.checkout()
      elif choice == "5":
        print("Exiting program...")
        break
      else:
        print("Unrecognized instruction.... Try again...")
    pass 
  
  
  def showMenu(self):
    print("\n-------------------------")
    print("\nMENU: Choose one...")
    print("1: Show Cart")
    print("2: Add Item to Cart")
    print("3: Show Checkout Total")
    print("4: Checkout")
    print("5: Exit")
    
  def showCart(self):
    print("In your cart...")
    if len(self.cart) == 0:
      print("Nothing in your cart...")
    index = 0
    while index < len(self.cart):
      print(f"{self.cart[index]}: {self.prices[index]}")
      index += 1
  
  def addItem(self):
    print("Adding item to cart...")
    item = input("What is the item? ")
    price = float(input("What is the price? (No $ sign) "))
    
    self.cart.append(item)
    self.prices.append(price)
    
  def getTotal(self):
    print("Getting cart total...")
    total = 0
    for price in self.prices:
      total += price
    return total

  def checkout(self):
    print("Checking out...")
    print(f"You paid ${self.getTotal()}")
    print("Your cart is now empty.")
    self.cart = []
    self.prices = []