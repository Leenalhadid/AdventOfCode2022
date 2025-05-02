def main():
    with open("input.txt", "rt") as inputString:
        inputList = inputString.readlines()
    
    variables = {}
    statements = {}
    
    for command in inputList:
        if len(command.split()) > 2: #because if we do't have a value then after spliting we will have more than 2 index(positions)
            statements.update({command.strip().split(':')[0]: command.strip().split(':')[1]})#if it has no value we add it to the statement dict
            #where the [0] is the key and [1] is the value
        else:
            variables.update({command.strip().split(':')[0]: int(command.strip().split(':')[1])})# if it has a values we add it to the variable dict
            #while the key is the ame and the value is the value of this variable
    
    while variables.get('root') is None: # to check if we had the root values after each loop on all the statements keys and values
        for var in statements: # it will take key by key
            if statements.get(var) == '* * *':#in order not to loop over them again if we did not find the root
                continue
            var1 = statements.get(var).split()[0] #the value of the key will be splited to two var and on operation
            op = statements.get(var).split()[1]
            var2 = statements.get(var).split()[2]
            if (variables.get(var1) is not None) and (variables.get(var2) is not None): #to check if the variables shaping the key have values
                #then they should be both in the variable dic if not both of them there then we will go to the next key in the statement dic
                if op == '+': #if the two values of the key are in the variables dict
                    #we will look to the operation and extract the value of the key
                    value = variables.get(var1) + variables.get(var2)
                elif op == '-':
                    value = variables.get(var1) - variables.get(var2)
                elif op == '*':
                    value = variables.get(var1) * variables.get(var2)
                else:
                    value = variables.get(var1) // variables.get(var2)
                variables.update({var: value}) # if we calculated a new value for a key in the statement dict then we will added to the variable dict and change it to *** in the main dict
                statements[var] = '* * *' # we changed the value of this key after we found it real value and transformed it to the vraiable dict
                #to change the key named var in the statement dict and replace it
    
    print(variables.get('root')) #it will execute this when the while loop will check the variable dict and find the key root with a real value
    
    
    #########part 02
    with open("E:\\input21S.txt", "rt") as inputFile:
        inputList = inputFile.readlines()
    
    v = 0
    
    while True:
    
        variables = {}
        statements = {}
    
        for command in inputList:
            if len(command.split()) > 2:
                if command.strip().split(':')[0] == 'root':
                    left = command.strip().split(':')[1].split()[0]#we put them in variables because they may differe over the input
                    right = command.strip().split(':')[1].split()[2]#so the left and right will be equal to values we already have later
                    # in the variable dict after we find the root so we search for them using left and right variables names
                statements.update({command.strip().split(':')[0]: command.strip().split(':')[1]})
                # after we saved the left and right we put the root as normal key in the statement dict
                # to execute the for loop on it and find its new value again
            else:
                if command.strip().split(':')[0] == 'humn':
                    variables.update({command.strip().split(':')[0]: v})
                    # we assigned the v value that we have after the last itteration we did and the last root value that we found
                else:
                    variables.update({command.strip().split(':')[0]: int(command.strip().split(':')[1])})
    
        while variables.get('root') is None: #while we do not have the root in the variable dict
            for var in statements:
                var1 = statements.get(var).split()[0]
                op = statements.get(var).split()[1]
                var2 = statements.get(var).split()[2]
                if (variables.get(var1) is not None) and (variables.get(var2) is not None):
                    if op == '+':
                        value = variables.get(var1) + variables.get(var2)
                    elif op == '-':
                        value = variables.get(var1) - variables.get(var2)
                    elif op == '*':
                        value = variables.get(var1) * variables.get(var2)
                    else:
                        value = variables.get(var1) // variables.get(var2)
                    variables.update({var: value})
                    statements[var] = '* * *'
        if variables.get(left) == variables.get(right):#this will be checked after we find the root value and we will then check
    # the left and right what values they have if they reached the same value then we preake and return the v that made us reach this
            break
        else:
            v += 1 #it is gonna change the value of humn by one each time till it reach the right value for the humn
    print('right v =', v)

if __name__ == "__main__":
    main()
