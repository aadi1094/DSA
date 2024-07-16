#sum of digits.

def SumofDigit(n):
    if n==0:
        return 0
    return int(n%10)  + SumofDigit(n/10)


print(SumofDigit(43378))