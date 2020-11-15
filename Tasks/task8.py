def task8(number):

    hour = number // 60 

    minute = number % 60

    if hour < 1:
        print(f"{minute} minutes")
    elif hour == 1:
        print(hour , f"hour and {minute} minutes")
    else:
        print(hour , f"hours and {minute} minutes")
task8(133)