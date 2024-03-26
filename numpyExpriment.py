import numpy as np

longString = "Oh, well! it is just as he chooses. Nobody wants him to come."
# ; though i shall always say that he used my daughter extremely ill; and, if I was
# her, I would not have put up with it. Well, my comfort is, I am sure
# Jane will die of a broken heart, and then he will be sorry for what he
# has done."

print( len(longString) )

# compute the number of characters in longString

count = 0
for ch in longString:
    count += 1
    # print(ch)
print(count, len(longString))


# make a list of unique letter in longString
uniqueletters = []
letterSet = set()
for letter in longString:
    if letter not in uniqueletters:
        uniqueletters.append(letter)
        letterSet.add(letter)
        #
#
print("unique letters = ", len(uniqueletters), uniqueletters, )
print("unique set = ", len(letterSet), letterSet)

letterList = []
for elem in letterSet:
    letterSet.append(elem)
#
letterList2 = list( letterSet )
print(letterList)
print(letterList2)



print(letterSet[0])