#Challenge-1: Word Length Dict
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  word_length = [len(word) for word in words]
  word_and_length_dict = {key:value for key, value in zip(words, word_length)}
  return word_and_length_dict
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

#Challenge-2: Frequency Count
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  word_frequency_dict = {}
  for word in words:
    if word not in word_frequency_dict:
      word_frequency_dict[word] = 0
      word_frequency_dict[word] += 1
    else:
      word_frequency_dict[word] += 1
  return word_frequency_dict

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#Challenge-3: Unique values
# Write your unique_values function here:
def unique_values(my_dictionary):
  unique_values_list = []
  for value in my_dictionary.values():
    if value not in unique_values_list:
      unique_values_list.append(value)
  return len(unique_values_list)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

#Challenge-4: Count First Letter
# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for last_name in names.keys():
    letter = last_name[0]
    if letter not in letters:
      letters[letter] = 0
      letters[letter] += len(names[last_name])
    else:
      letters[letter] += len(names[last_name])
  return letters
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
