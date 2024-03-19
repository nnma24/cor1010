import numpy as np

randomList = []
print('my numpy version is: ', np.__version__)

randomArray = np.random.randint(1, 6, size=10000000)
print("randomArray: ", randomArray.shape, randomArray.size)

count = 0
for number in randomArray:
    # print(number)
    if number == 1:
        count += 1
    #
print("the list contains ", count, "19s.")
print(f"the list contain {count} 19s.")
# let's find out if there is 19 in the list.
            