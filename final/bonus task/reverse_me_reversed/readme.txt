
How the message gets encrypted 



shift()

 --> 61   --shift()-->  [ "9", "4"] 
     

#notice that 6 + 3 = 9 and 1 + 3 = 4 
# similar analogy for alphabets, "a" becomes "d"      <+3 alphabets>
-----------------------------------------------------------------
xor() = This one was a bit of a pain in the butt, I had to learn first about the  XOR gate on youtube. 

I now see the xor gate as "contrast gives 1"

i.e  1^0 or 0^1 will return 1 

and 0^0 or 1^1 will return zero.  

the  property which helped me make the inverse of xor() is that if a^b = c, then a = b^c (arrangement does not matter, ^ is commutative)


I had to reverse     chr(ord(i)^10) = y




-----------------------------------------
now what are chr () and ord () ?


chr() returns a string representing a character whose Unicode code point is an integer.

for example chr(65) = "A"

Ord() is the inverse of chr(), it returns the unicode value (integer) of the character given in as input

for example - ord("A") = 65

hence the inverse of chr() is ord()

---------------------------------------
 
encode() converts each char into their respective hex values 

---------------------------------------

The code that I wrote to reverse the whole process does not work 100% as of now.
