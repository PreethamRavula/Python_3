#Challenge-1: Sum Values
# Write your sum_values function here:
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

#Challenge-2: Even Keys
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  sum_keys = 0
  for key,value in my_dictionary.items():
    if key % 2 == 0:
      sum_keys += value
  return sum_keys
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#Challenge-3: Add Ten
# Write your add_ten function here:
def add_ten(my_dictionary):
  value = 0
  for key in my_dictionary.keys():
    value = my_dictionary[key] + 10
    my_dictionary[key] = value
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

#Challenge-4: Values that are keys
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  values_which_are_keys = []
  for key,value in my_dictionary.items():
    if my_dictionary.get(value, "Does not exist") != 'Does not exist':
      values_which_are_keys.append(value)
  return values_which_are_keys

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#Challenge-5: Largest value
# Write your max_key function here:
def max_key(my_dictionary):
  max_key = 0
  max_value = 0
  for key,value in my_dictionary.items():
    if value > max_value:
      max_value = value
      max_key = key
  return max_key
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
