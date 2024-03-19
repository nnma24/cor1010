import numpy as np

print('my numpy version is: ', np.__version__)

randomList = []
for i in range(100):
    n = np.random.randint(1,20)
    randomList.append(n)

    # print("randomList:", randomList)

    randomArray = np.random.randint(1, 6, size=10000000)
    print("randomArray: ", randomArray.shape, randomArray.size)

    count = 0
    for number in randomList:
        # print(number)
        if number == 19:
            count += 1
    #
    print("the list contains ", count, "19s.")
    print(f"the list contain {count} 19s.")
    # let's find out if there is 19 in the list.
            