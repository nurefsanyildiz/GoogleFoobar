def solution(m,f):
    m, f = int(m), int(f)
    count=0
    while m>=1 and f>=1:
        if m == f: 
            return "impossible"
        if min(m,f) == 1:
            count += max(m,f)-1
            return str(count)
        if m>f:
            count += m // f
            m %= f
        else:
            count += f // m
            f %= m  
    return "impossible" 
