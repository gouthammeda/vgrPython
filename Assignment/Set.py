input = {1,2,3,4,5}
output = {5,2,3,4,1}

list_input = list(input)


def swapList(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0,last)
    list.append(first)
    return list

print(swapList(list_input))

def findMissingNumbers(n):
    numbers = set(n)
    # length= len(n)
    output = []
    for i in range(1,n[-1]):
        if i not in numbers:
            output.append(i)
    return output


listOfNumbers = [1,2,3,5,6,7,8,9,10,11,13,14,16]
print(findMissingNumbers(listOfNumbers))

