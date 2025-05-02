def main():
    import numpy as np
    
    with open("C:\\Users\\Sarah\\Desktop\\Saarland\\semester 2\\python\\Advent of code\\day12.txt", "rt") as inputString:
        inputList = inputString.read().splitlines()
    
    
    inputArray = np.array([list(row) for row in inputList]) #to have each line as a list of characters in bigger list
    startingPoint = np.where(inputArray.flatten() == 'S')[0][0] # part 1
    #np.where return an 2D array of all the positions found and data rype. [0] to index the first dim for the array and the second[0] to take the first position found
    #start = np.where(inputArray.flatten() == 'a')[0]  # part2
    
    endingPostion = np.where(inputArray.flatten() == 'E')[0][0]
    
    inputArray[np.where(inputArray == 'S')] = 'a' #to change the S to a in every postion
    inputArray[np.where(inputArray == 'E')] = 'z' #to change the E to b in every postion found to make it accecable while looping
    
    length = inputArray.shape[0] #the number of rows
    width = inputArray.shape[1] #the number of colums
    
    A = np.zeros((width * length, width * length)) #to change the number of colums and rows by changing the size of the matrix
    #so the numbers of row and colums will be equal to the number of length*width and it will be filled of zeros
    #print(A.shape)
    
    
    for i in np.arange(length): #looping over the rows
        for j in np.arange(width): #looping over the colums
            reachedIndices = []
            current = inputArray[i][j] #to save the value of the current position
    
            # to get the item in the previous row after checking that we are not in the first row by checking if the row number is bigger than 0
            if 0 < i:
                top = inputArray[i - 1][j]
    
            #to get the item in the next row same colum but after checking that we are not in the last row by cheking that it  is smaller than the last row number
            if i + 1 < length:
                bottom = inputArray[i + 1][j]
    
            # to get the item in the previous colum  after checking that we are not in the first colum by checking if the colum number is bigger than 0
            if 0 < j:
                left = inputArray[i][j - 1]
    
            #to get the item in the next colum but after checking that we are not in the last colum by cheking that it  is smaller than the last colum number
            if j + 1 < width:
                right = inputArray[i][j + 1]
            # top
            #cheking if every item we saved that is a nighbor is bigger or equal to the current position item
            if 0 < i and ord(top) <= ord(current) + 1:
                #adding the index of the reachable nighbors as a flatten position to change it to ones later in the zeros.array
                reachedIndices.append((i - 1) * width + j)
            # bottom
            #if the bottom nighbor is smaller to just bigger in one than the current i will add the faltten index of it
            if i + 1 < length and ord(bottom) <= ord(current) + 1:
                reachedIndices.append((i + 1) * width + j)
            # left
            if 0 < j and ord(left) <= ord(current) + 1:
                reachedIndices.append(i * width + j - 1)
            # right
            if j + 1 < width and ord(right) <= ord(current) + 1:
                reachedIndices.append(i * width + j + 1)
    
            row = i * width + j #it will indicate the next position possibility by changing the position of its accessable nighbors to 1
            #by changing the postion of the colums that we saved to one in the zeros matrix
            for col in reachedIndices: #to change the value of the colums reachable fro the current position
                A[row, col] = 1
    T = A
    shortestPath = 1
    # stop criteria we will keep multipling until the condition not True any more(the positions in the while loop is not 0 anymore)
    while (T[startingPoint, endingPostion] == 0) : #.all # part2 all()
        T = T @ A #if the positions are zero then the matrix will be multiplied by itself again and rechack the positions
        shortestPath += 1 #adding the steps one until we rach the point that the positions are 1 then the number of steps indicate the
        #the positions are accessable from each others after this numbers of steps
    
    print(shortestPath)

if __name__ == "__main__":
    main()
