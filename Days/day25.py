def main():
    with open("input.txt", "rt") as inputFile:
        inputList = inputFile.read().splitlines()
    
    ##line 11 why are taking -1 and not -2 ???
    
    sum = 0 # to summ all the temp that we have from each itteration (this is for the sum for all the strings )
    for number in inputList: #we take the full number as one string
        temp = 0 #the sum of the number we are getting after one itteration over one string
        for i in range(len(number)): # looping over the numbers of the full string we took
            if number[i] == '=':
                temp += 5 ** (len(number) - 1 - i) * -2 #(-1) is to remove the \n from the len of the string and get its actual len
                #then we substract the i which is the position of the number so the lenght of the string will be exavtually equal to the position of the number
            elif number[i] == '-':
                temp += 5 ** (len(number) - 1 - i) * -1
            elif number[i] == '0':
                pass  # temp += 5 ** (len(number) - 2 - i) * 0 = we will have 0 in any case so we do not need to add it again
            elif number[i] == '1':
                temp += 5 ** (len(number) - 1 - i) * 1
            else:
                temp += 5 ** (len(number) - 1 - i) * 2
                #we multiply the number after 5** with the value that is equal to it as it is mentioned in the proplem
        sum += temp
    
    print(sum)
    
    ###### part 02
    result = ""
    
    while sum != 0:
        r = sum % 5
        sum = sum // 5 #to know how many states we have
        if r > 2:  # to evaluate minus 1 and minus two status because we have the range just between [-2 and 2 ] we cannot have 3,4
            r -= 5
            sum += 1
        if r == 2:
            result = "2" + result
        elif r == 1:
            result = "1" + result
        elif r == 0:
            result = "0" + result
        elif r == -1:
            result = "-" + result
        elif r == -2:
            result = "=" + result
    
    print(result)

if __name__ == "__main__":
    main()
