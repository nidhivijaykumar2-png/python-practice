num = int(input("enter : "))
org = num
n = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit ** n
    num = num // 10
if sum == org:
    print("Armstrong")
else:
    print("Not armstrong")        
