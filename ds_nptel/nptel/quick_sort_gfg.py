def partition(arr, low, high):
    i = low-1
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j],arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

    return arr

print(quicksort([54,98,22,53,65,89,11],0,len([54,98,22,53,65,89,11])-1))

