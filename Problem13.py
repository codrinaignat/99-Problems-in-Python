from itertools import groupby
def encode_direct(alist):
    def aux(k, g):
        l = len(list(g))
        if l>1: return [l, k]
        else: return k
    return [aux(key, group) for key, group in groupby(alist)]

alist = [0, 0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9]
print(encode_direct(alist))
