import re

def get_braille(code):
    braille_lib = ["000000", "100000", "110000", "100100", "100110", "100010", "110100", "110110", "110010", "010100", "010110", "101000", "111000", "101100", "101110", "101010", "111100", "111110", "111010", "011100", "011110", "101001", "111001", "010111", "101101", "101111", "101011"]
    capitalize = "000001"
    
    def find_index(code):
        ascii_codes = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for index, letter in enumerate(ascii_codes):
            if letter == code:
                return index

    if re.findall("[a-z\s]", code):
        i = find_index(code)
        return braille_lib[i]
    elif re.findall("[A-Z]", code):
        i = find_index(code.lower())
        return capitalize + braille_lib[i]
    else:
        return braille_lib[0]

def get_target_date(ascii_code):
    output = ''
    for i, letter in enumerate(ascii_code):
        output += get_braille(letter)
        if i == (len(ascii_code) - 1) or i == 54:
            break
    return output

def solution(ascii_code):
    return get_target_date(ascii_code)
 
