def divide():
    start = int(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    multiplier = int(input("Number you want to multiply by:"))
    counter = 0
    print(start)
    while counter < terms:
            start /= multiplier
            print(start) 
            counter += 1

divide()