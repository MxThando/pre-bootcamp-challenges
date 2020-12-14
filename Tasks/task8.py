def task8(number):

    hour = number // 60 

    minute = number % 60

    if hour < 1:
        print(f"{minute} minutes")
    elif hour == 1 and minute == 1:
        print(f"{hour} hour and {minute} minute")
    elif hour == 1 and minute > 1:
        print(f"{hour} hour and {minute} minutes")
    elif hour > 1 and minute ==1:
        print(f"{hour} hours and {minute} minute")
    else:
        print(f"{hour} hours and {minute} minutes")
task8(71)