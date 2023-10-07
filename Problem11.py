from itertools import groupby
def encode_modified(alist):
        def aux(lg):
            if len(lg)>1: return [len(lg), lg[0]]
            else: return lg[0]
        return [aux(list(group)) for key, group in groupby(alist)]

aList = [0, 0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9]
print(encode_modified(aList))