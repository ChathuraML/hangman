print("Hello World!")

print("Wellcome to the Roller House")

height = int(input("#What is your height(CM) ? \n"))


if height >= 120 :
    print("Wooohoooo....You can have a ride!!!!!!!!!!!!!!")
    age = int(input("#What is your Age ? \n"))

    bill =0
    if age < 12:
        bill = 5
        print("Chiled tickets are $5")
    elif age >= 18:
         bill = 12
         print("Adult tickets are $12")
    else:
        bill=7
        print("Youth tickets are $7")


    photo = input("#Do you wanna photo ?(y/n) \n")

    if photo == "y":
        bill += 3
    
        
    print(f"Your total bill is ${bill}")
else:
    print("Sorry darling...., You cant have a ride!!!!!!!!!!!!!!")