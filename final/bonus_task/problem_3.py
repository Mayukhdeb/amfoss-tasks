
def isfactor(num, suspect):
    if num% suspect == 0 :
        return True 
    else:
        return False 
    
def prime_or_not(x):
    prime = False 
    
    if x > 2 :
        for m in range (2,x):
            if x % m == 0:
                prime = False 
                break

            else:
                prime = True
                
    else:
        prime = True
            
    return prime 
            
def check(foo):
    
  
    for x in range (foo,1, -1):
        if isfactor(foo, x ) == True and prime_or_not(x) == True:
            print (x) 
            break
          
        
def main():
    inp = int(input(""))
    
    inp_arr = []
    
    if 1<= inp<= 10:
        for s  in range(inp):
            foo = int(input(""))
            if 10 <= foo <= 10**12:
                

                inp_arr.append(foo)

        for c in inp_arr:
            check(c) 
main()

