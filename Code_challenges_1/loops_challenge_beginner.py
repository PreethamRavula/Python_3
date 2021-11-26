#Challenge-1: Divisible by 10
#Write your function here
def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 == 0:
      counter += 1

    else:
      continue
  return counter

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Challenge-2: Greetings
#Write your function here
def add_greetings(names):
  greetings = []
  i = 0
  while i < len(names):
    greetings.append("Hello, " + names[i])
    i += 1
    if i == len(names):
      break

  return greetings


#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#Challenge-3 : Delete starting even numbers
#Write your function here
def delete_starting_evens(lst):
  index = 0
  while index < len(lst) and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst


#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Challenge-4: Odd indices
#Write your function here
def odd_indices(lst):
  i = 0
  odd_index_list = []
  while i < len(lst):
    if i == len(lst):
      break
    elif i % 2 == 0:
      i += 1
    else:
      odd_index_list.append(lst[i])
      i += 1
  return odd_index_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Challenge-5: Exponents
#Write your function here
def exponents(bases, powers):
  raised_list = []
  for num in bases:
    for power in powers:
      raised_list.append(num**power)
  return raised_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
