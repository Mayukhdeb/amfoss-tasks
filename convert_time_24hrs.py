## cvt to 24 hr format

inp =  str(input("enter time in hh:ss:mmAM format   "))

arr = (inp.split(':'))

woop = (arr[2])


half = str(woop[2])

tens = int(woop[0])

ones = int(woop[1])

sec = (tens*10) + ones


print ("")



def convert():

    if half == "A":

        hour = arr[0]

        minute = arr[1]

        print ("the converted time is ---   ", hour,":", minute,":", sec)

    elif half == "P":
        

        hour = int(arr[0]) + 12

        minute = arr[1]

        print ("the converted time is ---   ", hour,":", minute,":", sec)


convert()


        
        
    



