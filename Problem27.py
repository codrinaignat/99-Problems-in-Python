#Group the elements of a set into disjoint subsets.
import itertools

def disjointSubsets(setOfElements, setOfSubsets):
    
    sumOfElements = 0
    numberOfGroups = len(setOfSubsets)
    for i in range(0, numberOfGroups):
        sumOfElements = sumOfElements + setOfSubsets[i]
    print(sumOfElements)
    print(numberOfGroups)

    setOfElementsList = list(setOfElements)
    print(setOfElementsList)

    if len(setOfElementsList) == sumOfElements:
        for j in setOfSubsets:
            subsets = list(itertools.combinations(setOfElementsList, setOfSubsets[j]))
            print(subsets)
    else:
        print("The number of elements in set does not match the sum of subsets array elements")
    subsetsListBackToSet = set(subsets)
    print(subsetsListBackToSet)
    return subsetsListBackToSet

mySet = {"apples", "strawberries", "pears", "cherries", "bananas", "plums", "watermelons"}
mySets = [2, 3, 2]
print(disjointSubsets(mySet, mySets))
