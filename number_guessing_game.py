import random
num = random.randint(1, 100)
count = 0
user = int(input("Enter your guess between 1 and 100: "))
count+=1
lownum = 1
highnum = 100
while num != user:
    if user > num:
        highnum = user
        print("Your guess was too high, try again. ")
        count+=1
        print("Between", lownum, "and ", highnum)
        user = int(input("Please enter your guess: "))
    elif user < num:
        lownum = user
        print("Your guess was too low, try again. ")
        count+=1
        print("Between ", lownum, "and ", highnum)
        user = int(input("Please enter your guess: "))
while num == user:
    print("You got it in ", count  ," tries! ")
    again = input("Would you like to play again? (y/n) ")
    if again == "y":
        print("i cant figure this out without doing function stuff so just launch it again from the terminal lol.")
        exit()
    elif again =="n":
        print("Thanks for playing.")
        exit()
    else:
        print("thats not a valid input, please try again.")
        again = input("Would you like to play again? (y/n) ")

#if user > num:
#    print("Too high, it was", num)
#elif user < num:
#    print("Too low, it was", num)
#else:
#    print("You got it!")
