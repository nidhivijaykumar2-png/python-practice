n1 = int(input("enter 1 : "))
n2 = int(input("enter 2 : "))
gcd = 1
for i in range(1, min(n1,n2)+1):
    if n1 % i == 0 and n2 % i ==0:
        gcd = i
print(gcd)
        
