# def multiply(x, y):
#     return x * y

# def get_input(prompt):
#     user_val = input(prompt)
#     # Check if the input is a valid integer
#     if user_val.lstrip('-').isdigit():
#         return int(user_val)
#     return user_val

# # Get inputs using a helper to handle type conversion
# num1 = get_input("Enter 1st number or string: ")
# num2 = get_input("Enter 2nd number or string: ")

# try:
#     result = multiply(num1, num2)
#     print(f"\nMultiplication of {num1} & {num2}: {result}")
# except TypeError:
#     print("\nError: You cannot multiply two strings together.")




def multiply(x, y):
    return x * y

# Get inputs as strings first
val1 = input("Enter 1st value: ")
val2 = input("Enter 2nd value: ")

# Try to convert them to numbers; if it fails, keep them as strings
try:
    num1 = int(val1)
except ValueError:
    num1 = val1

try:
    num2 = int(val2)
except ValueError:
    num2 = val2

# Note: Python can do (int * int) or (string * int), 
# but (string * string) will still throw an error.
print(f"\nResult of {num1} & {num2}: {multiply(num1, num2)}")
