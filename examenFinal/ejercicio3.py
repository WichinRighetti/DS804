## Dada una lista de enteros y un entero X, genera una funcion que regrese los indices de dos elementos de la lista cuyas suma sea igual a X.
# Ejemplos:[1,2,3,4].5 -> (1,2) | [8,1,7],9 -> (0,1) | [1,3,1].5 -> ()


# on this code findIndex will take two params 
def findIndex(nums, target):
    # Make object 
    numDict = {}

    # Using enumerate to get value and index of loop
    for i, num in enumerate(nums):
        # Each loop will take out num out of target
        complement = target - num
        # If indexes are found return result
        if complement in numDict:
            return [numDict[complement], i]
        numDict[num] = i

    return None

numbers = [2, 4, 6, 10]
targetSum = 14

result = findIndex(numbers, targetSum)
print(result)

