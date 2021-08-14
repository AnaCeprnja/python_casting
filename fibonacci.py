fib = int(input("up to how many terms"))

m1, n2 = 0, 1
count = 0

# is valid?

if nterms <= 0:
    print("please enter a positive integer")

# one term?
elif fib == 1:
    print("fibonacci seqence upto", fib, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < fib:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
