def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
    print(arr)

arr = list(map(int,input().split()))
BubbleSort(arr)