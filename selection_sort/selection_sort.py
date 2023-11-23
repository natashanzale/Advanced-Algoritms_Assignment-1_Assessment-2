def selection_sort(arr):
    n = len(arr) # Get the number of elements in the array
    for i in range(n - 1): #Outer loop for iterating through each element
        min_index = i #Assume the current index is the minimum
        for j in range(i + 1, n): #Inner loop to find the minimum element in the unsorted portion
            if arr[j] < arr[min_index]: #Compare with the current minimum
                min_index = j #Update the index of the minimum element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Testing the function with a list of integers
print(selection_sort([1, 2, 3, 4, 5, 6]))
print(selection_sort([5, 4, 3, 2, 1, 6]))
arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))