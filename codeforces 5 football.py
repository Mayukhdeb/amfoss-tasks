# football

inp = str(input(" enter the sequence of 0's and 1's "))

inp_array = list(inp)



danger = False

count = 0

def crunch():

    global count
    global danger
    for i in range (1,len(inp_array)):

        woop = i-1

        if inp_array[woop] == inp_array[i]:
            count+=1
            

        elif inp_array[woop] != inp_array[i]:
            count = 0

        if count >= 7:
            danger = True

            

crunch()

if danger == True:
    print ("YES")

else:
    print ("NO")
