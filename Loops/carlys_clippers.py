# Carly Clippers Hairstyles mangament program

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
total_price_2 = 0
index = 0
length = len(prices)

for price in prices:
  total_price += price
print("Sum of the prices of all haircuts is", total_price)
average_price = total_price / length
print("Average price of a haircut is", average_price)
new_prices = [price - 5 for price in prices]
print("The new prices list is", new_prices)
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total amount made in last week is", total_revenue)
average_daily_revenue = total_revenue/7
print("Average revenue made in a day is", average_daily_revenue)
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
