def multiply():
    start = float(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    multiplier = float(input("Number you want to multiply by:"))
    counter = 0
    print(start)
    while counter < terms:
            start *= multiplier
            print(start) 
            counter += 1

multiply()