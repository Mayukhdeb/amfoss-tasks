# k th place -- next round


people_count = 0

rank_count = 0

lock = True

print (" enter space seperated values of n and k       n = total number of contestants         k = cutoff rank ")


while lock == True:
    
    
    inp = input(" make sure n is greater than k   - ")
    inp_array = [int(i) for i in inp.split() if i.isdigit()]

    if inp_array[0] < inp_array[1]:   # constraint
        print ("")
        print (" please try again, n must be greater than k")

    else:
               lock = False 




main = input(" enter space seperated scores of contestants, in descending order ")
main_array = [int(i) for i in main.split() if i.isdigit()]      # stores the raw space seperated scores in the form of an array 

main_array.sort(reverse = True)   #just making sure

print ("The scores entered are   ", main_array)



i = 1

def define_cutoff():

    global i

    global rank_count

    global inp_array

    global people_count

    while rank_count < inp_array[1] and  i<len(main_array):    ## counts until rank count reaches cutoff
   
        woop = i - 1

        if main_array[i]< main_array[woop]:

            rank_count += 1

            people_count += 1                        # no. of people in a certain rank above cutoff get counted here

        elif main_array[i] ==  main_array[woop]:

            people_count += 1

        else:
            pass

        i += 1

           
    print ("")
    print ("no. of qualified contestants is  ", people_count)


define_cutoff()

        

    
  


