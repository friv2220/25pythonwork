def digonalDifferens(arr):
    leftdiag = rightdiag = 0:
        for i in range(n):
            leftdiag = arr[i][i]
            rightdiag = arr[i][n-1-i]
        return leftdiag - rightdiag