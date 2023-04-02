from min_max import Input
class Config:
    def __init__(self) -> None:
        self.obj = Input()
        self.arr = self.obj.get_input()
class ApproachOne:
    def find_second_min(self):
        arr = Config().arr
        minimun = min(arr)
        arr.sort()
        for i in arr:
            if minimun < i:
                print(i)
                return i

    def find_second_max(self):
        arr = Config().arr
        arr.sort()
        maximum = arr[-1]
        for i in reversed(arr):
            if maximum > i:
                print(i)
                return i

class ApproachTwo:
    def __init__(self) -> None:
        self.arr = Config().arr
        self.large = float('-inf')
        self.second_large = float('inf')
        self.small = float('inf')
        self.second_small = float('inf')

    def find_second_min(self):
        for i in self.arr:
            if i > self.large:
                self.second_large = self.large
                self.large = i
            elif i > self.second_large and i != self.large:
                self.second_large = i

        print(self.second_large)
        return self.second_large
    
    def find_second_max(self):
        for i in self.arr:
            if i < self.small:
                self.second_small = self.small
                self.small = i
            elif i < self.second_small and i != self.small:
                self.second_small = i

        print(self.second_small)
        return self.second_small
                
        




if __name__ == "__main__":
    approach_one = ApproachOne()
    approach_two = ApproachTwo()
    approach_two.find_second_min()
    approach_two.find_second_max()