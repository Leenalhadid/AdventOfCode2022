def main():
    with open('input.txt', 'rt') as inputFile:
        inputList = inputFile.readlines()
    
    currentDirectory = [] #to follow our current working path
    allDirectories = {'/': 0} #dictionary to put all the directories sizes
    
    for command in inputList:#will loop over each line of the text
        if command[:4] == '$ cd': #will take the first four positions of the command including the space
            if command[:-1].split(' ')[2] == '..': # we splited based on the spaces so we have the (..) in the second position and we ignored \n by [:-1]
                currentDirectory.pop() #we will remove the last directory was added
            else:
                currentDirectory.append(command[:-1].split(' ')[2]) #else we will append the current cd
        elif command[:4] == "$ ls":
            pass
        elif command[:3] == "dir":
            allDirectories.update({('/'.join(currentDirectory)+'/'+command[:-1].split(' ')[1]): 0})  # init size is 0
            #the key is the joining of the current working dir by '/' that we have it in the list
        else:
            #if it is a file then it should belong to the current all fathers dir
            copyOfCurrentDirectory = currentDirectory.copy()
            #we copied the list of current to loop on it and delete from it without affecting the current one
            while copyOfCurrentDirectory: # if still have items
                key = '/'.join(copyOfCurrentDirectory) # joining the copy dir so we have the full path
                allDirectories[key] += int(command.split(' ')[0]) #the key will be the joined working dir
                #adding the value of the file (which will be in position 0 after spliting by spaces for the command)
                copyOfCurrentDirectory.pop() #deleting the last dir to go backward
    
    size = 0
    for s in allDirectories.values():
        if s <= 100000:
            size += s
    
    print(size)
    
    #part 02
    
    #first searching for the value that we need to delete and then searching for all values that are equal to this condition
    #taking the minimum of those values
    minimum = min( m for m in allDirectories.values() if m >= 30000000 - (70000000 - allDirectories['/']))
    
    print(minimum)

if __name__ == "__main__":
    main()
