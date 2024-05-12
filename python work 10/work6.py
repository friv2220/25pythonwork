def staircase(n):
    for i in range(1, n+1):
        s = '#' * n
        print(s.rjust(n))
        
        
n=int(input())
staircase(n)