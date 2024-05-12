def minMaxSum(arr):
    s = 0
    minum = 999999999
    maxnum = 0
    n = len(arr)
    for i in range(n):
        s += arr[i]
        minum = min(minum, arr[i])
        maxnum = max(maxnum, arr[i])
    print(s-minum, s-maxnum)