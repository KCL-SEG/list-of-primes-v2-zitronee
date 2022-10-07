"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if (number_of_primes < 1):
        raise ValueError

    list = []
    x = 2
    isPrime = False
    count = 1


    while count < number_of_primes+1:
        isPrime = True
        for i in range (2, x):
            if (x % i) == 0:
                isPrime = False
                break

        if isPrime:
            list.append(x)
            count +=1

        x+=1

    return list
