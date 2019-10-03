def fin(x, big):
    cond = True
    for m in range (2,x+1):
        
        if big % m != 0:
            cond = False
            break
    return cond


def chug(x):
    
    if x == 0:
        print(0)
        
    elif x == 1:
        print (1)
        
    else:

        co = False 
        end = 2 
        while co == False:
            if fin(x, end) == True:
                break
            else:
                end += 1
        print (end)
    
def main():
    inp = int(input(""))
    
    inp_arr = []
    
    for foo in range(inp):
        
        inp_2 = int(input(""))
        
        inp_arr.append(inp_2)
        
    for g in inp_arr:
        
        chug(g)
        
main()
