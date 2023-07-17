def mergSorting(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        mergSorting(left_arr)
        mergSorting(right_arr)

        i=0
        j=0
        k=0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] > right_arr[j]:
                arr[k] = right_arr[j]
                j+=1
            else:
                arr[k]= left_arr[i]
                i+=1
            k+=1
        while i<len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]= right_arr[j]
            j+=1
            k+=1
    return arr

arr =[5,3,2,6,7,1,4]

print(mergSorting(arr))
