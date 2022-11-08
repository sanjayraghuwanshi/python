
def prime_checker(number):
    flag = False
    # prime numbers are greater than 1
    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)