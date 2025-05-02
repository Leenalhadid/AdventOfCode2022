
def main():
    with open("input.txt", "rt") as inputString:
        inputList = inputString.read().splitlines()
    
    
    
    preMixed = []
    mixed = []
    
    for x in inputList:
        preMixed.append(int(x))
    
    
    mixedIndices = list(range(len(preMixed))) #to know how may positions I have and then to use those positions
    
    
    for n in range(len(preMixed)): #to cover all the numbers in the list and change there positions
        i = mixedIndices.index(n) #it searches for the number n  in this list(ex: n= 3, then we search for the three in the
        #indexlist to replace the position of that number that has this index number in the premixedlist with its new position later
        del mixedIndices[i]
        j = (i + preMixed[n]) % (len(preMixed) - 1) #to make sure that we are going back again to the first and last elements and we are not going out of the
        #list range (while % will give us a number in the range of the list)
        mixedIndices.insert(j, n) # to insert the  n in the j position in the mixed list while later we can map over the normal list
        #and replace each position we have in the mixedlist(while the numbers there represent the positions of the elements) with the
        #number that suits the position in the premixed
    
    for i in mixedIndices: #to replace the numbers of positions we have in this list with the real numbers that they represent it
        mixed.append(preMixed[i])
    
    
    print(mixed[(mixed.index(0) + 1000) % len(mixed)] + mixed[
        (mixed.index(0) + 2000) % len(mixed)] + mixed[
              (mixed.index(0) + 3000) % len(mixed)])
    #if the position was in the range of 5000 after the addition of 1000 and 2000 and 3000
    # the reminder should give the same position that we should have
    
    #####part 02
    
    preMixed.clear() #because we will change the values of the list we had
    mixed.clear() #it is gonna be changed because we changged the values
    
    for x in inputList:
        preMixed.append(int(x) * 811589153) # we changed the values in the input list
    
    mixedIndices = list(range(len(preMixed)))
    
    for _ in range(10):  # second part mixing 10 times
        for n in range(len(preMixed)):
            i = mixedIndices.index(n)
            del mixedIndices[i]
            j = (i + preMixed[n]) % (len(preMixed) - 1)
            mixedIndices.insert(j, n)
    
    for i in mixedIndices:
        mixed.append(preMixed[i])
    
    print(mixed[(mixed.index(0) + 1000) % len(mixed)] + mixed[
        (mixed.index(0) + 2000) % len(mixed)] + mixed[
              (mixed.index(0) + 3000) % len(mixed)])

if __name__ == "__main__":
    main()
