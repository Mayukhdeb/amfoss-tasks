## long string sorter 

word_arr = []
lock = True
n = 0


while lock == True:
    
    n = int(input("enter the value of the  number of words to be entered"))

    if n > 100 or n < 0:
        print (" enter a value between 0 and 100")

    else:
        lock = False 




for i in range (n):

    print ("enter word", i+1)
    inp = str(input("---  "))
    word_arr.append(inp)




def shorten():
    for i in range (len(word_arr)):

        if len(str(word_arr[i])) > 10:

            new_str = ""

            mid = str(len(str(word_arr[i])) - 2)

            woop = str(word_arr[i])
            
            new_str = new_str + (woop[0])

            new_str = new_str + mid

            new_str =  new_str + (woop[len(woop)-1])

            word_arr[i] = new_str


shorten()
for i in range (n):
    print (word_arr[i])






