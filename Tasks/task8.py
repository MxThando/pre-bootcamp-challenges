number = int(input("PLease enter the number you want converted into hours and minutes: ", ))

hour = number // 60

minute = number % 60

print(hour , f"hours and {minute} minutes")