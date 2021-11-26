#Challenge-1: Every Three numbers
#Write your function here
def every_three_nums(start):
    return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))

#Challenge-2: Remove Middle
#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end + 1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Challenge-3: More Frequent Item
#Write your function here
def more_frequent_item(lst, item1, item2):
  count_1 = 0
  count_2 = 0
  for item in lst:
    if item == item1:
      count_1 += 1

    elif item == item2:
      count_2 += 1

  if count_1 >= count_2:
    return item1

  else:
    return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Challenge-4: Double Index
#Write your function here
def double_index(lst, index):
  if index <= (len(lst) - 1):
    lst[index] = 2 * lst[index]
    return lst

  else:

    return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#Challenge-5: Middle item
import math
#Write your function here
def middle_element(lst):
  length = len(lst)
  if len(lst) % 2 == 0:
    middle = (lst[int(length/2)] + lst[int(length /2) - 1]) / 2
    return middle

  else:
    middle = lst[int((length - 1) / 2)]
    return middle

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
