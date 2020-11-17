def task8(number):

    hour = number // 60 

    minute = number % 60

    if hour < 1:
        print(f"{minute} minutes")
        if minute <= 1:
            print(f"{minute} minute")
    elif hour == 1:
        print(hour , f"hour and {minute} minutes")
        if minute <=1:
            print(hour , f"hour and {minute} minute")
    else:
        print(hour , f"hours and {minute} minutes")
task8(61)