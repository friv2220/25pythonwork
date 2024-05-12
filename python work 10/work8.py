def birthdayCakeCandels(arr):
    n = len(arr)
    maxnum = 0
    count = 0
    for i in range(n):
        if arr[i]>maxnum:
            maxnum = arr[i]
            count = 1
        elif arr[i]==maxnum:
            count+=1
    return count