# Binary Search returning the index where the item should be inserted if not found
def binarySearch(arr, value):
    s, e = 0, len(arr)-1
    found = False
    while (s <= e):  # if we do s<e we will not be able to search in 1 item array
        m = (s + e) // 2  # same as m = s + (e - s) // 2
        if arr[m] == value:
            found = True
            return (m, found)
        elif arr[m] > value:
            e = m-1
        else:
            s = m+1
    # s > e : so s containing the bigger item
    # the index where the value should be inserted contains the next bigger value
    return (s, found)
