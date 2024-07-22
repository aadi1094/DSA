
def sum(arr):
    sum=0
    result=[]
    for i in arr:
        sum+=i
        result.append(sum)
    return result

arr = [1,2,3,4]
print(sum(arr))

