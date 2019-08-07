# project Euler # 1

# sum of all multiples of 3 or 5  below N

# T = test_cases


arr = []


def find_sum(foo):

    total = 0

    for i in range (1, foo):

        if i % 5 == 0 or i % 3 == 0:

            total += i

    return total


T = int(input("enter number of test cases   "))

for i in range (T):
    inp = int(input("enter the test cases  ( N )    "))

    arr.append(inp)



for a in range (len(arr)):


    blob = find_sum(arr[a])

    print (blob)
    

    

        
