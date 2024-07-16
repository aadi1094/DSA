def palin(x):
    if len(x)<=1:
        return x
    else:
        return x[len(x)-1]+palin(x[0:len(x)-1])
    
print(palin("python"))