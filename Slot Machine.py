"""
Programmer: Raj Shah
Description: A program to output the total number of times one can play if they have a certain amount of quaters. Machine 1 pays 30 quaters every 35th time, machine 2 pays 60 quaters every 100th time, machine 3 pays 9 quaters every 10th time.
Version: 1.0
Date: July 27, 2022

Algorithm:
create function play with parameter L
    set the number of quaters dora has
    define plays variable
    create loop while quaters is greater than 0
        increment the first machine and total plays by 1
        if the first machine reaches 35, increment quaters by 30
            then reset the machine to 0 plays

        decrement quaters by 1
        break out of loop if quaters is 0

        increment the second machine and total plays by 1
        if the second machine reaches 100, increment quaters by 60
            then reset the machine to 0 plays

        decrement quaters by 1
        break out of loop if quaters is 0

        increment the third machine and total plays by 1
        if the third machine reaches 10, increment quaters by 9
            then reset the machine to 0 plays

        decrement quaters by 1
        break out of loop if quaters is 0

    return plays in the function

create infinite loop
    get user list input
    call play function with user's input as the parameter

"""

def play(L):
    quaters = L[-1]
    plays = 0
    
    while quaters > 0:
        L[0] += 1       # check first machine if it has reached 35 plays and increment quaters
        plays += 1
        if L[0] == 35:   
            quaters += 30
            L[0] = 0

        quaters -= 1    # decrement quaters after each play

        if quaters == 0:
            break
        
        L[1] += 1       # check second machine if it has reached 100 plays and increment quaters
        plays += 1
        if L[1] == 100:
            quaters += 60
            L[1] = 0

        quaters -= 1

        if quaters == 0:
            break

        L[2] += 1       # check third machine if it has reached 10 plays and increment quaters
        plays += 1
        if L[2] == 10:
            quaters += 9
            L[2] = 0

        quaters -= 1

        if quaters == 0:
            break

    return plays

while True:
    l = eval(input("Enter the list L: "))
    print(play(l))
