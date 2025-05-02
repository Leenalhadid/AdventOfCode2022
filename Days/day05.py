def main():
    import re
    
    with open('input.txt', 'rt') as inputString:
        inputList = inputString.read()
    
        l = list()
        for i in inputList.splitlines():
            if i.startswith("move"):
                l.append(i)
    
    
    # the first list is empty becaue our stacks start from 1
    l2 = [ [] ,["M", "J","C", "B", "F", "R", "H", "L"], [ "Z","D", "C"], ["H", "J" , "F", "C", "N", "G", "W"],
    ["P", "J", "D", "M", "T", "S","B"],["N", "C", "D", "R", "J"], ["W", "L", "D", "Q", "P", "J", "G", "Z"],
    ["P", "Z", "T", "F", "R","H"], ["L", "V", "M", "G"],["C", "B", "G", "p", "F", "Q", "R","J"]]
    
    
    def moving(x,y):
        for i in x:
           nr = re.split(r'move|[from,to]+', i) # the | is to use different patterns to split
           #the pattern to split the string based on several delimiters the move and the from,to
           nr = list(filter(None, nr)) #When None is used as the first argument to the filter() function,
                                       # all elements that are truthy values (gives True if converted to boolean) are extracted.
                                       #it will remove the empty string
           move = int(nr[0]) #save the value of the strack
           From = int(nr[1]) #save the value of the from strack
           To = int(nr[2]) #save the value
           for z in range(len(l2)): #to find the list that is equal to from to pop from it
               if z == From:
                   for j in range(len(l2)): #to find the list that should append to it
                       if j == To:
                           for k in range(0,move): #to determinw how many ones we should pop
                              a = l2[z].pop() #pop it from the list that is equal to from
                              l2[j].append(a) #append it to the list that is equal to the to
    
        last = "" #to put all the last stacks from each list
        for u in l2: #after changing and appending the new things
            if len(u) != 0: #to check if it was not empty
                last+=(u[-1]) #adding the last element from the list
        return last
    
    print(moving(l,l2))
    
    #####part02
    # working on another list while we changed the first one by empliminting the function on it
    l3 = [ [] ,["M", "J","C", "B", "F", "R", "H", "L"], [ "Z","D", "C"], ["H", "J" , "F", "C", "N", "G", "W"],
    ["P", "J", "D", "M", "T", "S","B"],["N", "C", "D", "R", "J"], ["W", "L", "D", "Q", "P", "J", "G", "Z"],
    ["P", "Z", "T", "F", "R","H"], ["L", "V", "M", "G"],["C", "B", "G", "p", "F", "Q", "R","J"]]
    
    def moving_2(x,y):
        for i in x:
           nr = re.split(r'move|[from,to]+', i) #same as above
           nr = list(filter(None, nr))
           move = int(nr[0])
           From = int(nr[1])
           To = int(nr[2])
           for z in range(len(y)):
               if z == From:
                   for j in range(len(y)):
                       if j == To:
                           for k in range(0,move):
                              a = y[z].pop(len(y[z])-move) # then it will start the removing from the first element we should move in order
                              y[j].append(a)
                              move = move -1 #to change the poping place
    
        last = "" #same as before
        for u in y:
            if len(u) != 0:
                last += (u[-1])
        return last
    
    print(moving_2(l,l3))

if __name__ == "__main__":
    main()
