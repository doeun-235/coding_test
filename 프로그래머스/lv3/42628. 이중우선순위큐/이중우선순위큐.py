class minmaxheap:
    def __init__(self):
        self.data=[None]
        self.minCand = dict()
    
    def insert(self,item):
        self.data.append(item)
        self.down2top(len(self.data)-1) 
        
    def down2top(self,ind):
        i = ind
        while i > 1 :
            if self.data[i] > self.data[(i//2)]:
                self.data[i], self.data[(i//2)] = self.data[(i//2)], self.data[i]
                i = i//2
            else : break
        if ind//2 in self.minCand.keys():
            del self.minCand[ind//2]
        self.minCand[ind] = self.data[ind]
     
    def popMax(self):
        if len(self.data) == 1: return None
        self.data[-1], self.data[1] = self.data[1], self.data[-1]
        ind = len(self.data)-1
        del self.minCand[ind]
        if ind % 2 == 0 : self.minCand[ind//2] = self.data[ind//2]
        ret = self.data.pop()
        self.top2down(1)
        return ret

    def top2down(self,i):
        left,right = 2*i,(2*i)+1
        largest = i
        if right < len(self.data) :
            largest = right if self.data[left] < self.data[right] else left
            if self.data[largest] <= self.data[i]: largest = i
        elif left < len(self.data) :
            if self.data[left] > self.data[i]: largest = left
        if largest != i :
            self.data[largest], self.data[i] = self.data[i],self.data[largest]
            if largest in self.minCand.keys() : self.minCand[largest] = self.data[largest]        
            self.top2down(largest)
    
    def popMin(self):
        if not self.minCand : return None
        i = min(list(self.minCand.keys()),key=lambda x: self.minCand[x])
        self.data[i], self.data[-1] = self.data[-1], self.data[i]
        del self.minCand[len(self.data)-1]
        if len(self.data)%2==1:
            self.minCand[(len(self.data)-1)//2] = self.data[(len(self.data)-1)//2]
        ret = self.data.pop()
        if i < len(self.data) :
            #self.minCand[i] = self.data[i]
            self.down2top(i)
        return ret

def numeric(string):
    try : return int(string)
    except : return float(string)    

def solution(operations):
    twopriorque = minmaxheap()
    for query in operations:
        print(query)
        if query[0] == 'I':
            item = query.split(' ')[-1]
            twopriorque.insert(numeric(item))
        elif query[2] == '1': print(twopriorque.popMax())
        else :
            print(twopriorque.popMin())
        print(twopriorque.data)
        print(twopriorque.minCand)
    
    queMax = twopriorque.popMax()
    if queMax is not None :
        queMin = twopriorque.popMin()
        return [queMax,queMax] if queMin is None else [queMax,queMin]
    else : return [0,0]