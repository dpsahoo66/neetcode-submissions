class MedianFinder:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr = sorted(self.arr)
        
    #0,1,2,3,4
    def findMedian(self) -> float:
        size=len(self.arr)
        if size%2==0:
            return (self.arr[int((size/2)-1)]+self.arr[int(size/2)])/2
        else:
            return self.arr[size//2]
        
        