




##                              INSTRUCTIONS   

##  1 . PRESS ENTER AFTER THE MOUSE POINTER IS ON THE UPPER LEFT VERTEX OF THE MATH PROBLEM

##  2. THE MOVE THE POINTER TO THE LOWER RIGHT CORNER AND PRESS ENTER AGAIN

##  3. PRAY THAT IT WORKS 

## ** MAKE SURE THE TEXT IS NOT TOO SMALL TO READ

#---------------------------------------------------------


##  removes junk automatically junk like whitespaces, "=", etc 

##  detects blank images and requests for input again

##  works not just on 2 digit numbers, but bigger numbers as well

## as of now can only work with one operator

####################################################





from PIL import Image

from read_image import read_image

from mouse_coordinates import queryMousePosition,take_corners

import pyautogui

import string

from crunch_n_chug import crunch_n_chug





def capture_screen(co_ord):

        ##    print (co_ord)

            im = pyautogui.screenshot("ss.png", region= co_ord )

            print ("successfully grabbed image")







def remove_junk(read):
            global fin_arr
            
            read =  "".join(read.split())  # removes trailing and leading spaces

            read = read.replace(" ", "") # remove spaces in between 

            
            arr = list(read)
            
            fin_arr =  arr

            
            for poo in range(len(arr)):   # removes the = ? junk 
                if  arr[poo] == "=":
                    

                    fin_arr = arr[:poo]

                    print ("removed junk  >> ", arr[poo:])

            return(fin_arr)


def main():
    while True :

        lock = True

        while lock == True:

            corners = tuple(take_corners())

            capture_screen(corners)

            print("what python sees -")
            print ("--------------------------------")

            print ("")

            read = read_image("ss.png")    # OCR magic

            print (read)
            print ("")
            print ("--------------------------------")

            if read ==  "":
                print ("")
                print (" cant see a thing ! , try again")
                print ("")
            else:
                lock = False 
                
        arr = []

        fin_arr = []


        final = crunch_n_chug(remove_junk(read))

        print ("the answer is --", final)

        print ("")

        input(" --- PRESS ENTER TO RESTART  ---")

        print ("")


            

main()
