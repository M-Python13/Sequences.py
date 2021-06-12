#even numbers
def even():
    upper_bound = int(input("You want all the even numbers below..."))
    lower_bound = int(input("but above..."))
    while lower_bound <= upper_bound:
        if lower_bound % 2 == 0 :
            print(lower_bound)
            lower_bound += 1 
        else:
            lower_bound += 1
even()
