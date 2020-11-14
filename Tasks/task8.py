number = int(input("PLease enter the number you want converted into hours and minutes: ", ))

hour = number // 60 

minute = number % 60

if hour <= 1:
    print(hour , f"hour and {minute} minutes")
else:
    print(hour , f"hours and {minute} minutes")