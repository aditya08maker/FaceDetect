def print_n_natural_numbers():                                              # prints natural numbers till n and replaces even numbers with 0
    while True:
        try:
            n = int(input("Enter a positive integer value for n: "))        # asks user for the value of n repeteadly if invalid
            if len(n) != 1:
                raise ValueError
        except(ValueError, TypeError):
            print("ERROR! INVALID INPUT! TRY AGAIN!")
        finally:
            break
    for natural_numbers in range(1, n+1):
        if natural_numbers % 2 == 0:                                        # prints 0 if mod of natural_numbers is 0
            print("0")
        else:
            print(natural_numbers)