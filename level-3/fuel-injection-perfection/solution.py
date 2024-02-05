def priority(num):
    return (num & 1 == 0) + (num & 1 == 0 and (num >> 1) & 1 == 0) + ((num == 2) * 3)

def solution(num):
    pellets = int(num)
    operations = 0

    while pellets > 1:
        current_choice = pellets + 1
        current_priority = priority(current_choice)
        previous_priority = priority(pellets - 1)

        if previous_priority >= current_priority:
            current_choice = pellets - 1
            current_priority = previous_priority

        if pellets & 1 == 0:
            half_priority = priority(pellets >> 1)
            if half_priority >= current_priority:
                current_choice = pellets >> 1

        pellets = current_choice
        operations += 1

    return operations 
