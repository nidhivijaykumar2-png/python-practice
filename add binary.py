n1 = input("enter : ")
n2 = input("enter : ")
i = len(n1)-1
j = len(n2)-1
carry = 0
result = "" 
while i>=0 or j>=0 or carry:
    d1 = ord(n1[i]) - ord('0') if i>=0 else 0
    d2 = ord(n2[j]) - ord('0') if j>=0 else 0
    total = d1 + d2 + carry
    carry = total // 2
    result = str(total % 2)+ result
    i -= 1
    j -= 1
print(result)    