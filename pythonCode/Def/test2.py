def primeChecker(primeNumber):
    if primeNumber > 1:
        for i in range(2, primeNumber):
            if (primeNumber % i) == 0:
                print(primeNumber, "is not a prime number")
                break
        else:
            print(primeNumber, "is a prime number")
    else:
        print(primeNumber, "is not a prime number")
primeChecker(24)