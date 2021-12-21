# Challenge-1: Check Name
# Write your check_for_name function here:
def check_for_name(sentence, name):
  name_lower = name.lower()
  sentence_lower = sentence.lower()
  if name_lower in sentence_lower:
    return True
  return False
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# Challenge-2: Every Other Letter
# Write your every_other_letter function here:
def every_other_letter(word):
  new_string = ''
  i = 0
  while i < len(word):
    new_string += word[i]
    i += 2
  return new_string

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

#Challenge-3: Reverse
# Write your reverse_string function here:
def reverse_string(word):
  reverse_string = ''
  i = -1
  while i >= -1 * len(word):
    reverse_string += word[i]
    i -= 1
  return reverse_string

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

#Challenge-4: Make Spoonerism
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  new_word = word2[0] + word1[1:] + " " + word1[0] + word2[1:]
  return new_word
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

#Challenge-5: Add Exclamation
# Write your add_exclamation function here:
def add_exclamation(word):
  length = len(word)
  while length < 20:
    word = word + '!'
    length += 1
  return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
