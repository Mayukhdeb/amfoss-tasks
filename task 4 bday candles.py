#the candle problem
#can only blow out the tallest candles
# n = age

n = int(input("please enter the value of n for age/ number of candles   -- "))
        
mat = []

high_val = 0

count = 0


print ("-------------")
print ("")

print ("now enter the heights of candles   --  ")

for i in range (n):
        print ("enter height of candle", i+1)   ## change 
        inp = int(input("---    "))
        mat.append(inp)

print (mat)



def find_highest_candle():
        
        global high_val
        for i in range(len(mat)):

                
                if mat[i] > high_val: 
                    high_val = mat[i]


        return high_val
                               


def find_count():
        global high_val

        global count 

        

        for i in range (len(mat)):
                if mat[i] == high_val:
                        count+=1
                else:
                        pass

        return count



find_highest_candle()

find_count()



print("highest candle == ", high_val)
print("no. of candles that will be extinguished =   ", count )
                
        
                
                
                
