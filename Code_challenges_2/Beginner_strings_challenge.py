#Challenge-1: Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  count = 0
  for letter in letters:
    if letter in word:
      count += 1
  return count

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

#Challenge-2: Count X
# Write your count_char_x function here:
def count_char_x(word, x):
  count = 0
  for letter in word:
    if letter == x:
      count += 1
  return count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

#Challenge-3: Count Multi X
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  split_word = word.split(x)
  return len(split_word) - 1
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

#Challenge-4: Substring Between
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  starting_index = word.find(start)
  ending_index = word.find(end)
  if starting_index and ending_index > -1:
    return word[starting_index + 1 : ending_index]
  return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#Challenge-5: X length
# Write your x_length_words function here:
def x_length_words(sentence, x):
  split_sentence = sentence.split()
  for word in split_sentence:
    if len(word) < x:
      return False
    else:
      return True
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True
