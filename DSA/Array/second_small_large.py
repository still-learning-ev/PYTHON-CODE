from min_max import Input

def find_second_min():
    obj = Input()
    arr = obj.get_input()
    minimun = min(arr)
    arr.sort()
    for i in arr:
        if minimun < i:
            print(i)
            return i

def find_second_max():
    obj = Input()
    arr = obj.get_input()
    arr.sort()
    maximum = arr[-1]
    for i in reversed(arr):
        if maximum > i:
            print(i)
            return i



if __name__ == "__main__":
    find_second_min()
    find_second_max()