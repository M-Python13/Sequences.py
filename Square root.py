# number = (number x number) / number 
def square_root():
    import math 
    start = int(input("Starting at?"))
    terms = int(input("Number of terms? (excluding starting number)"))
    counter = 0
    print(start)
    while counter < terms:
        start = math.sqrt(start)
        print(start)  
        counter += 1
    
square_root()