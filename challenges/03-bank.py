print("Welcome to Chase bank.")
print("Have a nice day!")

finished = 'yes'
balance = 0
def bank():
global finished
global balance
  while (finished != "yes"):
    ans = input("What would you like to do? (deposit, withdrawl, check_balance\n")

    if (ans == "deposit"):
      amount = int(input("How much would you like to deposit?\n"))
      balance = balance + amount
      print(f"Your current balance is {balance}\n")
      finished = input("Are you done?\n")
    elif (ans == "withdraw"):
      amount = int(input("How much would you like to withdraw?\n"))
      balance = balance - amount
      print(f"Your current balance is {balance}\n")
      finished = input("Are you done?\n")
    elif (ans == "balance"):
      print(f"Your current balance is {balance}\n")
      finished = input("Are you finished?\n")
      
bank()