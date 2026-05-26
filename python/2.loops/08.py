num = int(input("Number: "))

is_prime = True
if num>1:
    for i in range(2, num):
        if (num%i) == 0:
            is_prime = False
            break

print(f"Oh! {num} is prime? \n {is_prime}")