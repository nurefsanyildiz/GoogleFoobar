import math
def solution(area):
    if(1 <= area <= 1000000):
        solarPanelsList = []
        while(area>=1):
            get_square_root = int(math.sqrt(area))
            get_square = pow(get_square_root,2)
            solarPanelsList.append(get_square)
            area -= get_square  
        return solarPanelsList
    else:
        return "Your area must be between 1 and 1000000"  
