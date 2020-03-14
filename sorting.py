import random

def quick_sort(data):
    left = 0
    right = len(data) - 1
    output = randomized_quick_sort(data, left, right)
    return output

def randomized_quick_sort(data, left, right):
    if left <= right:
        temp = random.randint(left, right)
        data[left], data[temp] = data[temp], data[left]
        m1, m2 = partition3(data, left, right)
        randomized_quick_sort(data, left, m1-1)
        randomized_quick_sort(data, m2+1, right)
    return data

def partition3(data, left, right):
    pivot = data[left]
    i = m1 = left
    m2 = right
    while i <= m2:
        if data[i] < pivot:
            data[i], data[m1] = data[m1], data[i]
            m1 = m1+1
        elif data[i] > pivot:
            data[i], data[m2] = data[m2], data[i]
            m2 = m2-1
            i = i-1
        i = i+1
    return m1, m2