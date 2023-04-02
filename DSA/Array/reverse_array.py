from min_max import Input


def reverse_array_one(arr):
    arr.reverse()
    print(arr)

def reverse_array_two(arr):
    n = len(arr)
    i, j = 0, n-1

    while i < j:
        temp  = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

    print(arr)
if __name__ == "__main__":
    obj = Input() 
    reverse_array_one(obj.get_input())
    reverse_array_two(obj.get_input())