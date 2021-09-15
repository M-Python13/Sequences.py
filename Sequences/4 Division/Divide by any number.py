def divide():
    start = float(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    divider = float(input("Number you want to divide by:"))
    counter = 0
    print(start)
    while counter < terms:
            start /= divider
            print(start) 
            counter += 1

divide()