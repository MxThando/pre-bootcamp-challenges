x = int(input("Please enter your first number: ",))
y = int(input("Please enter your second number: ",))
z = int(input("Please enter your third number: ",))



response = [x, y, z]

sorted_response = sorted(response, reverse = True )

print("The highest number is:", sorted_response[0])


