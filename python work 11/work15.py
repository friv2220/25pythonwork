def birthday(s, d, m):
    count = 0
    total = sum(s:[m])
    
    if total == d:
        count+=1
        
    for i in range(m, len(s)):
        total += s[i]
        total -= s[i-m]
        
        if total == d:
            count+=1
    return count 