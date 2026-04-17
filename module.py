# In main file
# import script1
# print(script1.sum(1, 3))

# You will need to add code in this module to make teh Point of Sale Application functional.


from tkinter import Menu
from unicodedata import name

from prompt_toolkit import choice


class PointOfSale:
  def __init__(self):
    self.checkout_total = 0 # This is an example varialbe, remove it or change it as you please.
    self.cart = {}
    print("\nInitializing POS system...")

    
    
  def start(self): # This is the function that should be used to start the application.
    print("welcome to Cristian's POS.")
    while (True):
      self.showmenu()
      choice = input("\nEnter your choice 1-5: ")
      if choice == '1':
        self.add_item()
      elif choice == '2':
        self.remove_item()
      elif choice == '3':
        self.view_cart()
      elif choice == '4':
        self.checkout()
      elif choice == '5':
        print("Exiting the application. Goodbye!")
        break
      else:
        print("Invalid choice. Please enter a number between 1 and 5.")
  def showmenu(self):
     print("\n Menu:")
     print("\n--------------")
     print("1. Add item to cart")
     print("2. Remove item from cart")
     print("3. View cart")
     print("4. Checkout")
     print("5. Exit") 

  def add_item(self):
    try:
      name = input("Enter item name: ")
      price = float(input("Enter item price: "))
      self.cart[name] = price
      print(f"{name} added to cart.")
    except ValueError:
      print("Invalid price.")

  def remove_item(self):
    name = input("Enter item name to remove: ")
    if name in self.cart:
      del self.cart[name]
      print(f"{name} removed from cart.")
    else:
      print("Item not found in cart.")

  def view_cart(self):
    if not self.cart:
      print("Cart is empty.")
      return

    print("\nItems in cart:")
    total = 0
    for item, price in self.cart.items():
      print(f"{item}: ${price:.2f}")
      total += price

    print(f"Total so far: ${total:.2f}")

  def checkout(self):
    if not self.cart:
      print("Cart is empty.")
      return

    total = sum(self.cart.values())
    print(f"\nTotal amount: ${total:.2f}")
    print("Thank you for your purchase!")

    self.cart.clear()
     
     
      

        
      

    
    
    
    