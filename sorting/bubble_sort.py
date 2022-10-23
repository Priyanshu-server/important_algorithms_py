class Array(object):
    def __init__(self,arr):
        self.arr = arr
        self.length = len(arr)

    def show(self):
        print(*self.arr)

    def bubble_sort(self):
        for step in range(self.length-1):
            swapped = False
            for i in range(0,self.length-step-1):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i],self.arr[i+1] = self.arr[i+1],self.arr[i]
                    swapped = True
            if not swapped:
                break
        self.show()



array = Array([3,4,2,5,1])
array.bubble_sort()