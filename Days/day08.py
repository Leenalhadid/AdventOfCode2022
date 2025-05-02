def main():
    import numpy as np
    
    with open('input.txt', 'rt') as inputString:
        inputList = inputString.read().splitlines()
    
    visibleOnTheEdge = 2 * (len(inputList) + len(inputList[0])) - 4 # to exclude the edges(first and last row and first and last colum)
    #-4 is because we do not want to repeat the numbers on the corners
    #len(inputlist) gives the row numbers , len(inputList[o] gives the first row len of elements which is equal to the number of colums
    visibleInTheInterior = 0
    treesLength = []
    
    for i in range(len(inputList)): # it is the range that is equal to the row number
        row = []
        for j in range(len(inputList[i])):# the range that is equal to the length of the elements of the first row and that is equal to the row numbers
            row.append(int(inputList[i][j])) #it is going to append the values in those two indexes (positions ) of the i as a row and j as a colum
        treesLength.append(row) # then it is going to append the row list to another list
    
    trees = np.array(treesLength)
    for i in range(1,trees.shape[0]-1):#while we already counted the edges first
        for j in range(1, trees.shape[1]-1):
            #checking the left, right, down, and up
            if trees[i,j] > max(trees[i,:j]) or trees[i,j] > max(trees[i,j+1:]) or trees[i,j] > max(trees[i+1:,j]) or trees[i,j] > max(trees[:i,j]):
              visibleInTheInterior += 1
    
    print(visibleOnTheEdge + visibleInTheInterior)
    
    ####################part 02
    
    score = []
    
    for i in range(1, trees.shape[0]-1):
        for j in range(1, trees.shape[1]-1):
            a = b = c = d = 0
            #left
            #[] in the row i from the colum starting from 0 to j but flipped
            for x in np.flip(trees[i,:j]):# we did the flip to make the order go from the left of j to the index 0 while it has to check the nighbores first
              a += 1 #we first add the value then we check if the value is bigger we break beacuse the value we stop at is included in the counter
              if x >= trees[i,j]:#after adding one we check if it is bigger we break and we don not check the next position
                break
             #right
              #in the row i but the clum starting from the next item to j to the end of the row
            for x in trees[i,j+1:]:
              b += 1
              if x >= trees[i,j]:
                break
            #bottom
            #in the row that is after the row of i till the end of rows in the position equal to the position of j(same colum)
            for x in trees[i+1:,j]:
              c += 1
              if x >= trees[i,j]:
                break
            #top
            #in the row that is befor the row of i till the row 0 (because we used flip)
            # if we did not used then it will start checking from 0 till i and that is not correct because we check starting from neighbors
            # (here row 0 is included it is just excluded from the range of looping)
            for x in np.flip(trees[:i,j]):
              d += 1
              if x >= trees[i,j]:
                break
            score.append(a*b*c*d)
    
    print(max(score))

if __name__ == "__main__":
    main()
