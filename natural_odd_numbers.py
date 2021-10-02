def natural_odd_numbers(n):
    # Loop through 1-n
    for i in range(1, n):
        if i % 2 == 0: # If i is divisable by 2 it is even
            print(0) # Print 0
        else: # Else, print i
            print(i)
