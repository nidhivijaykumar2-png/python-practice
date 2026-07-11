n = list(map(int,input().split()))
target = int(input("enter the number : "))
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] + n[j] == target:
          print(n[i],n[j])