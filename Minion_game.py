def minion_game(string):
    
    ls = []
    
    # Two variables to store a score
    Stuart = 0   
    Kevin = 0
    
    for i in range(len(string)):
        for j in range(len(string)):
            #print(string[i:j + 1])
            ls.append(string[i:j + 1])
    
    #print(ls)      
    ls = ' '.join(ls).split()
    #print(ls)
    
    for i in range(len(ls)):
        #print(ls[i][0])
        if ls[i][0] in ('A', 'E', 'I', 'O', 'U'):
            Kevin += 1
        elif (ord(ls[i][0]) >= 65 and ord(ls[i][0]) <= 90):
            Stuart += 1
    
    if (Kevin > Stuart):
        print("Kevin", Kevin)
    elif (Kevin < Stuart):
        print("Stuart", Stuart)
    else:
        print("Draw")
            
if __name__ == '__main__':
    s = input()
    minion_game(s)