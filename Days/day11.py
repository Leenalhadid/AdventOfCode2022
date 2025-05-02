def main():
    import math
    
    with open("C:\\Users\\Sarah\\Desktop\\Saarland\\semester 2\\python\\Advent of code\\day11.txt", "rt") as inputFile:
        inputString = inputFile.read()
    
    inputList = inputString.split('\n')#it will give me each line as an item with in the  list and it will give it with the spaces
    
    monkeyIndex = []
    monkeyStartingItems = []
    monkeyOperation = []
    monkeyOperationFactor = []
    monkeyDivisibleByTest = []
    monkeyIfTrue = []
    monkeyIfFalse = []
    monkeyInspectItems = []
    
    for i in range(len(inputList) // 7): #while each monkey has the 7lines to finish all its info then we divided by seven to insure that the for loop will have just the range of the monkeys in the input
        #example ( if we have a 140 line in the text and we devided by 7 the line needed for each monkey then we will know that we have 20 monekies and our loop should end with 20)
    
        # line1
        monkeyIndex.append(int(inputList[i * 7 + 0][6:-1]))
        #it will start with the i as 0 and end with i as 7 so by multipling the i with 7 and adding 0 to 5 the line that we need to append its info will be reached
        # the [6:-1] is to insure taking just the number of the monkey we are at its position
    
        # line2
        monkeyStartingItems.append(list(inputList[i * 7 + 1][18:].strip().split(',')))
        #with i*7+1 the line that has the items for each monkey will be reached
        #to have just the numbers: the strip was used to remove spaces and split to split the numbers and appended them as list
    
        # line3
        monkeyOperation.append(inputList[i * 7 + 2][23])
        #working her in the same line but suppstracting different things one for the operation
        # and the other is the nr
        monkeyOperationFactor.append(inputList[i * 7 + 2][24:])
    
        # line4
        monkeyDivisibleByTest.append(int(inputList[i * 7 + 3][20:]))
    
        # line5
        monkeyIfTrue.append(int(inputList[i * 7 + 4][29:]))
    
        # line6
        monkeyIfFalse.append(int(inputList[i * 7 + 5][29:]))
    
        monkeyInspectItems.append(len(monkeyStartingItems[i]))
        #this list is to know how many times each monkey is toutching somehing and to append the number of items monkey started with
        #as len(monkeystartingitems)
    
    
    
    for round in range(20): # to loop 20 times
        for monkey in monkeyIndex: # to start with the monkies one by one the list is from [o to 7]
            for currentItem in monkeyStartingItems[monkey]:
                # will loop on the item with the same index number as the monkey index
    
                item = int(currentItem)
                # saved as intiger to have operation on it
    
                if monkeyOperation[monkey] == '*': #if the operation in the same index number is (*)
                    if monkeyOperationFactor[monkey].strip() == 'old':#if the factor before the operation is (old)
                        item **= 2
                        #it will rais the number to the power of 2
                    else:
                        # other than this we will have the number multiplied by the factor in the same index number
                        item *= int(monkeyOperationFactor[monkey])
                else:
                    #if the operation is not multipling this it is going to be summing
                    if monkeyOperationFactor[monkey].strip() == 'old':
                        #if the factor that we are going to sum with is the same number that we are working on
                        item *= 2
                        # will sum it with itself
                    else:
                        #if the factor is a number
                        item += int(monkeyOperationFactor[monkey])
                        # will sum this number with our item that we are working on
    
                item = item // 3#// because we want not decimal number
                # will devide the number that the is optained from any of the previous operation on 3.
    
                if (item % monkeyDivisibleByTest[monkey]) == 0:
                    #after deviding by 3 we check if the number id devisable on the number in the list of the monkeyDivisibleByTest
                    #in the same indexing for the monkey
                    monkeyStartingItems[monkeyIfTrue[monkey]].append(str(item))
                    #if it was devisable it will append the item to the number
                    monkeyInspectItems[monkeyIfTrue[monkey]] += 1#adding one to the monkey in the position equal to the true monkey position
                else:
                    monkeyStartingItems[monkeyIfFalse[monkey]].append(str(item))
                    #for the monkeystartingitems in the position that is equal to the position of the monkeyIfFalse in the position number of monkey
                    # will append the new value
                    monkeyInspectItems[monkeyIfFalse[monkey]] += 1
                    #in the same indexing position of the list of false for monkey ,will add one each time touching the items
    
            monkeyStartingItems[monkey].clear()
            #after going through all the items the list should be cleared of the items for the monkey  finished in the position of the monkey
            #returns empty list
    
    
    for monkey in monkeyIndex:
        monkeyInspectItems[monkey] -= len(monkeyStartingItems[monkey]) #because in the example the number was equal to the number without counting the last round inspection
    
    
    monkeyInspectItems.sort()
    print(monkeyInspectItems)
    print(monkeyInspectItems[-1] * monkeyInspectItems[-2])
    
    
    
    ############part 2
    
    import math
    
    with open("C:\\Users\\Sarah\\Desktop\\Saarland\\semester 2\\python\\Advent of code\\day11.txt", "rt") as inputFile:
        inputString = inputFile.read()
    
    
    
    inputList = inputString.split('\n')
    
    monkeyIndex = []
    monkeyStartingItems = []
    monkeyOperation = []
    monkeyOperationFactor = []
    monkeyDivisibleByTest = []
    monkeyIfTrue = []
    monkeyIfFalse = []
    monkeyInspectItems = []
    
    for i in range(len(inputList) // 7):
        # line1
        monkeyIndex.append(int(inputList[i * 7 + 0][6:-1]))
    
        # line2
        monkeyStartingItems.append(list(inputList[i * 7 + 1][18:].strip().split(',')))
    
        # line3
        monkeyOperation.append(inputList[i * 7 + 2][23])
        monkeyOperationFactor.append(inputList[i * 7 + 2][24:])
    
        # line4
        monkeyDivisibleByTest.append(int(inputList[i * 7 + 3][20:]))
    
        # line5
        monkeyIfTrue.append(int(inputList[i * 7 + 4][29:]))
    
        # line6
        monkeyIfFalse.append(int(inputList[i * 7 + 5][29:]))
    
        monkeyInspectItems.append(len(monkeyStartingItems[i]))
    
    m = 1
    for mod in monkeyDivisibleByTest:
       m = m * mod
    
    for round in range(10000):
        for monkey in monkeyIndex:
            for currentItem in monkeyStartingItems[monkey]:
    
                item = int(currentItem)
    
                if monkeyOperation[monkey] == '*':
                    if monkeyOperationFactor[monkey].strip() == 'old':
                        item **= 2
                    else:
                        item *= int(monkeyOperationFactor[monkey])
                else:
                    if monkeyOperationFactor[monkey].strip() == 'old':
                        item *= 2
                    else:
                        item += int(monkeyOperationFactor[monkey])
    
                item = item % m
    
                if (item % monkeyDivisibleByTest[monkey]) == 0:
                    monkeyStartingItems[monkeyIfTrue[monkey]].append(str(item))
                    monkeyInspectItems[monkeyIfTrue[monkey]] += 1
                else:
                    monkeyStartingItems[monkeyIfFalse[monkey]].append(str(item))
                    monkeyInspectItems[monkeyIfFalse[monkey]] += 1
    
            monkeyStartingItems[monkey].clear()
    
    print(monkeyInspectItems)
    
    for monkey in monkeyIndex:
        monkeyInspectItems[monkey] -= len(monkeyStartingItems[monkey])
    
    
    monkeyInspectItems.sort()
    print(monkeyInspectItems[-1] * monkeyInspectItems[-2])

if __name__ == "__main__":
    main()
