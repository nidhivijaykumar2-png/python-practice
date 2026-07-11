import random
import string

length = int(input("enter the password length: "))

chara = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(chara)

print("Generated password: ", password)    

if length < 8:
    print("weak password") 
elif length < 12:
    print("medium password")
else:
    print("strong password")        