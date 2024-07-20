import numpy as np
# #By using list .
n=int(input("Enter the number of days: "))
total=0
temp=[]
for i in range(n):
    element=float(input(f"Enter the temperature for day {i+1}: "))
    temp.append(element)
    total+=temp[i]


avgTemp=np.mean(temp)
print(f"The average temperature for the {n} days is {avgTemp} degrees Celsius.")

above=0
for i in temp:
    if i>avgTemp:
        above+=1
print(f"The number of days with temperature above the average is {above}.")

# #Normal way
# n=int(input("Enter the number of days: "))
# total=0
# for i in range(n):
#     element=float(input(f"Enter the temperature for day {i+1}: "))
#     total+=element

# avgTemp=total/n
# print(f"The average temperature for the {n} days is {avgTemp} degrees Celsius.")

