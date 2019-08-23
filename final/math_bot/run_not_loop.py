




## INSTRUCTIONS

##  1 . PRESS ENTER AFTER THE MOUSE POINTER IS ON THE UPPER LEFT VERTEX OF THE MATH PROBLEM

##  2. THE MOVE THE POINTER TO THE LOWER RIGHT CORNER AND PRESS ENTER AGAIN

##  3. PRAY THAT IT WORKS 

## MAKE SURE THE TEXT IS NOT TOO SMALL TO READ





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

    



    

corners = tuple(take_corners())

capture_screen(corners)

print("what python sees -")
print ("--------------------------------")

print ("")

read = read_image("ss.png")    # OCR magic

print (read)
print ("")
print ("--------------------------------")

arr = []

fin_arr = []

def remove_junk(read):
    global fin_arr
    
    read =  "".join(read.split())  # removes trailing and leading spaces

    read = read.replace(" ", "") # remove spaces in between 

    
    arr = list(read)
    
 

    for poo in range(len(arr)):   # removes the = ? junk 
        if  arr[poo] == "=":
            

            fin_arr = arr[:poo]

    print ("removed junk  >> ", arr[poo-1:])

    return(fin_arr)

        
    


final = crunch_n_chug(remove_junk(read))

print ("the answer is --", final)


    

