
def rotate(nums,k):
    n=len(nums)
    k%=n

    nums.reverse()

    nums[:k]=reversed(nums[:k])
    nums[k:]=reversed(nums[k:])
    return nums

n=[1,2,3,4,5,6,7]


print(rotate(n,3))
