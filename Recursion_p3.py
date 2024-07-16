#to find fibonacci

def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

list=[]       
def fib_list(len):
    for i in range(1,len+1):
        list.append(fibonacci(i))
    return list

print(fib_list(10))
print(fibonacci(10))