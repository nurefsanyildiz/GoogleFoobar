from decimal import *
def beatty(r,n):
    if n < 1:
        return 0
    else:
        n1= int((r-1)*n)
        result = n*n1 + n*(n+1)/2 - n1*(n1+1)/2 - beatty(r, n1)
        return int(result)
def solution(str_n):
    n = int(str_n)  
    getcontext().prec = 101
    r = Decimal(2).sqrt()
    return str(beatty(r,n))
