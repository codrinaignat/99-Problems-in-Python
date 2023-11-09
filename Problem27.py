#Group the elements of a set into disjoint subsets.
import itertools

def disjointSubsets(setOfElements, setOfSubsets):
    
    sumOfElements = 0
    numberOfGroups = len(setOfSubsets)
    for i in range(0, numberOfGroups):
        sumOfElements = sumOfElements + setOfSubsets[i]
    #print(sumOfElements)
    #print(numberOfGroups)

    setOfElementsList = list(setOfElements)
    #print(setOfElementsList)

    if len(setOfElementsList) == sumOfElements:
        for j in range(0, numberOfGroups):
            subsets = list(itertools.combinations(setOfElementsList, setOfSubsets[j]))
            print(subsets)
    else:
        print("The number of elements in set does not match the sum of subsets array elements")
    subsetsListBackToSet = set(subsets)
    #print(subsetsListBackToSet)
    return subsetsListBackToSet

mySet = {"banane", "pere", "mere", "gutui"}
subsetLengths = [1, 2, 1]
print("Here the program executed again:")
print(disjointSubsets(mySet, subsetLengths))
