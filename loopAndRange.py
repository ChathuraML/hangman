import random
# total = 0
# for number in range(1,101):
#     total += number

# print(total)

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','^','&','*']
numbers = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the password generator!\n")

lttr = int(input("How many letters would you like in your password?\n"))

symbl = int(input("How many symbols would you like?\n"))

num = int(input("How many numbers would you like?\n"))

password = []

password += random.sample(letters,k=lttr)

password += random.sample(symbols,k=symbl)

password += random.sample(numbers,k=num)

print(password)
your_password = []

your_password += random.sample(password, k=len(password))

final_password = ''.join(your_password)

print(f"You Password is: {final_password}")