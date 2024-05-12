def plusMinus(arr):
    pus = neg = zero = 0
    for i in range(n):
        if arr[i]>0:
            pus+=1
        elif arr[i]<0:
            neg+=1
        else:
            zero+=1
    print(pus/n)
    print(neg/n)
    print(zero/n)