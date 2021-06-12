#prime numbers
def prime():
    import math
    upper_bound = int(input("You want to find all the prime numbers below..."))
    for num in range(2,upper_bound):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            print(num)

prime()
