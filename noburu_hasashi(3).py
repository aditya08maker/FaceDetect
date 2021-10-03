def print_fibonacci_series():                                               # prints fibonacci series till n
    while True:
        try:
            n = int(input("Enter a positive integer value for n: "))        # asks user for the value of n repeteadly if invalid
            if len(n) != 1:
                raise ValueError
        except(ValueError, TypeError):
            print("ERROR! INVALID INPUT! TRY AGAIN!")
        finally:
            break
    print("0")
    first_number, second_number = 0, 1
    while n-1 > 0:                                                            # print fibonacci series
        print(second_number)
        first_number, second_number = second_number, first_number + second_number
        n -= 1