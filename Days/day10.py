def main():
    # %40 and not %20 because the size of every cycle is 40 and it is just sutable for the inputs which is equal
    # to the multiplies of 40
    
    with open('input.txt', 'rt') as inputFile:
        inputString = inputFile.read()
    
    inputList = inputString.split('\n')
    
    sumOfSignalsStrength = 0
    x = 1
    cycle = 0
    crt = ''
    for instruction in inputList[:-1]: #while the last line is emplty
        if instruction.strip() == 'noop':
            cycle += 1
            if cycle % 40 == 1: #to start a new cycle for the CRT, entering a new cycle by adding a new line
                crt += '\n'
            if x <= cycle % 40 <= x+2: # to check if the number of cycle is in the range between the value of x and two position after
                crt += '#' #because we are allowed to put pixel just in the postions equal to x or x+2
            else:
                crt += '.' #if the cycle not in this range we put '.'
            if (cycle - 20) % 40 == 0: # to know if we are in any of the ranged cycles (then the reminder should equal to 0) indicate that we are entering new cycle
                #for part 01
                sumOfSignalsStrength += cycle * x #her we did't use cycle-1 because it's only one cycle we dont't finish in the middle of it
        else: #in the case of addx
            cycle += 1
            if cycle % 40 == 1: #for the part 2 the same concept
                crt += '\n'
            if x <= cycle % 40 <= x + 2: #we are doing %40 because we want to have the number of the cycle suitabel for the positions in every row
            #while every row the length of it is not more than 40 (x=6 and the cycle is 86 it will never be the case that the cycle will be equale to the x)
            #therefore we have 86%40 = 6 so the x=6 we can draw a (#)
                crt += '#'
            else:
                crt += '.'
            cycle += 1 #we check if the cycle is in the range of the x to x+2 after each (cycle += 1)
            if cycle % 40 == 1:# just to go back again to the new line if we entered a new cycle
                crt += '\n'
            if x <= cycle % 40 <= x+2:
                crt += '#'
            else: 
                crt += '.'
                # part 01 specific lines
            if (cycle - 20) % 40 == 0:
                sumOfSignalsStrength += cycle * x
            if (cycle - 20) % 40 == 1: # in the case that we ended our cycle in the middel of addx
                sumOfSignalsStrength += (cycle - 1) * x #then we should multiply the cycle-1 with x insted of the cycle number we have
            v = int(instruction.split()[1]) #after we multiply we add the value not before
            x += v #we finish first the number of cycles should be added with (addx) and then we check if the cycle is finished ot not
                    #if it was finished we add the value to the next cycle not the one we finished and multiply depending on the cycle we have or the cycle -1 if we finish in the middle of addx
    
    print(sumOfSignalsStrength)
    
    print(crt)

if __name__ == "__main__":
    main()
