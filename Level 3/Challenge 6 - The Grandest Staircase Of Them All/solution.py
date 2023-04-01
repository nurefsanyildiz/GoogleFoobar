def solution(n):
    C = [int(s == 0) for s in range(n + 1)] 
    for k in range(1, n):
        C = [C[a] if a - k < 0 else C[a] + C[a - k] for a in range(n + 1)]
    return C[n] 
