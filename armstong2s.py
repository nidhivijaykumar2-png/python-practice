n = int(input("enter : "))
digits = str(n)
power = len(digits)
total = 0
for i in digits:
    total = total + int(i) ** power
if total == n:
    print("Armstorng")
else:
    print("Not armstrong")        