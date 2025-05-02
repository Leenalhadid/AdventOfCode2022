def main():
    with open('input.txt', 'rt') as inputString :
        inputList = inputString.read().splitlines()
    
    def sections_assignment(x):
        a = 0
        b = 0
        for i in x:
           st = i.split(',') #splitting the string into two paires each as string
           l = list() # a list to append each one pair as list
           for i in st:
               sp = i.split('-') #splitiing the number of each pair into a list of two elements
               l.append(sp)
           z = l[0]
           j = l[1]  #if the range of the z in smaller than j in the start and bigger at the end then j will be includded in z
                     #if the range of the j is smaller than z from the start and bigeer at the end then z is included in j
           if (int(z[0]) <= int(j[0]) and int(z[1]) >= int(j[1]) or int(j[0]) <= int(z[0]) and int(j[1]) >= int(z[1])):
               a += 1
               #if it is not all included then one of the ends of one range should be smaller than the start of the other one
               # or the other way around
               #which indicades that there is an intersection between the two ranges representing the pairs
           if not (int(z[1]) < int(j[0]) or int(j[1]) < int(z[0])):
               b += 1 #for part 2
    
        return a ,b
    
    print(sections_assignment(inputList))

if __name__ == "__main__":
    main()
