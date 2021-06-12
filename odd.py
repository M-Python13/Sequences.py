#odd numbers
def odd():
    upper_bound = int(input("You want all the odd numbers below..."))
    lower_bound = int(input("but above..."))
    while lower_bound <= upper_bound:
        if lower_bound % 2 == 1:
            print(lower_bound)
            lower_bound += 1 
        else:
            lower_bound += 1
            
odd()
