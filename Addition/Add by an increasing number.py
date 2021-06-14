# number + another number which increases by 1 each time
def add_inc():
    start = int(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    counter = 0
    number = 1
    print(start)
    while counter < terms:
            start += number
            print(start) 
            counter += 1
            number +=  1

add_inc()
