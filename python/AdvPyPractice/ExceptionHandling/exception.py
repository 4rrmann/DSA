x = input("enter num1: ")
y = input("enter num2: ")

try:
    # z = x / int(y)
    z = int(x) / int(y)

except ZeroDivisionError as e:
    print("\nDivision by zero exception")
    z = None

# except Exception as e:
#     print("exception type: ", type(e).__name__)
except TypeError as e:
    print("\nType error exception")
    z = None

print("Division is:", z)