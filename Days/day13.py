
def Right_Order_Check(Line1, Line2):
    while True: #the listst are not empty and if one of them is empty or both of them then it will compare the len of them
        if len(Line1) <= 0 or len(Line2) <= 0:
            break
        lhs = Line1.pop(0) #the first elemnt of the firt lest
        rhs = Line2.pop(0) #the first element of the second list then delete them

        if type(lhs) == int and type(rhs) == list:
            Smaller_Value_check = Right_Order_Check(list([lhs]), rhs)
            if Smaller_Value_check != 0:
                return Smaller_Value_check
        elif type(lhs) == int and type(rhs) == int:  #both integers then directly comparing
            if lhs < rhs:
                return 1
            elif lhs > rhs:
                return -1
        elif type(lhs) == list and type(rhs) == list:
            Smaller_Value_check = Right_Order_Check(lhs, rhs)
            if Smaller_Value_check != 0:
                return Smaller_Value_check
        else:
            Smaller_Value_check = Right_Order_Check(lhs, list([rhs]))
            if Smaller_Value_check != 0:
                return Smaller_Value_check
    if len(Line1) < len(Line2):
        return 1
    elif len(Line1) > len(Line2):
        return -1
    else:
        return 0


def main():
    with open("input.txt") as inputString:
        inputList = inputString.read().splitlines()

    index = 1
    indices = []
    listOflists = []
    for i in range(len(inputList)):
        if (i + 1) % 3 != 0:
            listOflists.append(eval(inputList.pop(0)))
        else:
            inputList.pop(0)

    for i in range(0, len(listOflists), 2):
        compareValue = Right_Order_Check(listOflists[i], listOflists[i + 1])
        if compareValue == 1:
            indices.append(index)
        index += 1

    print(sum(indices))

    # part2
    with open("input.txt") as inputFile:
        inputList = inputFile.readlines()
        inputList = [x.strip() for x in inputList]

    lessOfTwo = 0
    lessOfSix = 0
    listOflists = []
    for i in range(len(inputList)):
        if (i + 1) % 3 != 0:
            listOflists.append(eval(inputList.pop(0)))
        else:
            inputList.pop(0)

    for i in range(len(listOflists)):
        if Right_Order_Check(listOflists[i].copy(), [[2]]) == 1:
            lessOfTwo += 1
        if Right_Order_Check(listOflists[i].copy(), [[6]]) == 1:
            lessOfSix += 1

    print((lessOfTwo + 1) * (lessOfSix + 2))

if __name__ == "__main__":
    main()
