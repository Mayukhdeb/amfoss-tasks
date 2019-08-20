
import string
import binascii

def xor(x):
    q = ''.join(chr(ord(i)^10) for i in x)
    print ("-----------------------------------------------------")
    print ("")

    print (" string form  -- ", q)
    return q

def shift(x):
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    n = []
    for i in x:
        
        if i.isupper() is True:
            n.append(upper[(upper.index(i)+3)%26])
        elif i.islower() is True:
            n.append(lower[(lower.index(i)+3)%26])
        elif i.isdigit() is True:
            n.append(digits[(digits.index(i)+3)%10])
    print ("-----------------------------------------------------")
    print ("")
    print ("string before shift()  - ", x)
    print ("")

    print ("-----------------------------------------------------")

    
    print ("array_entering_xor   - ", n)
    return n

def encode(x):
    
    return x.encode("utf-8").hex()    

if __name__=="__main__":
    
    print ("Enter what you want to encrypt - ")

    arr1 = input()
    


    

    your_code = encode(xor(shift(arr1)))

    print ("-----------------------------------------------------")

    print ("")

    print ("encrypted thingy", your_code)


