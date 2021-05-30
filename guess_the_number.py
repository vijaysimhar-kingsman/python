import random
#you have to guess computer has a number in this perticular code
def guess(x):
    random_number =random.randint(1,x)  #genereating a random number
    guess=0              #making it not eqaul to random number that we generated in order to enter in to loop
    while guess !=random_number:
        guess =int(input(f"enter a number between 1 and {x} :"))
        if(guess>random_number):

            print(f"{guess} oh ohh,you guessed too high")

        elif(guess<random_number):

            print("{} oh ohh,you guessed too low ".format(guess))

    print("yeyy you guesed correctly......")
#what if computer have to guess and you have a number ,let's go for it
def computer_guess(x):
    low =1
    high =x
    feedback =''
    print("\nIf  guessed number by computer is greater than your number give feedback as ('h')\n")
    print("\nIf lesser give ('l'), else give a ('c') : ")
    while feedback !='c':

        if low!=high:
            guess =random.randint(low, high)
        else :
            guess = low # we can give high also not a prob  any way both are same we are doing this because random funcion
                        #genrates an error if both the vaues in the range are same 
        print(f"What about this number {guess} \n")
        feedback=input("\nFeedback(h/l/c) : ")
        if(feedback == 'h'):
            high = guess-1
        elif(feedback == 'l'):
            low = guess+1
            
    print("Yeeey computer won ......")

play=1
while(play==1):
    print("\nDo you wanna guess or do you want to let the computer guess the number____\n")
    choice =int(input("If you wanna guess enter 1 else 2: "))
    
    if(choice==1):
        rangee= int(input("\nEnter the range  : "))
        guess(rangee)
    elif(choice ==2):
        rangee= int(input("\nEnter the range  : "))
        computer_guess(rangee)
    else:
        print("Enter  either 1 or 2 : ")
    print("Do you wanna play again ?")
    play=int(input("If you wanna play enter  1 else 0 : "))


