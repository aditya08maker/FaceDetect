def is_palindrome(string):      # enter a string value while calling the function
    if string == string[::-1]:
        return True             # returns TRUE if the given string IS a palindrome
    else:
        return False            # returns FALSE if the given string IS NOT a palindrome