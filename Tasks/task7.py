#conversion from celcius to farenheit
def celcius(conversion1):
    conversion1 = int((conversion1*1.8) + 32)
    return(conversion1)
        
celcius(32)

#conversion from farenhight to degrees
def farenheit(conversion2):
    conversion2 = int(((conversion2-32)*5)/9)
    return(conversion2,)
farenheit(100)