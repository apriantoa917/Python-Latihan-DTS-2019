# 4.1.3.10 LAB: Converting fuel consumption

# mpg = mile per gallons -> m/g

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres.


def l100kmtompg(liters):
    mile = 100_000 / 1609.344
    gallon = liters / 3.785411784
    mpg = mile / gallon
    return mpg

def mpgtol100km(miles):
    meters = 1609.344 * miles 
    liters =  3.785411784
    l100km = liters / meters * 100_000
    return l100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))