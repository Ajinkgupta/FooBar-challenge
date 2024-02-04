from fractions import Fraction

FALSE = [-1, -1]

def solution(pegs):
    sum = 0
    total_distance = pegs[-1] - pegs[0]
    for i in range(2, len(pegs), 2):
        sum += pegs[i] - pegs[i - 1]
    sum *= 2
    rn = total_distance - sum
    numerator = rn * 2
    denominator = 1 if len(pegs) % 2 == 1 else 3
    return FALSE if numerator < denominator else verify(pegs, [numerator, denominator])

def verify(pegs, ret):
    numerator = ret[0]
    for i in range(len(pegs) - 1):
        distance = (pegs[i + 1] - pegs[i]) * ret[1]
        next_numerator = distance - numerator
        if numerator < ret[1]:
            return FALSE
        numerator = next_numerator
    return [ret[0] // ret[1], 1] if ret[0] % ret[1] == 0 else ret

