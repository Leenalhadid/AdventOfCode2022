def main():
    import numpy as np
    
    with open('input.txt', 'r') as inputFile:
        inputList = inputFile.readlines()
    
    movements = []
    
    for entry in inputList:
        element = entry.split(' ')
        T = (element[0], int(element[1]))
        movements.append(T)
    
    start = np.array([0, 0])
    end = np.array([0, 0])
    
    def tailPositionChange(start, end):
        difference = start - end  #we count the difference between the two states
        # deppending on the difference we can determine how many steps the tail should move (we should add) on each dimension
        if difference[0] == 2 and difference[1] == 1:
            return end + np.array([1, 1])
        elif difference[0] == 1 and difference[1] == 2:
            return end + np.array([1, 1])
        elif difference[0] == 2 and difference[1] == 0:
            return end + np.array([1, 0])
        elif difference[0] == 2 and difference[1] == -1:
            return end + np.array([1, -1])
        elif difference[0] == 1 and difference[1] == -2:
            return end + np.array([1, -1])
        elif difference[0] == 0 and difference[1] == 2:
            return end + np.array([0, 1])
        elif difference[0] == 2 and difference[1] == 2:
            return end + np.array([1, 1])
        elif difference[0] == -2 and difference[1] == -2:
            return end + np.array([-1, -1])
        elif difference[0] == -2 and difference[1] == 2:
            return end + np.array([-1, 1])
        elif difference[0] == 2 and difference[1] == -2:
            return end + np.array([1, -1])
        elif difference[0] == 0 and difference[1] == -2:
            return end + np.array([0, -1])
        elif difference[0] == -1 and difference[1] == -2:
            return end + np.array([-1, -1])
        elif difference[0] == -2 and difference[1] == -1:
            return end + np.array([-1, -1])
        elif difference[0] == -2 and difference[1] == 0:
            return end + np.array([-1, 0])
        elif difference[0] == -2 and difference[1] == 1:
            return end + np.array([-1, 1])
        elif difference[0] == -1 and difference[1] == 2:
            return end + np.array([-1, 1])
        else:
            return end
    
    def headPositionUpdate(start, nextPoint): #moving the head position according to instructions
        if nextPoint == 'R':
            start[1] += 1
        elif nextPoint == 'L':
            start[1] -= 1
        elif nextPoint == 'U':
            start[0] += 1
        elif nextPoint == 'D':
            start[0] -= 1
        return start
    
    #used a set not to repeat the position that were already visited
    tailPositionsSet = set([tuple(end)]) #[] added in order to add the first tail of zeros as a full list
    
    for move in movements:
        d = move[1]
        while True:
            if d <= 0:
                break
            start = headPositionUpdate(start, move[0])
            d -= 1
            end = tailPositionChange(start, end)
            tailPositionsSet.add(tuple(end))
    
    print(len(tailPositionsSet))
    
    # part2
    
    nodes = [np.array([0, 0]) for _ in range(10)]
    
    tailPositionsSet = set([tuple(nodes[9])])
    for move in movements:
        d = move[1]
        while True:
            if d <= 0:
                break
            nodes[0] = headPositionUpdate(nodes[0], move[0])
            d -= 1
            i = 1
            while i < len(nodes):
                nodes[i] = tailPositionChange(nodes[i - 1], nodes[i])
                i += 1
            tailPositionsSet.add(tuple(nodes[9]))
    
    print(len(tailPositionsSet))

if __name__ == "__main__":
    main()
