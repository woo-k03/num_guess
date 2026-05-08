import random

rand_num = random.randint (0,100)

while True:
    guess = int(input ("Guess the numer: "))
    if guess > rand_num:
        print ("Lower!")
    elif guess < rand_num:
        print("Higher!")

    else:
        print ("Correct!!")
        break