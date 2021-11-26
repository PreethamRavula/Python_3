#Challenge-1: Larger sum
#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  i = 0
  j = 0
  for i in lst1:
    sum1 += i

  for j in lst2:
    sum2 += j

  if sum1 >= sum2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Challenge-2: Over 9000
#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for i in lst:
    if sum < 9000:
      sum += i

  return sum


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#challenge-3: Max Num
#Write your function here
def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
  return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#Challenge-4: Same Values:
#Write your function here
def same_values(lst1, lst2):
  new_list = []
  length = len(lst1)
  for i in range(0, length):
    for j in range(0, length):
      if lst1[i] == lst2[j] and i == j:
        new_list.append(i)

  return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Challenge-5: Reversed List:
#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
