def get_pivot(arr,low,high):
    pivot = arr[high]

    i = low-1

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    i+=1
    arr[i],arr[high] = arr[high],arr[i]

    return i

def quickSort(arr,low,high):
    if low<high:
        pi = get_pivot(arr,low,high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


arr = [5,3,4,1,2]
quickSort(arr,0,len(arr)-1)
print(*arr)