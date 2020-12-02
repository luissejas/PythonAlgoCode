def PrimeCalculator(iLower, iUpper):
    for n in range(iLower, iUpper + 1, 1):
        #print("New number")
        for c in range(2, n):
            iResult = n % c
            lCheck.append(iResult)
        if 0 in lCheck:
            lNormal.append(n)
        else:
            lPrimes.append(n)

        lCheck.clear()

if __name__ == '__main__':
    #iLower is the variable to define the lower bound
    #iUpper is the variable to define the upper bound
    #lPrimes is the List of Primes

    lPrimes = list()
    lNormal = list()
    lCheck = list()

    iLower = int(input("Please enter the lower bound of the prime number program!\n"))
    while iLower <= 0:
        iLower = int(input("Invalid number, please insert a number higher than 0 \n"))

    iUpper = int(input("Please enter the upper bound of the prime number program \n"))
    while iUpper <= 0 or iUpper <= iLower:
        iUpper = int(input("Invalid Upper Bound, it is equal or lower than 0 or the Lower Bound. Please try again! \n"))

    print("Your values are " + str(iLower) + " and " + str(iUpper) + ". They are valid inputs, we may proceed!")

    PrimeCalculator(iLower, iUpper)

    print("The prime numbers are :")
    print(lPrimes)
    print("The non-prime numbers are: ")
    print(lNormal)