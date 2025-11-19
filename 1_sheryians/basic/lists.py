""" 1. Print positive and negative elements of an List? """
# arr = [23,54,-65,90,-15,-40,78]
# positiveNum = []
# negativeNum = []

# for i in arr:
#   if i >= 0:
#     positiveNum.append(i)
#   else:
#     negativeNum.append(i)

# print(f"Positive number {positiveNum}")
# print(f"Negative number {negativeNum}")

""" 2. Mean of List elements? """
# avgList = [11,54,96,21,5,8]
# listLength = len(avgList)
# avg = 0

# for i in avgList:
#   avg += i 

# print(avg / listLength)

""" 3. Find the greatest element and print its index too? """
# arr = [8,12,11,15,32,17,99]
# greatest = arr[0]
# index = 0

# for i in range(len(arr)):
#   if arr[i] > greatest:
#     greatest = arr[i]
#     index = i

# print(greatest,i)

""" 4. Find the second greatest element? """
# arr = [8,12,11,15,32,17,99,70]
# greatest = arr[0]
# secondGreatest = arr[0]

# for i in arr:
#   if i > greatest:
#     secondGreatest = greatest
#     greatest = i
  
#   elif i > secondGreatest:
#     secondGreatest = i

# print(secondGreatest)


""" 5. Check if List is sorted or not. """
# arr = [22,3,4,5,6,7]

# for i in range(len(arr)-1):
#   if arr[i] < arr[i+1]:
#     continue
#   else:
#     print("List is not sorted")
#     break

# else:
#   print("List is sorted")