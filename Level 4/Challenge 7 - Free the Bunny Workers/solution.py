import numpy
def calculateCombinations(n,r):
    char = tuple(n)
    n = len(char)     
    if r > n:
        return     
    index = numpy.arange(r)         
    yield tuple(char[i] for i in index)     
    while True:         
        for i in reversed(range(r)):
            if index[i] != i + n - r:
                break
        else:
            return         
        index[i] += 1         
        for j in range(i + 1, r):             
            index[j] = index[j-1] + 1             
        yield tuple(char[i] for i in index)

def solution(num_buns, num_required):
    if(1<=num_buns<=9 and 0<=num_required<=9 and num_buns >= num_required):
        keys = [[] for num in range(num_buns)]        
        if(num_buns == num_required):
            keys = [[i] for i in range(num_buns)]         
        elif(num_required == 1):
            keys = [[0] for i in range(num_buns)] 
        elif(num_required == 0):
            keys 
        else:
            for key, bunnies in enumerate(calculateCombinations(range(num_buns),num_buns-(num_required-1))):                      
                for b in bunnies:
                    keys[b].append(key)
        return keys
    else:
        return "Please enter valid values"      
