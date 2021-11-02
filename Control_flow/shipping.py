# program for deciding the cheapest shipping method.

weight = 41.5
flat_charge = 0.0
weight_cost = 0.0
shipping_cost = 0.0
shipping_cost_premium = 125.0
shipping_cost_drone = 0.0
# Ground Shipping: weight in pounds
if weight <= 2:
  flat_charge = 20.0
  weight_cost = 1.50
  shipping_cost = flat_charge + (weight*weight_cost)
  print("The cost of Ground Shipping is $",shipping_cost)

elif 2 < weight <= 6:
  flat_charge = 20.0
  weight_cost = 3.0
  shipping_cost = flat_charge + (weight*weight_cost)
  print("The  cost of Ground Shipping is $",shipping_cost)

elif 6 < weight <= 10:
  flat_charge = 20.0
  weight_cost = 4.0
  shipping_cost = flat_charge + (weight*weight_cost)
  print("The cost of Ground Shipping is $",shipping_cost)

elif weight > 10:
  flat_charge = 20.0
  weight_cost = 4.75
  shipping_cost = flat_charge + (weight*weight_cost)
  print("The cost of Ground Shipping is $",shipping_cost)

print("The cost of Premium Ground shipping for any weight category is $", shipping_cost_premium)

#Drone Shipping: Weight in Pounds

if weight <= 2:
  flat_charge = 0.0
  weight_cost = 4.5
  shipping_cost_drone = flat_charge + (weight*weight_cost)
  print("The cost of Drone shipping is $", shipping_cost_drone )

elif 2 < weight <= 6:
  flat_charge = 0.0
  weight_cost = 9.0
  shipping_cost_drone = flat_charge + (weight*weight_cost)
  print("The cost of Drone shipping is $", shipping_cost_drone)

elif 6 < weight <= 10:
  flat_charge = 0.0
  weight_cost = 12.0
  shipping_cost_drone = flat_charge + (weight*weight_cost)
  print("The cost of Drone shipping is $", shipping_cost_drone)

elif weight > 10:
  flat_charge = 0.0
  weight_cost = 14.25
  shipping_cost_drone = flat_charge + (weight*weight_cost)
  print("The cost of Drone shipping is $", shipping_cost_drone)

if shipping_cost < shipping_cost_drone and shipping_cost < shipping_cost_premium:
  print("The cheapest way of shipping is by ground and it cost's $", shipping_cost )

elif shipping_cost_drone < shipping_cost and shipping_cost_drone < shipping_cost_premium:
  print("he cheapest way of shipping is by drone and it cost's $", shipping_cost_drone)

elif shipping_cost_premium < shipping_cost and shipping_cost_premium < shipping_cost_drone:
  print("he cheapest way of shipping is by premium ground and it cost's $", shipping_cost_premium)
