def is_valid_phone(number):
    # if the number is composed of 9 digits
    if len(number) == 9:
        try:
            int(number)
            return True
        except:
            return False

    def is_all_int(list_of_number):
        try:
            for number in list_of_number:
                int(number)
            return True
        except:
            return False
 
    # if the number is composed of 3 groups of digits separated
    # either by spaces, dots or dashes
    if len(number) == 11:
        a = number.split()
        b = number.split('.')
        c = number.split('-')
        if len(a) == 3:
            return is_all_int(a)
        if len(b) == 3:
            return is_all_int(b)
        if len(c) == 3:
            return is_all_int(c)

    return False
