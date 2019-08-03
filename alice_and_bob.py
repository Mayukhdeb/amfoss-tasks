alice_scores = []
bob_scores = []

alice_final = 0
bob_final = 0

lock = 1

lock_2 = 1

lock_matrix = []




while lock == 1:
        lock_matrix = []

        alice_raw = input("please enter space seperated scores of alice    --   ")

        alice_scores = [int(i) for i in alice_raw.split() if i.isdigit()]   #detects numbers and makes an array from the string
        
        for n in range (3) :
                
                if alice_scores[n] > 100 or alice_scores[n]<0:
                        
                        
                        
                        lock_matrix.append(1)
                        
                        
                
                        
                else:
                             # unlocked 
                        lock_matrix.append(0)

                
        
        if 1 in lock_matrix:
                lock = 1
                print("Please enter values between 0 and 100 for alice")
                print ("--------------------------")
                print ("")
        else:
                lock = 0






while lock_2 == 1:
        lock_matrix_2 = []

        bob_raw = input("please enter space seperated scores of bob    --   ")

        bob_scores = [int(i) for i in bob_raw.split() if i.isdigit()]   #detects numbers and makes an array from the string
        
        for n in range (3) :
                
                if bob_scores[n] > 100 or bob_scores[n]<0:
                        
                        
                        
                        lock_matrix_2.append(1)
                        
                        
                
                        
                else:
                             # unlocked 
                        lock_matrix_2.append(0)

                
        
        if 1 in lock_matrix_2:
                lock_2 = 1
                print("Please enter values between 0 and 100 for bob")
                print ("--------------------------")
                print("")

        else:
                lock_2 = 0








                








def crunch():
        global alice_final
        global bob_final

        global alice_scores
        global bob_scores

        for n in range(3):
                if alice_scores[n] > bob_scores[n]:
                       alice_final += 1
                elif alice_scores[n] < bob_scores[n]:
                        bob_final += 1


                elif alice_scores[n] == bob_scores[n]:
                        pass







         

         







crunch()

res = [alice_final, bob_final]
print ("RESULT ----    ", res)
