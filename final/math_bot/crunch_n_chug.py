import string

## take in an array 

def crunch_n_chug(inp):  # slices  cleaned array into 3 parts , digit1, operator, digit2  

    dig_1 = []
    dig_2 = []
    

    for i in range(len(inp)):   


        if inp[i].isdigit() == False:

            doo = i

##            print (inp[doo])    # the sign detected 


    dig_1_arr = {}

    dig_1_arr = inp[0:doo]

    dig_2_arr = inp[doo+1:]

    

    def generate_number(arr):   # generate int form string 
        woop = ""

        for mario in range (len(arr)):

            woop += arr[mario]

        digit = int(woop)
        
        return digit 




    d1 = generate_number(dig_1_arr)
    d2 = generate_number(dig_2_arr)

##    print (d1)
##    print (d2)
    
    if inp[doo] == "+":

        res = d1 + d2

    elif inp[doo] == "-":

        res = d1 - d2

    elif inp[doo] == "/" or inp[doo] == "÷":

        res = d1 / d2

    elif inp[doo] == "*" or inp[doo] == "x" or inp[doo] == "X":

        res = d1 * d2


##    print (res)

    return (res)

    

    
        


        


     

            

            

            

            

            


            

            

            

           

        
    
