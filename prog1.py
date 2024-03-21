import numpy as np

arrayNumber = np.random.randint(0, 10, size=20)
print(arrayNumber)

# to make a group of unique numbers
# A = [5 7 6 7 6 0 2 6 6 8 7 4 7 5 4 1 2 9 6 0]
# unique_A = [5, 7, 6, 0, 2, 8, 4, 1, 2, 9]

uniqueList = []
for number in arrayNumber:
    if number in uniqueList:
        pass
    else:
        uniqueList.append(number)
#
print("unique: ", uniqueList)

uniqueList2 = list() # []
for number in arrayNumber:
    if number not in uniqueList2:
        uniqueList2.append(number)
#
print("unique2: ", uniqueList2)

# uniqueList3 = [number for number in arrayNumber if number not in uniqueList3] 

myList = []
myList2 = list()

# set, dict
uniqueSet = set ()
for num in arrayNumber:
    uniqueSet.add(num)
#
print(uniqueSet)
for elem in uniqueSet:
    print(elem, end=' ')
print()
