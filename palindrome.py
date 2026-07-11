n = int(input("enter : "))
num = list(map(int,input().split()))
rev = num[::-1]
print(rev)
if num == rev:
    print("Palindrome")
else:
    print("Not palidrome")    


