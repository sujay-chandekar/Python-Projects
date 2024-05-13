import random
#Generating random number
random_no = random.randint(1, 100)

while 1:
  #Guessing the number
  val = input("Guess The Number OR Quit: ")
  if val == "Quit":
    break
  val = int(val)
  if val == random_no:
    print("----------Right Guess !!!!!----------")
    break
  elif val < random_no:
    print("----------Guess some bigger number----------")
  else:
    print("----------Guess some smaller number----------")
print("----------End Game----------")