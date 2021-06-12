def sub_two():
    start = int(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    counter = 0
    print(start)
    while counter < terms:
            start -= 2
            print(start) 
            counter += 1

sub_two()
