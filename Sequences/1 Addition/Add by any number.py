
def add():
    start = float(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    number = float(input("You want to add by..."))
    counter = 0
    print(start)
    while counter < terms:
            start += number
            print(start) 
            counter+= 1

add()