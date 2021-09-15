def add_one():
    start = float(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    counter = 0
    print(start)
    while counter < terms:
            start += 1
            print(start) 
            counter+= 1

add_one()

    