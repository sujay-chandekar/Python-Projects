import random
class bank:
  #account creatation
  def __init__(self):
    print("ENTER AMOUNT YOU WANTED TO STORE IN YOUR ACCOUNT ")
    self.balance = int(input())
    self.acc_no = random.randint(1000000000, 9999999999)
    print(self.acc_no, "THIS IS YOUR ACCOUNT NO")
    pin = int(input("ENTER YOUR GREEN PIN :"))
    self.pin = pin

  def credit(self):
    acc_no = int(input("ENTER YOUR ACCOUNT NO :"))
    pin = int(input("ENTER YOUR PIN : "))
    if (self.acc_no == acc_no and self.pin == pin):
      print("Enter amount you wanted to credit : ")
      self.balance += int(input())
      print("Amount credited succesfully , thank you")
    else:
      print("INVALID CREDENTIALS ")

  #Debit code
  def debit(self):
    acc_no = int(input("ENTER YOUR ACCOUNT NO :"))
    pin = int(input("ENTER YOUR PIN : "))

    if (acc_no != self.acc_no and self.pin != pin):
      print("INVALID CREDENTIALS ")
      return
    print("ENTER AMOUNT THAT YOU WANTED TO WITHDRAW : ")
    amount = int(input())
    if (amount > self.balance):
      print("YOU DON'T HAVE ENOUGH MONEY TO WITHDRAW ")
      return
    self.balance -= amount
    print("MONEY WITHDRAW SUCCESSFULLY :", amount)

  #Cheak balance
  def cheak_bal(self):
    acc_no = int(input("ENTER YOUR ACCOUNT NO :"))
    pin = int(input("ENTER YOUR PIN : "))
    if (self.acc_no == acc_no and self.pin == pin):
      print("YOUR ACCOUNT BALANCE IS : ", self.balance)
    else:
      print("INVALID CREDENTIALS ")

#code
bank_acc = []
cnt = 0
while (1):
  print(
      "Enter 1 To create account \nEnter 2 To credit amount \nEnter 3 to withdraw amount \nEnter 4 to cheak balance \nEnter 5 to exit "
  )
  choice = int(input())
  if choice == 1:
    print("remember your account index ", cnt)
    bank_acc.append(bank())
    cnt += 1
  if choice == 2:
    key = int(input("Enter your account index: "))
    bank_acc[key].credit()
  if choice == 3:
    key = int(input("Enter your account index: "))
    bank_acc[key].debit()
  if choice == 4:
    key = int(input("Enter your account index: "))
    bank_acc[key].cheak_bal()
  if choice == 5:
    break
print("THANK YOUR VISITING")
