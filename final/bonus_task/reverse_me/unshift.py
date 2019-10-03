##    667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268

####   ABCDEFGHIJKLMNOPQRSTUVWXYZ

####   abcdefghijklmnopqrstuvwxyz

####   0123456789

upper_arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lower_arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

num_arr = ["0","1","2","3","4","5","6","7","8","9"]


def unshift(foo):


    arr = []

    ploopy = ""

    global upper_arr
    global lower_arr
    global num_arr

    for m in range (len(foo)):
        arr.append(foo[m])
    for n in range (len(arr)):
        
        if arr[n].isupper() is True:

            ind = upper_arr.index(arr[n])

            arr[n] = upper_arr[ind - 3]


        if arr[n].islower() is True:

            ind = lower_arr.index(arr[n])

            arr[n] = lower_arr[ind - 3]

        if arr[n].isdigit() is True:

            ind = num_arr.index(arr[n])

            arr[n] = num_arr[ind - 3]


            

    for ii in range (len(arr)):

        ploopy += arr[ii]
        

    return ploopy

                    





