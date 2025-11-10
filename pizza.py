print("Welcome to Python Pizza Deliveries!")

size = input("\nWhat size pizza do you want? S, M or L: ")
pepperoni = input("\nDo you want pepperoni in your pizza? Y or N: ")
extra_cheese = input("\nDo you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"\nYour final bill is: ${bill}")
print("Enjoy your food...........")