def celcius_to_farenheit(conversion):
    conversion = int((conversion*1.8) + 32)
    return conversion
        
celcius_to_farenheit(32)

def farenheit_to_calcius(conversion):
    conversion = int(((conversion-32)*5)/9)
    return conversion
farenheit_to_calcius(100)