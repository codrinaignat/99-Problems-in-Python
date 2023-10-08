from itertools import groupby
def modified_encode(aList):
        def second_fcn(length):
            if len(length)>1: return [len(length), length[0]]
            else: return length[0]
        return [second_fcn(list(group)) for key, group in groupby(aList)]

aList = [0, 0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9]
print(modified_encode(aList))