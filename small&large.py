n = int(input("enter : "))
num = list(map(int,input().split()))
largest = num[0]
smallest = num[0]
for i in num:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print(largest)
print(smallest)            
    