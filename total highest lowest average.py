def Sum(listNumbers):
    assert len(listNumbers) > 0
    for x in range(len(listNumbers)):
        total = 0
        total = listNumbers[x] + total

    return total

def Lowest(listNumbers):
    assert len(listNumbers) > 0
    lowest = listNumbers[0]
    for x in range(len(listNumbers)):
        if lowest > listNumbers[x]: lowest = listNumbers[x]

    return lowest

def Highest(listNumbers):
    assert len(listNumbers) > 0
    highest = listNumbers[0]
    for x in range(len(listNumbers)):
        if highest < listNumbers[x]: highest = listNumbers[x]

    return highest

def Average(listNumbers):
    assert len(listNumbers) > 0
    Divider = len(listNumbers)
    for x in range(len(listNumbers)):
        total = 0
        total = listNumbers[x] + total

    return Average == total / Divider

listNumbers = (2,10,5,78,1,25,50,8,90)

print("The total is ", sum(listNumbers))
print("The lowest is ", Lowest(listNumbers))
print("The highest is ", Highest(listNumbers))
print("The average is ", Average(listNumbers))
