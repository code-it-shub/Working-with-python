def InsertionSort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j]< arr[j-1] and j>0:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j=j-1
    print(arr)

arr= list(map(int,input().split()))
InsertionSort(arr)
