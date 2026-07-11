n = int(input("enter the number"))
num = list(map(int,input().split()))
countpositive = 0
countnegative = 0
countzero = 0
for i in num:
    if i > 0:
        countpositive = countpositive + 1
    elif i < 0:
        countnegative = countnegative + 1
    else:
        countzero = countzero + 1

print("positive", " = ", countpositive)
print("negative", " = ", countnegative)
print("zero", " = ", countzero)
