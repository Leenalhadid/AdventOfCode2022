def main():
    with open("C:\\Users\\Sarah\\Desktop\\Saarland\\semester 2\\python\\Advent of code\\day18.txt", "rt") as inputString:
        inputList = inputString.read().split()
    
    
    Cubes = []
    
    
    for item in inputList:#taking the first item in the list inputString
        items = []
        for j in item.split(','):#split the string item we are taking to avoid taking the (,)
            items.append(int(j))#to have every item in alist
        Cubes.append(items)#list of lists of the lines
    
    
    
    Sides= []
    for cube in Cubes: #list of the cubes each cube
        for dimension in range(len(cube)): #to work on each dimension we have one loop after the other so we will have the loop three times
            copyofcube = cube.copy() #to change on the copy
            adding = cube[dimension] +1 #adding on the current dimension 1 (either x or y or z)
            copyofcube[dimension] = adding #we will add the new value after adding to the position of the old dimension
            if copyofcube not in Cubes: #checking if the side is already existed
                Sides.append(copyofcube) # if not we will added to the sides lists
            copy2ofcube = cube.copy() #to change the same dimension we are working in but by substracting
            substract = cube[dimension] -1 #same as adding
            copy2ofcube[dimension] = substract
            if copy2ofcube not in Cubes:
                Sides.append(copy2ofcube)
    
    print(len(Sides)) #we will have the number of sides that are free and not conected to the real (border) cubes
    
    ##############part 02
    
    cubes = []
    for i in Cubes:
        cubes.append(tuple(i))
    
    #to find the smallest X,Y,Z (-1) for each to know the cube that is surronding the whole cubes
    minimum = [min(c[i] - 1 for c in cubes) for i in range(3)]
    #to find the largest X,Y,Z (+1) for each to know the cube that is surronding the whole cubes
    maximum = [max(c[i] + 1 for c in cubes) for i in range(3)]
    
    air_cubes = 0
    seen = set()
    #we start from the largest aircube and we expose it till we reach a point that the sides of those cubes in the air
    # are in the real cubes then the limit of air cube will be ended
    queue = [tuple(maximum)]
    while queue:
        currentCube = queue.pop(0)
        if currentCube in cubes:
            air_cubes += 1
            continue
        if currentCube not in seen:
            seen.add(currentCube)
            #the zip will add the values in order of d to the current cube so in the end we will have the final 6 sides of this cubes after summing with d
            neighbors = [tuple(sum(x) for x in zip(currentCube, d)) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
            for n in neighbors:
                #to isure that all dimension of each new cube of the nighbores are in the air space then we will added to the queue
                # to expande it again and see if it is nighboors are still in the airspace or not
                # untill we reach a real cube side then we stop to expand this cube
                if all(minimum[i] <= n[i] <= maximum[i] for i in range(3)):
                    queue.append(n)
    
    print(air_cubes)

if __name__ == "__main__":
    main()
