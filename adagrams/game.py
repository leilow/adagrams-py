import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}


def draw_letters():
    # takes in no parameter
    letters = [] # the "hand" with 10 letters that we return

    # random drawing from letters in dictionary — random module***
    """ 
    STEPS:
    begin to pull letters, randomly
        iterate through dict, key:value pair
        as we iterate, update the value
        update a list of letters, .append()
    return the hand
    """
    # Our thoughts on making a loop
    """
    LOOP:
    random get a key from —> calls the value
    return an updated value
    """

    # get a random letter
    # random_letter = random.choice(list(LETTER_POOL.keys()))
    # # player_choice = list(LETTER_POOL.values()) # random piece of code we were thinking about using LOL
    # print("Here's your letter = ", random_letter)

    # # create a list with the letters chosen
    # letters.append(random_letter)
    # print("Here's your current hand =", letters)

    # create a list that's 10 letters long
    count = 0
    
    while len(letters) < 10:
        random_letter = random.choice(list(LETTER_POOL.keys()))
        letters.append(random_letter)
        count += 1
        print(letters)

        # iterate through the list of letters being randomly pulled for the hand
    # for letters in range(len(letters)):

    # # for-loop updates the dictionary
    #     for letter, value in LETTER_POOL.items():
    #         # print(letter, value)
    #         if letter == random_letter:
    #             print(letter, value)
    #             value -= 1
    #             print(letter, value)
    #             return value
    


        # counter? length of letters list, as we try to get 10 letter for the hand
        # return the value—so update the dictionary           

    # returns array of 10 strings - testing for len(letters) == 10
    return letters

    
    
    
    pass

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass