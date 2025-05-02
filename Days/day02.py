def main():
    with open('input.txt', 'rt') as inputString:
        inputList = inputString.read().splitlines()
    
    #you = {'X':1, 'Y':2, 'Z':3}
    
    sums = 0 #the score by following the strategy guid
    for i in inputList:
        if i == 'A X':
            sums += 4
        if i == 'A Y':
            sums += 8
        if i == 'A Z':
            sums += 3
        if i == 'B X':
            sums += 1
        if i == 'B Y':
            sums += 5
        if i == 'B Z':
            sums += 9
        if i == 'C X':
            sums += 7
        if i == 'C Y':
            sums += 2
        if i == 'C Z':
            sums += 6
    
    print(sums)
    
    #####part  02
    
    #manually I callculated
    #losing (x) will add 0 and if it takes to lose (A =1, B=2, c=3)
    #drawing (y) will add 3 and if it takes to draw (A =1, B=2, c=3)
    #winning (z) will add 6 and if it takes to draw (A =1, B=2, c=3) but u are the opponent to lose so instead of the second colum
    #u should chose the thing that should lose in front of the first colum
    
    sums = 0
    for i in inputList:
        if i == 'A X': #x = 0 lossing and the one who lose with rock is sec c = 3 => 0+3 = 3
            sums += 3
        if i == 'A Y':# y = 3 drawing and the one who draws with roc is rock A = 1 => 3+1 =4
            sums += 4
        if i == 'A Z':# z = 6 winning and the one who winnes the rock is th paper and B=2 => 6+2 =8
            sums += 8
        if i == 'B X':
            sums += 1
        if i == 'B Y':
            sums += 5
        if i == 'B Z':
            sums += 9
        if i == 'C X':
            sums += 2
        if i == 'C Y':
            sums += 6
        if i == 'C Z':
            sums += 7
    
    print(sums)

if __name__ == "__main__":
    main()
