def decimal_to_base_string(decimal, base):
    digits = []
    while decimal > 0:
        digits.insert(0, str(decimal % base))
        decimal //= base  # Use integer division to avoid float values
    return ''.join(digits)

def base_string_to_decimal(base_string, base):
    result = 0
    for digit in str(base_string):
        result = base * result + int(digit)
    return result

def base_difference(x, y, base):
    if base == 10:
        return int(x) - int(y)

    decimal_x = base_string_to_decimal(x, base)
    decimal_y = base_string_to_decimal(y, base)
    decimal_difference = decimal_x - decimal_y
    return decimal_to_base_string(decimal_difference, base)

def solution(initial_number, base):
    history = []
    while True:
        sorted_desc = ''.join(sorted(str(initial_number), reverse=True))
        sorted_asc = ''.join(sorted(str(initial_number)))
        difference = base_difference(sorted_desc, sorted_asc, base)

        difference_length = len(str(difference))
        initial_length = len(str(sorted_desc))

        if difference_length != initial_length:
            difference = difference * 10**(initial_length - difference_length)

        if difference in history:
            return history.index(difference) + 1

        history = [difference] + history[:50]  # Limit the length of history to 50 elements
        initial_number = difference

 
