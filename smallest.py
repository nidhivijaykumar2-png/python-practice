n = int(input("enter the number"))
num = list(map(int,input().split()))
smallest = num[0]
for i in num:
    if i < smallest:
        smallest = i
print(smallest)