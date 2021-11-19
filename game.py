import hangman

def main():
    MAX_TRIES = hangman.first_screen()
    file = input("Please enter the word's file path: \t")
    secret_word_index = int(input("Please enter the secret word's index: \t"))
    num_of_tries = 0 #Setting the user's wrong tries at zero.
    old_letters_guessed = [] #Setting the user's letter guessing as empty list.
    check_win = False #the default value for the win is False in order to start the while loop at least once.

    secret_word = hangman.choose_word(file,secret_word_index) #the tuple that giving the secret word index (index zero) and the secret word (index one).
    template = hangman.word_template(secret_word) #creating the first template depands on the user chosen word.

    print(template)

    while (num_of_tries < MAX_TRIES): #the loop will run until the user have 6 wrong tries (or until he will win - see the break line inside the loop).
        letter_guessed = input("Please choose a letter:\t") #the letter that the user choose.
        letter_check = hangman.try_update_letter_guessed(letter_guessed,old_letters_guessed) #checking if the letter is legit and if it's in the list or not.
        if (letter_check == False): #if the letter isn't legit or it's in the list it considers as wrong try.
            num_of_tries += 1
        if (letter_check == True and letter_guessed.lower() not in secret_word):
            #if the letter isn't in the list but isn't in the secret word as well it considers as wrong try.
            num_of_tries += 1

        if hangman.check_win(secret_word,old_letters_guessed) == True: #using this function to check if the user guessed the secret word.
            print (hangman.show_hidden_word(secret_word,old_letters_guessed)) #prints the pattern of the whole word.
            break #breaks the loop because the user guessed every letter in the secret word.

        print(hangman.print_hangman(num_of_tries), "\n") #prints the hangman picture depands on the user's wrong tries.
        print (hangman.show_hidden_word(secret_word,old_letters_guessed), "\n") #prints the pattern of the word.

    #after the loop ends, the program will check what is the reason it ends.
    if (num_of_tries == 6): #if the reason the loop ends is because the user used 6 tries, he lost.
        print("You lose! the secret word was :", secret_word, "\n")
    else: #if the loop ends not because the user used 6 tries, he won.
        print("Good job, YOU WIN! the secret word is :", secret_word, "\n")

if __name__ == "__main__":
    main()



    

