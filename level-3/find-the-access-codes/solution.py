def solution(l):
    count = 0
    counts = [0] * len(l)
    
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                counts[i] += 1
                count += counts[j]
    
    return count
