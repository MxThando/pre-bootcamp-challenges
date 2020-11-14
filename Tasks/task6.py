x = int(input("Please enter your first number: ",))
y = int(input("Please enter your second number: ",))
z = int(input("Please enter your third number: ",))


if x > y and x > z:
    print(x, "is the greatest number")
elif y > z and y > x:
    print(y, "is the greatest number")
elif z > y and z > x:
    print(z, "is the greatest number")



