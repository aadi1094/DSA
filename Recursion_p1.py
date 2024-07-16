def powerofTwo(n):
    if n==0:
        return 1
    else:
        power=powerofTwo(n-1)
        return power*2

print(powerofTwo(5))