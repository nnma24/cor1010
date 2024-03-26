filename = "pg1342.txt"

filehandler = open(filename, "r", encoding='utf-8')

n = 0
while True:
    line = filehandler.readline()
    n += 1
    print(n, line)
    if n > 10:
        break

