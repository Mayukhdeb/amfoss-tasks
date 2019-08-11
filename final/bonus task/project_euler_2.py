
# euler 2

arr = []
arr_even = []
arr_inp = []


def fibonacci_final(foo):
   
    foo = foo - 2
    a = 0
    b = 1
    for i in range(foo):
        t = a + b
        a = b
        b = t

    return t


def chop_fib(lim):

    global arr

    arr = []
    i = 3
    while fibonacci_final(i) <= lim:
        i+=1
        arr.append(fibonacci_final(i))

    arr.pop()
    return arr
    
 

def evonacci(blob):   # extract even terms
    
    global arr
    global arr_even
    arr_even = []

    for i in range (len(blob)):
        if arr[i] % 2 == 0:
            arr_even.append(arr[i])

    return arr_even  ## array of even terms



def find_even_sum(woop):
    sumonacci = 0

    for i in range (len(woop)):
        
        sumonacci += arr_even[i]
    return sumonacci





def main():

    lock = True 
    while lock == True :

    
        T = int(input("enter number of test cases   "))

        if T<0 or T> 10**5:

            print ("please enter values between 1 ans 10^5")
            print ("")

        else:
            lock = False 
            
    for i in range (T):

        lock = True 
        while lock == True :
            inp = int(input("enter the test cases  ( N )    "))

            if inp<10 or inp> 4 * 10**16:   # constraint
                print ("make sure the N is between 10 and 4 x 10^16")

            else:
                lock = False 

        arr_inp.append(inp)



    for i in range (len(arr_inp)):

        print (find_even_sum(evonacci(chop_fib(arr_inp[i]))))

       
    
main()        


    
