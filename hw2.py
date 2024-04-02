filename = "pg1342.txt"

# 1. make a list off unique letters
unqLetters = set ()
with open(filename, "r", encoding='utf-8') as filehandler:
    n = 0
    while True:
        line = filehandler.readline()
        if not line:
            break
        n += 1
        for letter in line:
            unqLetters.add(letter)
        # print(n, line)
        # if n > 3:
        #     break
    #
#
print(f"Total {n} lines from {filename}:{(unqLetters)} letters in the set {unqLetters}")

