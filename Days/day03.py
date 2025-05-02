def main():
    import string
    
    with open('input.txt', 'rt') as inputString:
        inputList = inputString.read().splitlines()
    
    mutual = []
    for i in inputList:
        splitting = i[0: len(i) // 2]  # to take all the values in the range of 0 till half of i
        halfs = i[len(i) // 2: len(i)]  # to take the other half
        comparison = list((set(splitting).intersection(halfs)))  # it will return only the items existed in both sets as a list
        mutual.append(comparison[0])  # [0] to return just the element no the whole list
    
    letter_count = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))  # string.ascii_lowercase and the other are strings containing the alphabest in uper and lower case
    
    sums = []
    for i in mutual:  # the list that contain the letters we found by intersection
        sums.append(letter_count[i])  # we get the value for the key[i] and put it in sums
    
    print(sum(sums))
    
    ####### part 02
    
    slices = [] # a list of lists each list contain three elements
    items =[]
    for i in inputList: # it is going to be empty at the end
        while len(inputList) >= 3: # to execute the loop while there is elements enough to do so
            item1 = inputList.pop(0)
            items.append(item1)
            item2 = inputList.pop(0)
            items.append(item2)
            item3 = inputList.pop(0)
            items.append(item3)
            slices.append(items)
            items = []
            
    #letter_count = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))
    # looping over each list of the slice list and then just indexing every element of the lists of three and have a set for
    #those strings to find the intersection
    R = list()
    for i in slices:
        A = list(set(i[0]) & set(i[1]) & set(i[2])) #the and between the sets works as the intersection
        R.append(letter_count[A[0]]) # to append the value of the letter we found by searching for thr key value in the dict
    
    print(sum(R))

if __name__ == "__main__":
    main()
