print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child thickets are $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
