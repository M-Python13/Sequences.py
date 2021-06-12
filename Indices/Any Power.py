#number x number several times
def any_power():
    start = int(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    power = int(input("The power you want is..."))
    counter = 0
    print(start)
    while counter < terms:
        start = start ** power
        print(start) 
        counter += 1

any_power()
