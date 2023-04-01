def solution(n, b):
    id_list=[]
    k = len(str(n))
    while True :
        x = "".join(sorted(str(n), reverse=True)) 
        y = "".join(sorted(str(n)))
        z = subtract(x, y, b)        
        z_len = len(str(z))   
        if z_len != k:
            z= str(z)
            z = z.zfill(k)
        n = z    
        if n in id_list:
            index= id_list.index(n)
            lastindex= len(id_list)-1
            length_of_iteration= lastindex - index + 1
            return length_of_iteration
            break
        id_list.append(n)    
        
def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10;
 
def toDeci(str,base):
    llen = len(str)
    power = 1 
    num = 0     
    for i in range(llen - 1, -1, -1):
        if val(str[i]) >= base:
            print('Invalid Number')
            return -1
        num += val(str[i]) * power
        power = power * base
    return num

def reVal(num): 
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))
 
def toBase(res, base, inputNum): 
    while (inputNum > 0):
        res+= reVal(inputNum % base)
        inputNum = int(inputNum / base)
    res = res[::-1] 
    return res
  
def subtract(num1,num2,base):
  sub_result = 0    
  if base==10:
    sub_result = int(num1) - int(num2)
  else:
    num1D = toDeci(num1,base)
    num2D = toDeci(num2,base)
    resultD = num1D - num2D
    sub_result = toBase("",base,resultD)  
  return sub_result 
