#diagonal matrix
#take dimensions and find diff of diagonals sum



n = 1

matrix = []

primary_dia = []

secondary_dia = []

sum_primary = 0

sum_secondary = 0


def input_dimension():
        global n
        n = int(input("enter value of n for n x n matrix    "))
        
input_dimension() 


def input_matrix():
        global matrix

        for i in range (n):
                sub_matrix = []
                for j in range (n) :
                        
                        print ("enter values of row - ", i + 1,"  column - ", j +1)
                        inp = int(input(""))
                        sub_matrix.append(inp)
                matrix.append(sub_matrix)
                                

input_matrix()

        

def find_primary_diagonal():
        global primary_dia
        for foo in range(n):
                beep = matrix[foo]

                plop = beep[foo]
                primary_dia.append(plop)

        print ("primary diagonal   --   ", primary_dia)


def find_secondary_diagonal():
        global secondary_dia
        global matrix
        oof = 0
        
        for foo in range(n-1, -1 , -1):  #fancy indexing
                oof = (n-1 - foo)

                
                beep = matrix[foo]

                plop = beep[oof]
                secondary_dia.append(plop)

        print ("secondary diagonal   --   ", secondary_dia)




def dia_sum_pri():
        global n
        global sum_primary

      
        for i in range (n):
                
                sum_primary = sum_primary + primary_dia[i]
                

        return sum_primary


def dia_sum_sec():
        
        global n
        global sum_secondary
        for i in range (n):
                
                sum_secondary = sum_secondary + secondary_dia[i]       

        return sum_secondary


                                
print (matrix)
print("")

find_primary_diagonal()

find_secondary_diagonal()

dia_sum_pri()
dia_sum_sec()

woop = dia_sum_pri() - dia_sum_sec()


answer = abs(woop)

print("")
print ("absolute difference between diagonal element sum   --   ",answer)
