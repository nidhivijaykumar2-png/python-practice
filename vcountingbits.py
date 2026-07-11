
n = int(input("enter : "))
result = []
for i in range(n+1):
    binary = "{:03b}".format(i)
    result.append(binary.count('1'))
print(result)
    