class Input:
    def get_input(self):
        arr_string = input("Enter array space seperated ")
        arr = arr_string.strip().split(" ")
        arr = list(map(int, arr))
        return arr


def find_min_in_array():
    # built in function min(arr)
    obj = Input()
    arr = obj.get_input()
    max = float('-inf')
    for i in arr:
        if max< i:
            max = i
    print(max)


def find_max_in_array():
    obj = Input()
    arr = obj.get_input()
    min = float('inf')
    for i in arr:
        if min > i:
            min = i
    print(min)

if __name__ == "__main__":
    find_min_in_array()
    find_max_in_array()