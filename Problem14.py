def duplicate(aList):
    return [element for element in aList for i in (1,2)]

alist = [0, 1, 2, 3, 4, 5, 6]
print(duplicate(alist))
