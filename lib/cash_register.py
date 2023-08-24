#!/usr/bin/env python3

# We're going to create an Object-Oriented Cash Register that can:

# Add items of varying quantities and prices
# Calculate discounts
# Keep track of what's been added to it
# Void the last transaction

from typing import Any


class CashRegister:

  def __init__(self,discount=0):
    self._discount=discount
    self.total=0
    self.items=[]

  def get_discount(self):
    return self._discount
  def set_discount(self,discount):
    if discount is int or float:
      self._discount=discount
    else:
      self._discount=0
  discount=property(get_discount,set_discount,)       

  
  def add_item(self,title,price,quantity=1):
    self.title=title
    self.price=price
    self.quantity=quantity
    for i in range(quantity):
        self.items.append(title)
    self.total += price *quantity
    return self.total
  
  def apply_discount(self):
    if self._discount:
      self.total= int(self.total - (self.total*self._discount/100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.") 

  def void_last_transaction(self):
    if self.items:
      last_item=self.total - self.get_item_price(self.items.pop())
      self.total=last_item

  def get_item_price(self,title):
    return self.price         


cash=CashRegister()
cash.add_item("egg",4.5)
cash.add_item("bread",5.0)
cash.add_item("milk",2.50,2)

print(cash.total)

dis=CashRegister(20)
dis.add_item("macbook",1000)
dis.apply_discount()

no_dis=CashRegister()
no_dis.add_item("book",100)
no_dis.apply_discount()

last=CashRegister()
last.add_item("apple",5)
last.add_item("tomato",10,2)
last.add_item("bread",5.0)
last.void_last_transaction()
print(last.total)
