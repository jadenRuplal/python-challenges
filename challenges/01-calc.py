# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculator():

  
    first = int(input("first number\n"))
    sign = input("What method would you like to use?\n")
    second = int(input("second number\n"))

  signs = {
    "add": first + second,
    "sub": first - decond,
    "multiply": first * second,
    "div": first / second,
  }

  if (sign in signs):
    return signs[sign]

print(calculator())