#importing Datetime Module:
from datetime import time

# Defining the Class:
class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{menu} menu available from {start} to {end}".format(menu = self.name, start = self.start_time, end = self.end_time)

  def calculate_bill(self, purchased_items):
    calculate_bill = 0
    for item in purchased_items:
      calculate_bill += self.items[item]
    return calculate_bill

# Creating a Franchise Class:
class Franchise:

  def __init__(self, address, menus = []):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= getattr(menu, "start_time", "none") and time <= getattr(menu, "end_time", "none"):
        available_menus.append(menu)
    print("\nAvailable menus at the store {} at present time {} are: ".format(self. __repr__(), time))
    for food in available_menus:
      print("\n", food)

    return available_menus

# Creating a Business Class:
class Business:

  def __init__(self, name, franchises = []):
    self.name = name
    self.franchises = franchises

# Brunch Menu:
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_start = time(11)
brunch_end = time(16)
menu_brunch = Menu("Brunch", brunch_items, brunch_start, brunch_end)

# Early bird Menu:
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird_start = time(15)
early_bird_end = time(18)
menu_early_bird = Menu("Early bird", early_bird_items, early_bird_start, early_bird_end)

# Dinner Menu:
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner_start = time(17)
dinner_end = time(23)
menu_dinner = Menu("Dinner", dinner_items, dinner_start, dinner_end)

#Kids Menu:
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids_start = time(11)
kids_end = time(21)
menu_kids = Menu("Kids", kids_items, kids_start, kids_end)

#Arepas Menu:
arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_start = time(10)
arepas_end = time(20)
menu_arepas = Menu("Arepas", arepas_items, arepas_start, arepas_end)

print(menu_brunch)
print(menu_arepas)

# Testing calculate bill function:
brunch_order = ['pancakes', 'home fries', 'coffee']
brunch_bill = menu_brunch.calculate_bill(brunch_order)
print("Brunch bill to be paid: ",brunch_bill)

early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
early_bird_bill = menu_early_bird.calculate_bill(early_bird_order)
print("Early bird meal bill to be paid: ", early_bird_bill)

Franchise_menus = [menu_early_bird, menu_brunch, menu_kids, menu_dinner]
Arepas_menus = [menu_arepas]
#Franchises:
flagship_store = Franchise("1232 West End Road", Franchise_menus)
new_installment = Franchise("12 East Mulberry Street", Franchise_menus)
arepas_place = Franchise("189 Fitzgerald Avenue", Arepas_menus)

print(flagship_store)

flagship_store.available_menus(time(12))
new_installment.available_menus(time(17))

#Businesses:
stores = [flagship_store, new_installment]
basta = Business("Basta Fazoolin' with my Heart", stores )
arepa = Business("Take a' Arepa", [arepas_place])
