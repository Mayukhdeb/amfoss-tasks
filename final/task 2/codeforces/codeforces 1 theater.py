## Theater square problem

print (" n x m = area of rectangle         dimension of each flagstone = a x a ")

mat = []
lock = True 



while lock == True:

    lock_matrix = []

    mat = input("enter space seperated values of n , m, a  --  ")
    mat = [int(i) for i in mat.split() if i.isdigit()]
    
    for i in range (3):
        if (mat[i]<1 or mat[i]>10**9):  # constraints

            lock_matrix.append(1)

            
            
    else:
        lock = False
        lock_matrix.append(0)  # had to make a lock matrix to look into multiple constraints in parallel
        


    if 1 in lock_matrix:
                lock = 1
                print("Please enter values between 1 and 10^9")
                print ("")
                print ("")
        

area_of_square = mat[0] * mat[1]

area_of_stone = mat[2] **2


n_tiles = 0

while (n_tiles*area_of_stone)< area_of_square:  # counts the number of tiles required
    n_tiles  += 1


print ("")
print ("the minimum number of tiles required to cover the theater square is  -- ", n_tiles)


