# def firstmethod():
#     secondmethod()
#     print("First method is called")
# def secondmethod():
#     thirdmethod()
#     print("Second method is called")
# def thirdmethod():
#     fourthmethod()
#     print("Third method is called")
# def fourthmethod():
#     print("Fourth method is called")

# print(firstmethod())
# n=int(input("Enter the size of n"))
def recursivemethod(n):
    if n<1:
        print("n is less than 1")
    else:
        recursivemethod(n-1)
        print(n)
        
recursivemethod(5)
