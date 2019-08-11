#staircase program
#got rid of the extra space by adding strings instead of using a comma in print statement 

lock = True

while lock == True:


        n = int(input("enter n factor for staircase   ---  "))


        if n>100 or n<0:  #constraint
                print ("")
                print ("   Please enter a number between 0 and 100")
        else:
                
                break

       




for i in range (n+1):

        woop = n-i

        blob= (" ")*woop+("#")*i  #this 

        print(blob)
        
        
        

       
