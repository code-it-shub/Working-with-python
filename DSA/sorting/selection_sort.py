def SelectionSort(arr):
    i=0
    for i in range(0,len(arr)):
        j=arr.index(min(arr[i:len(arr)]))
        print(j)
        if arr[j] < arr[i]:         
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    print(arr)

arr=[5,4,6,2,3,1]

SelectionSort(arr)
