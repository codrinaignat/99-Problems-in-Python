#Group the elements of a set into disjoint subsets.
import itertools
def disjointSubsets(setOfElements, setOfSubsets):
    sumOfElements = 0
    numberOfGroups = len(setOfSubsets)
    for i in range(0, numberOfGroups):
        sumOfElements = sumOfElements + setOfSubsets[i]
    setOfElementsList = list(setOfElements)
    if len(setOfElementsList) == sumOfElements:
        for j in range(0, numberOfGroups):
            subsets = list(itertools.combinations(setOfElementsList, setOfSubsets[j]))
            subsetsListBackToSet = set(subsets)
            print(subsetsListBackToSet)
    else:
        print("The number of elements in set does not match the sum of subsets array elements")
    return 

mySet = {"aldo", "beat", "carla", "david", "ivan"}
subsetLengths = [2, 3]
print(disjointSubsets(mySet, subsetLengths))
