n = int(input("enter the number"))
num = list(map(int,input().split()))
sum = 0
for i in num:
    if i%2==0:
        sum = sum + i
print(sum)