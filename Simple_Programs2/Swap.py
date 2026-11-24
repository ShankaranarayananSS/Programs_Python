#Swap Two Numbers

n1 = int(input("Enter number-1:"))
n2 = int(input("Enter number-2:"))

print(f"Before Swap: {n1} and {n2}")
temp = n1
n1 = n2
n2 = temp
print(f"After Swap: {n1} and {n2}")
