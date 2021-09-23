import random

def draw_letters():
    letter_pool = {
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

    letters_drawn = []

    letter_pool_list = []
    for key in letter_pool:
        for idx in range(letter_pool[key]):
            letter_pool_list.append(key)

    while len(letters_drawn) != 10:
        random_entry = random.choice(letter_pool_list)
        letters_drawn.append(random_entry)
        letter_pool_list.remove(random_entry)
    return letters_drawn


    
    
    # * is array a list or dictionary which includes the qty + letters

    
    # create a data structure for the distribution of letters
    # while len of new data structure - list "letters" is < 10
    #   note to self - double check length of 10 actually means 10
    # use random() to pull a random letter
    #   check if random letter is in our dataset 
    # #   check if quantity is > 0
    # #    if yes then return letter to list "letters" as single letter strings
    # #      qty value of letter decrease by 1
    # #    if not - continue 
    # return list of drawn letters

def uses_available_letters(word, letter_bank):
    pass

# return a score (int) of inputted word
    # create score chart data structure
        # dictionary with score int as the key and a list of string letters as the values
    #for each letter in the word
    #   find the letter in the score chart
        # will need to access the list of letters
        # for each score value (key)
        #   access the letter which is the value and a list
        #   iteratre thru the list to flag if the letter exists
        #  perhaps use continue?? when letter is found
    #   add up the points from each letter in word
    #   define var for total points (count)
    # count length of word
    #   if length 7 -10 letters long, add 8 pts
    pass

def score_word(word):
    
    score_chart = {
    
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
    }

    word = word.upper()
    total_points = 0

    for letter in word:
        total_points += score_chart[letter]
    if len(word) >= 7 and len(word) <= 10:
        total_points += 8
    
    return total_points

def get_highest_word_score(word_list):
    pass