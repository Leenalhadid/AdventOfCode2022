def main():
    with open('input.txt', 'rt') as inputString:
         inputList = inputString.read().splitlines()
    
    
    
    sums = []
    Calories = 0
    for i in inputList:
        if i != '': #to seperate the elves passed on the empty space
            Calories += int(i) #adding all the sum of all one elves calories to one variable
        else: # it will implement this when it reaches an empty line which indicades that the elve calroes ended for summing
            sums.append(Calories)
            Calories = 0 #to start the sum of the other elve starting from zero
    
    print(max(sums))
    
    
    ##### part 02
    
    sums.sort(reverse=True) #ordering the sums for all the elves in a revers way(the largest to smallest)
    print(sum(sums[:3])) #take the first three largest numbers after ordering

if __name__ == "__main__":
    main()
