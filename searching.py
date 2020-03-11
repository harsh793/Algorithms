def linear_search(data, key):
    for i in range(len(data)):
        if key == data[i]:
            return i
    return "Not Found."

def binary_search(data, key):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low+high)//2
        if data[mid] == key:
            return mid
        elif key < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "Not Found."