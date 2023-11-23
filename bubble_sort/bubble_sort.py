def bubble_sort(arr):
    # get the length of the list
    n = len(arr)
    # iterate through the list
    for i in range(n):
        switched = False
        # iterate through the list from 0 to n-i-1
        for j in range(n-i-1):
            # check if the element at position j is greater than the element at position j+1
            if arr[j] > arr[j+1]:
                # swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # set switched to True
                switched = True
        # if switched is False, then break out of the loop
        if not switched:
            break
    # return the sorted list
    return arr
# Testing the function with a list of integers
print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1]))
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
