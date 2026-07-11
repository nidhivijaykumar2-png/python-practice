n = int(input("enter the number"))
num = list(map(int,input().split()))
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print(largest)


    
           
   