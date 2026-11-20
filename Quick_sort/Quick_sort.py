def quick_Sort(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
def quicksort(arr, low, high):
    if low < high:
        pivot_index =quick_Sort(arr, low, high)

        quicksort(arr, low, pivot_index -1)
        quicksort(arr,pivot_index +1, high)
arr = list(map(int,input("Enter the elements by separating with spaces: ").split()))

quicksort(arr, 0, len(arr) -1)
print("Sorted list: ",arr)