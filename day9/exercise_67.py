# Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.

def binarySearch(lst, item):
    first = 0
    last = len(lst) - 1
    
    while first <= last:
        center = round((first + last) / 2)
        
        if lst[center] == item:
            return center
        elif lst[center] > item:
            last = center - 1
        else:
            first = center + 1
    return 'Not found!'

result = binarySearch(list(range(0, 10)), 5)
print(result)
