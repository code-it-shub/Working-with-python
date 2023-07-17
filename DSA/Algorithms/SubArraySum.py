def SubArraySum(arr,given_sum):
    l=0
    r=0
    current_sum=0
    while True:
        if current_sum == given_sum:
            print(f"from index {l} to index {r}")
            return
        elif current_sum > given_sum :
            current_sum = current_sum - arr[l]
            l=l+1
        else:
            current_sum = current_sum + arr[r]
            r=r+1
        print(l,r)

arr=list(map(int,input().split()))
given_sum = int(input())    
SubArraySum(arr,given_sum)