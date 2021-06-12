#fibonacci terms
def fibonacci():
    first= 0
    second = 1
    terms = int(input("Number of terms?"))
    n1, n2 = 0, 1
    counter = 0
    if terms <= 0:
        print("Please enter a positive integer")

    elif terms == 1:
        print(n1)

    elif terms == 2:
        print(n1)
        print(n2)
    
    else:
        while counter < terms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            counter += 1
    
fibonacci()




