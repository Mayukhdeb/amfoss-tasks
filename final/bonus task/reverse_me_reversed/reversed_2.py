## works for the first 6 characters as of now , try enetring "667b6c7d6367"






##    667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268

inp = str(input("enter the encrypted thingy  > "))  ## encrypted thingy


hex_array = []

for i in range (0,len(inp), 2):
    hex_array.append(str(inp[i])+str(inp[i+1]))
print ("HEX ARRAY")
print (hex_array)




xeh_array = []

for j in range (len(hex_array)):
    woop = bytearray.fromhex(hex_array[j]).decode()
    xeh_array.append(woop)


print ("-----------------------------------------------------")



print ("UN-HEXED  ARRAY")
print (xeh_array)





stronk = ""

for m in range (len(xeh_array)):
    
    stronk += (str(xeh_array[m]))


print ("-----------------------------------------------------")

print ("string form  --  ", stronk)   ##################################### PERFECT





pre_shift_arr = []

def rox(foo):
    arr = []
    for phi in range(len(foo)):
        poop = chr(ord(foo[phi])^10)
        
        arr.append(poop)
    return arr

calvin = rox(stronk)


print ("-----------------------------------------------------")
print ("")
print (" UN-XORed array =   ", calvin)  ############################ MARVELOUS

## NOW JUST HAVE TO UNSHIFT THE ARRAY





## unshift

import string



def unshift(arr):
## len alphabets = 25 
    alphabets = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
    numbers = [ 0,1,2,3,4,5,6,7,8,9]
    return_arr = []
    for pop in range(len(arr)):

        if arr[pop].isdigit() == True:
            #print ("digit  !!  ")

            tin = int(arr[pop]) - 3

            if tin<0:
                tin+= 10
            #print ("appending  -- ", tin)
            return_arr.append(tin)

            

        else:
            #print ("alphabet !!")
            

            for e in range (len(alphabets)):
                if arr[pop] == alphabets[e]:
                    cached_index = e

            
            ton = alphabets[cached_index-3]

            for f in range (len(alphabets)):
                if ton == alphabets[f]:
                    cached_final = f
            #print ("appending  -- ", cached_final)
            return_arr.append(cached_final)

        

    return return_arr


print ("-----------------------------------------------------")
print ("")
print ("UN-SHIFTED ARRAY    ", unshift(calvin))

almost_there = unshift(calvin)       
chars = []

print (almost_there)

#####################################################



alphabets_1 = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 

print ("-----------------------------------------------------")
print ("")

    

final_arr = []

for loo in range (len(almost_there)):
    final_arr.append(alphabets_1[almost_there[loo]])

print ("-----------------------------------------------------")



message= ""
              
for mop in range(len(final_arr)):

    message += final_arr[mop]
    
print ("")
print ("message -> ", message)








        



