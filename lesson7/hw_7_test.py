def find_gcd(a, b):
    dilniki = []
    dilnik = 1
    while dilnik <= b:
        if a % dilnik == 0 and b % dilnik == 0:
            dilniki.append(dilnik)
            print(dilnik)
        dilnik = dilnik +1
    return dilniki[-1]


print(find_gcd(12, 18))


