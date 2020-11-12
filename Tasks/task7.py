print("Degrees celcius to degrees farenheit = 1")
print("Degrees farenheit to degrees celcius = 2")

answer = int(input("Which conversion would you like to do? ", ))

temperature = int(input("Please enter the value of the temperature you want converted: ", ))

conversion1 = int((temperature*1.8) + 32)

conversion2 = int(((temperature-32)*5)/9)

if answer == 1:
    print(conversion1, "Degrees farenheit")
else:
    print(conversion2, "Degrees Celcius")