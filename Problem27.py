#Group the elements of a set into disjoint subsets.

mySet = {"apples", "strawberries", "pears", "cherries", "bananas", "plums", "watermelons"}
mySets = [2, 3, 2]

def disjointSubsets (setOfElements, setOfSubsets):
    sumOfElements = 0
    numberOfGroups = 0
    for i in range(0, len(setOfSubsets)):
        sumOfElements = sumOfElements + setOfSubsets[i]
        numberOfGroups = numberOfGroups + 1
    print(sumOfElements)
    print(numberOfGroups)
        
    if len(setOfElements) == sumOfElements:
        for j in range(0, numberOfGroups):
            
    else:
        print("The number of elements in set does not match the sum of subsets array elements")
        
print(disjointSubsets(mySet, mySets))
