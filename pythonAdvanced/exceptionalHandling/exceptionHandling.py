# 1. handle ZeroDivisionError exception when dividing by zero.
# ---------------------------------------------------------------------------------------

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# try:
#     print(num1/num2)
# except ZeroDivisionError as e:
#     print("Donot try dividing by zero.")
# else:
#     print("numbers divided successfully!")

# ---------------------------------------------------------------------------------------
# 2.ValueError if input is not valid integer

# try: 
#     num1 = int(input("Enter 1st Number: "))
# except ValueError as v:
#     print("Please enter a valid integer.")    
# else:
#     print("Number is successfully entered!")

# ---------------------------------------------------------------------------------------
# 3.FileNotFoundError while opening a file

# try:
#     file = open("abc.txt")
# except FileNotFoundError :
#     print("File doesn't exist.") 
# else:
#     file.close()

# ---------------------------------------------------------------------------------------
# 4. TypeError exception 

# try:
#     num1 = int(input("Enter the 1st number: "))
#     num2 = int(input("Enter the 2nd number: "))
#     s = str(num1)
#     result = num2 + s
# except TypeError :
#     print("The entered values are not integer.")
# else:
#     print("Values are successfully entered!")