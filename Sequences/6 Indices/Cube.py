#number x number x number
def cube():
    start = float(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    counter = 0
    print(start)
    while counter < terms:
            start = start * start * start
            print(start) 
            counter += 1

cube()