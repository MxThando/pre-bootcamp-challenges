def conversion_from_celcius_to_farenheit(conversion):
    conversion = int((conversion*1.8) + 32)
    return conversion

def conversion_from_farenheit_to_calcius(conversion):
    conversion = int(((conversion-32)*5)/9)
    return conversion
if __name__ == '__main__':
    print(conversion_from_celcius_to_farenheit(32))
    print(conversion_from_farenheit_to_calcius(100))
