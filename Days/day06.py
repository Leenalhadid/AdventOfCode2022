def main():
    # part01
    
    from collections import Counter
    
    with open('input.txt', 'rt') as inputString :
        inputList = inputString.read()
        p=[] #containes every letter as a string in the list
        for i in inputList:
            p.append(i)
    
    
    def markers(x):
        l = list()
        v = list()
        t = list()
        for i in range(len(x)-3): # to shift the range one by one
            l, t = [], []
            for j in range(i,i+4): #it will always start from the next j in a range of three
                l.append(x[j])
                if len(l) == 4:
                    a = Counter(l) #it will give the element and how many times it is appering as a dict with key and value
            for k,h in a.items(): #it will loop over every key and value in the dict we did in the previous step
                 if h == 1: # if it was appering once it will append it (it will check the value)
                      t.append(h)
                      if len(t) == 4: #if we reached four different letters (they have value of one as apperence)
                          v.append(j+1) #then we will return the value of the position that was found after those four different latters
                          break
            else:
                continue
            break
        return v
    
    print(markers(p))
    
    
    def markers_14(x):
        l = list()
        v = list()
        t = list()
        for i in range(len(x)-3):
            l, t = [], []
            for j in range(i,i+14):
                l.append(x[j])
                if len(l) == 14:
                    a = Counter(l)
            for k,h in a.items():
                 if h == 1:
                      t.append(h)
                      if len(t) == 14:
                          v.append(j+1)
                          break
            else:
                continue
            break
        return v
    
    print(markers_14(p))

if __name__ == "__main__":
    main()
