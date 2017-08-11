def unique_char(text):
    '''check to see if there are repeated characters in text'''
    for char in text:
        try:
            if text.index(char, text.index(char) + 1) != -1:
                print('duplicates found')
                return
        except ValueError:
            pass
    else:
        print('all unique')


unique_char('abcdefghijk')

unique_char('abcd12a')
