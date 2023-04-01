def solution(s):
    chars = ["<",">","-"]
    count = 0
    a = 0    
    for char in s: 
        if char not in chars:
            return "s must contain only < > - characters"
    if(1 <= len(s) <=100):
        for char in s[a : :]: 
            if(char == ">"): 
                for char in s[a+1 : :]:
                    if(char == "<"):
                        count += 1
            a+=1               
        return count*2          
    else: 
        return "length of string should be between 1 and 100" 
