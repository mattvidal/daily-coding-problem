"""

Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""

def ReturnArrayProduct(array):

    aux = 1
    newArray = [0 for x in range(len(array))]
    n = range(0, len(array))

    for i in range(0, len(array)):

        for j in (j for j in n if j != i):
            aux *= array[j]
            
        newArray[i] = aux
        aux = 1

    return newArray


array = [3, 2, 1]
print(ReturnArrayProduct(array))