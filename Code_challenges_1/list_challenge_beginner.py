#Challenge-1: Append size
#Write your function here
def append_size(lst):
  length = len(lst)
  lst.append(length)
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108

#Challenge-2: Append sum
#Write your function here
def append_sum(lst):
  i = 0
  while i < 3:
    sum = lst[-2] + lst[-1]
    lst.append(sum)
    i += 1
  return lst


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Challenge-3: Larger List
#Write your function here
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#Challenge-4: More than N
#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#Challenge-5: Combine sort
#Write your function here
def combine_sort(lst1, lst2):
  new_list = lst1 + lst2
  sorted_list = sorted(new_list)
  return sorted_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10])) 
