import random
import string
str = string.ascii_letters + string.digits + string.punctuation
size = 8
password = ""
for i in range(size):
  password +=random.choice(str)
print("Generated Password is : ",password)