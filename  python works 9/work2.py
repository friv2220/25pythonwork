def complereTRiples(a, b):
    alice = bob = 0
    for i in range(3):
        if alice[i]>bob[i]:
            alice+=1
        elif alice[i]<bob[i]:
            bob+=1
    return alice, bob



