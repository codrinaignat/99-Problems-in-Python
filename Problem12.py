def decode(alist):
    def aux(g):
        if isinstance(g, list): return [(g[1], range(g[0]))]
        else: return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]

aList = [0, 0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9]
print(decode(aList))