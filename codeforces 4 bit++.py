# Bit ++

final = 0

lock = True

woop = 0

i = 0


while lock == True:

    woop = int(input("enter number of operations to be done   "))
    

    if woop<1 or woop > 150:
        print ("")
        print (" please try again, n must be between 1 and 150    ")

    else:
               lock = False 




def bit_add():
    global final

    final += 1


def bit_sub():
    global final

    final -= 1


def detect_operation(foo):

    

    if "++" in foo:
        bit_add()
       

    elif "--" in foo:
        bit_sub()
        
    else:
        print ("invalid syntax")
        



for i in range (woop):
    
    foo = str(input("enter operation "))
    detect_operation(foo)
        



print (final)


    
    
