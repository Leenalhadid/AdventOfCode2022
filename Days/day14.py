
def main():
    from copy import deepcopy

    with open("input.txt", "rt") as inputString:
        inputList = inputString.read().splitlines()

    #splitting the inputs to a list of lists
    rocks = []
    for i in inputList:
        first = i.split('->')
        line = []
        for j in first:
            second = j.split(',')
            position = tuple(map(int, second))
            line.append(position)
        rocks.append(line)

    # the new rocks that are between the input ranges
    added_rocks = set()
    # to compar each 2 rocks and fille up the gaps values between x and y
    def compairing_ranges(t1, t2):
        x1, y1 = t1# as a first values to compare
        x2, y2 = t2#as second values to compare
        added_rocks.add(t1) #to get ride of th list of lists
        added_rocks.add(t2)
        if x1 != x2:
            minimum = min(int(x1), int(x2))#to know to which value to add on
            adding_value = abs(int(x1) - int(x2)) - 1 #to count the difference between the values
        while adding_value > 0:
            while adding_value > 0:
                new_value = minimum + 1#adding to the samllest value
                new_one = (new_value, y1) #creating and adding  new rock
                added_rocks.add(new_one)
                adding_value = adding_value - 1
                minimum = new_value
        if int(y1) != int(y2):
            minimum = min(int(y1), int(y2))
            adding_value = abs(int(y1) - int(y2)) - 1
        while adding_value > 0:
            new_value = minimum + 1
            new_one = (x1 , new_value)
            added_rocks.add(new_one)
            adding_value = adding_value - 1
            minimum = new_value

    return #the adding_rocks is being changed inside the function so we don not need to return anything while the changes
           #are inside the function

Limitation = 0 #the max_y that we can found
for Line in rocks:
    for i in range(len(Line)-1):
        r1 = Line[i] #the two values to compare in the previous function
        r2 = Line[i+1]
        Limitation = max(r2[1], r1[1])  # this is the rock limitation to not cross
        compairing_ranges(r1,r2)


Cave = deepcopy(added_rocks) #this is for working on part 2

#the function will study the direction availabe to the sand to move and when there is no place to move it will return it after
#preforming changes
def Sand_direction(position):
    x, y = position #starting sand in this function
    # first we check down
    #y += 1
    if (x,y+1) not in added_rocks:
        return (x, y+1)
    # we check left
    if (x-1,y+1) not in added_rocks:
        return (x-1, y+1)
    # we check right
    if (x+1, y+1) not in added_rocks:
        return (x+1,y+1) #we return when the sand have a place in this position or others in previous
    return (False,False) # comes to rest when all the previous are blocked



Unites = 0
last_call = 500,0
print('Limitation: ', Limitation)
# for part 2,
while last_call[1] < Limitation:
    x,y = 500, 0
    while last_call[1] < Limitation and (x,y) != (False,False): # we go in this while until we are out of limitation
                                                     # or we don not have a new rock to add  then we exit the loop
        last_call = x, y #we save it in order we had a False,False after preforming the function
        x, y = Sand_direction((last_call)) #the new sand I will have after this will be checked by while and reused if the while is true
    added_rocks.add(last_call)#we add this rock to the rocks set
    Unites += 1  # if we exit the while then we have a rock that went to rest and we add one


print('Unites: ', Unites -1)#last rock that will go out > max_y and break the loop will add unit but because it has no rest we substracted it


####part 02
def Sand_direction(position):
    x, y = position #starting sand in this function
    # first we check down
    #y += 1
    if (x,y+1) not in Cave:
        return (x, y+1)
    # we check left
    if (x-1,y+1) not in Cave:
        return (x-1, y+1)
    # we check right
    if (x+1, y+1) not in Cave:
        return (x+1,y+1) #we return when the sand have a place in this position or others in previous
    return (False,False) # comes to rest when all the previous are blocked

Unites = 0
while last_call != (500,0):
    x,y = 500, 0
    while y < Limitation +2 and (x,y) != (False,False): # we go in this while until we are out of limitation
                                                     # or we don not have a new rock to add  then we exit the loop
        last_call = x, y #we save it in order we had a False,False after preforming the function
        x, y = Sand_direction((last_call)) #the new sand I will have after this will be checked by while and reused if the while is true
    Cave.add(last_call)#we add this rock to the rocks set
    Unites += 1  # if we exit the while then we have a rock that went to rest and we add one
print('Unites for part 2:', Unites)

if __name__ == "__main__":
    main()
