#number x number
def square():
    start = int(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    counter = 0
    print(start)
    while counter < terms:
            start = start * start
            print(start) 
            counter+= 1
square()