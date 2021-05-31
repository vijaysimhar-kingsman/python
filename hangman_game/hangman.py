import random
from words_doc import words
import string

def valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word =random.choice(words)
    return word.upper()

def hangamn():
    word = valid_word()
    #print(word)
    word_letters = set(word) #this converts word to set of characters in it in alphabetical order
    #print(word_letters)
    alphabets =set(string.ascii_uppercase)# storing all uppercase lettes  in list
    used_letters=set()
    lives =6
    #taking user input
    while (len(word_letters))>0 and lives >0:

        #print the letters  used for user idea
        print(f"you have left with {lives} lives , you have used : "," ".join(used_letters))

        #write current word in this style (W-RD)
        word_list=(letter if letter in used_letters else "-" for letter in word)
        print("current word : "," ".join(word_list))

        user_letter = input("\nguess a letter : ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print("\nyou have guessed wrong letter__________\n")
        elif(user_letter in used_letters):
            print("\nyou have entered it already , plese try another \n")
        else:
            print("\ninvalid character\n")
    
    if(lives==0):
        print(f"\nyou died , and the word is {word}\n")
    elif(lives==6):
        print(f"you are jus awesome ,you guessed it correctly without a single loose of life :{word}")
    elif(lives!=0):
        print(f"yeyy you guessed it correctly : {word}")
    elif(lives==1):
        print(f"omg atlast you guessed it correctly:  {word}")

intrested =1
while(intrested):
    hangamn()
    intrested=int(input("\n\nEnter 1 to play again , else  enter 0: "))