password = str(input("enter the password: "))
noc = len(password)

if noc < 6:
    pas = "Weak"
elif noc < 10:
    pas = "Medium"
else:
    pas = "Strong"

print(f"Your password is {pas}")