##    667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268






def de_code(luigi):

    arr = []
    stronk = ""
    for i in range (0, len(luigi), 2):
        
        indi = luigi[i] + luigi[i+1]

        arr.append(indi)


    for m in range(len(arr)):
        poo = arr[m]

        out = bytearray.fromhex(poo).decode()

        stronk+= out

    return stronk

        
        


    
   

