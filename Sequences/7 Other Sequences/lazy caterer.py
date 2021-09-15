#The Lazy Caterer's Sequence
def lazyc():
    n = int(input("How many cuts do you have?"))
    n = (n * ( n + 1)) // 2 + 1
    print(n)

lazyc()
