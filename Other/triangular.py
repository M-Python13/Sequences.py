#traingular sequence
def trian():
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

trian()
