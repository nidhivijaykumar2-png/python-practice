n = int(input("enter the number"))
num = list(map(int,input().split()))

largest = num[0]

for i in num:
    if i > largest:
        largest = i

for i in num:
    if i!= largest:
        secondlargest = i
        break
    
for i in num:
    if i < largest and i > secondlargest:
        secondlargest = i

print(secondlargest)               



