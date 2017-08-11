def char_checker(text):
    '''check to see if there are repeated characters in text'''
    # Find the number of characters in the given text string
    num_char = len(text)
    # Find the unique characters in the string
    # set(iterable) iterates over the parameter to make a set.
    unique_char = set(text)
    # Find the number of unique characters in the string using
    #  properties of set datatype
    num_unique = len(unique_char)
    # If the total number of elements in the text equals the number of
    # unique elements in the text, then there are no repeated values.
    if num_char == num_unique:
        print('all unique')
    # If the number of elements doesn't match, then there is a character
    # that appears in the text more than once.
    else:
        print('duplicates found')
