x = float(input("Enter the amount for the bills: "))
y = float(input("Enter the amount given: "))

if y > x:
    change = y - x
    print(f"Your change is: {change:.2f}")
elif y == x:
    print("Thank you, no tips.")
elif y < x:
    while True:
        y = float(input("Enter again: "))
        if y >= x:
            if y > x:
                change = y - x
                print(f"Your change is: {change:.2f}")
            elif y == x:
                print("Thank you, no tips.")
            break
