n = list(map(int,input().split()))
current = n[0]
maximum = n[0]
for i in range(1,len(n)):
    current = max(current + n[i], n[i])
    if current > maximum:
        maximum = current
print(maximum)        