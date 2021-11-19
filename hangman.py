def first_screen():
    '''the function prints the first screen and giving the player number
    of tries.
    :return MAX_TRIES: the number of tries.
    :rtype: num'''
    print("""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")

    MAX_TRIES = 6
    print("You have 6 tries")
    return MAX_TRIES

def choose_word(file_path, index):
    '''the function returns tuple including the number of different words on the list it gets and the secret word.
    :param file_path: file including words.
    :param index: the index of the secret word.
    :return gametuple: tuple that including the number of different
    words and the secret word.
    :rtype: tuple'''
    file = open(file_path, "r") #opens the file with the words.
    data = file.read()
    words = data.split()
    file.close()
    templist = []
    if (index > len(words)): #if there is word that match the index (the index is bigger then the word's list)
        while (index > len(words)): #the user will insert new index until he'll insert legit one.
            print("The index ", index," isn't in the list's range")
            index = int(input("Please enter the secret word's index: \t"))
                  
    selectedword = words[index-1].lower() #the secret word will be with lowercase letters.
    wordsnum = 0
    for i in words: #in the assignment, we asked for giving the number of different words.
        if (i not in templist): #this loop making sure the counter will count and append only new words in the list.
            templist.append(i)
            wordsnum += 1

    return selectedword

def word_template(selectedword):
    '''the function gets the selected word and turns it into a template.
    :param selectedword: the secret word the user chose.
    :return wordtemplate: the secret word template.
    :rtype: str'''
    wordlength = len(selectedword) #the length of the secret word.
    wordtemplate = ("_ " * wordlength) #creating the word's template.
    return wordtemplate

def check_valid_input(letter_guessed, old_letters_guessed):
    '''the function checking if string include only one alpabeth letter
    and if it's on a list, given a string.
    the function returns true if the letter isn't on the list and
    adds it to that list. if the letter isn't only
    one alpabeth letter or it's already on the list - the function
    return False with the list sorted.
    :param letter_guessed: the string the user insert
    :type letter_guessed: str
    :param old_letter_guessed: the letters the user already tried.
    :type old_letters_guessed: list
    :return: boolean value depands on letter_guessed
    :rtype: bool'''
    
    import string
    counter = 0
    
    if (len(letter_guessed) > 1):
        return False
    elif (letter_guessed not in string.ascii_letters or letter_guessed.lower() in old_letters_guessed or letter_guessed.upper() in old_letters_guessed):
    #if the letter is only alphabeth letter and in the old_letters_guessed list.
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    '''the function using the function check_valid_input to check if the letter is legit.
    the function checking if the letter is in the old_letters_guessed list and return the right value.
    :param letter_guessed: the secret word the user needs to guess.
    :param old_letters_guessed: list of the letters the user already guessed.
    :return wordtemplate: the secret word template.
    :rtype: str'''
    import hangman
    tempstr = ""
    indicator = hangman.check_valid_input(letter_guessed, old_letters_guessed)
    
    if (indicator == True): #with the check_valid_input function, the indicator points if the letter is legit.
        if (letter_guessed in old_letters_guessed): #if the letter that the user guessed already in the old_letters_guessed list.
            print ("X")
            for i in sorted(old_letters_guessed):
                tempstr = tempstr + i + " -> "
            print (tempstr)
        else:
            old_letters_guessed.append(letter_guessed.lower())
        return True

    else: #if the letter the user chose is illegal.
        print ("X")
        for i in sorted(old_letters_guessed):
            tempstr = tempstr + i + " -> "
        print (tempstr)
        print (indicator)
        return False

def show_hidden_word(secret_word,old_letters_guessed):
    '''the function returns string combined with underscores and the letters that
    match to the secret word, given a string and list of guessed letters.
    :param secret_word: the word the user needs to guess.
    :type letter_guessed: str
    :param old_letters_guessed: list of the letters the user already guessed.
    :return progressword: string combined with underscores and the letters
    :rtype: str'''
    
    progressword = ""
    for i in secret_word:
        if (i in old_letters_guessed):
            progressword = progressword + "" + i.lower() + " "
        else:
            progressword = progressword + " _ "
    return progressword

def is_valid_input(letter_guessed): #unnessecery for the game but was one of the assignments.
    '''the function checking if string include only one alpabeth letter,
    given a string.
    :param letter_guessed: the string the user insert
    :type letter_guessed: str
    :return: boolean value depands on letter_guessed
    :rtype: bool'''
    
    import string
    counter = 0
    lettervalue = None
    for i in letter_guessed:
        if (i not in string.ascii_letters):
            counter = counter + 1
            
    if (len(letter_guessed) < 1): #if there is no input.
        print ("Next time please guess a letter.")
        lettervalue = False
    elif (len(letter_guessed) > 1):
        if (counter == 0): #if the string is longer than one letter and not include special letter.
            lettervalue = False
        else:
            lettervalue = False #if the string is longer than one letter and include special letter.
            
    elif (counter > 0): #if the string is only one special letter.
        lettervalue = False
    else:
        lettervalue = True #if the string is only one alpabeth letter.

    return lettervalue



def check_win(secret_word,old_letters_guessed):
    '''the function returns True if the list includes all the letters in the
    secret word or False if not, given a string and list of guessed letters.
    :param secret_word: the word the user needs to guess.
    :type letter_guessed: str
    :param old_letters_guessed: list of the letters the user already guessed.
    :return: boolean value
    :rtype: bool'''

    counter = 0
    for i in secret_word:
        if (i in secret_word and i not in old_letters_guessed):
            counter += 1
    if (counter == 0):
    #if the counter equals zero, all of the letters in the secret word is in the old_letters_guessed list so the user guessed them all.
        return True
    else:
        return False
    
    


def print_hangman(num_of_tries):
    '''the function returns the correct picture depands
    the number of tries that the player played.
    :param num_of_tries: the number that the player played already.
    :return: string.
    :rtype: str'''
    picslist = (
    """    x-------x""",
    """
        x-------x
        |
        |
        |
        |
        |""",
    """
        x-------x
        |       |
        |       0
        |
        |
        |""",
    """
        x-------x
        |       |
        |       0
        |       |
        |
        |""",
    """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |""",
    """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |""",
    """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |""")
    return picslist[num_of_tries]


def main():
    import hangman
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



    




