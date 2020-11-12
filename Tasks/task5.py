bottom = int(input("insert the bottom length of your triangle: ", ))
height = int(input("insert the height of your triangle: ", ))
hypot = int(input("insert the lenght of the longest side of your triangle: ", ))

sp = 0.5*(bottom + height + hypot)

area = (sp * (sp-bottom) * (sp-height) * (sp-hypot))**0.5

print(f'The area of your triangle is: {area}')
