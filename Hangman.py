import random
#Picking Random Words and Checking Answers
#Step One: setup word list and pick random word
#Step Two: Ask user to guess a letter and assign lowercase value to variable
#Step Three: check if user guess is a letter in the word.
#Step Three: Add a list for the blank entries. For each letter in the chosen word add a "_" to the list
#Step Four: Display the underscore list
#Step Five: Replace the underscores with correct guess letters

def split(word):
    return[char for char in word]

def printImage(image):
    for i in range(6): #rows
        for j in range(5): #columns
            print(image[i][j], end = " ") 
        print() 

def formatEmptyChars(list):
    for c in list:
        empty_chars.append("_ ")

def printEmptyChars(list):
    for i in range(0, len(empty_chars)):
        print(empty_chars[i], end='')
    print("")

def guess(empty_chars, string_chars):
    index_pos = 0
    good_guess = False
    guess_char = input("What letter do you guess? ")
    for c in string_chars:
        if c == guess_char.lower():
            empty_chars[index_pos] = guess_char.lower()
            good_guess = True
        index_pos += 1
    return good_guess

image = [[' ', '_', '_', '_', ' '], [' ', '|', ' ', '|', ' '], [' ', ' ', ' ', '|', ' '], [' ', ' ', ' ', '|', ' '], [' ', ' ', ' ', '|', ' '], [' ', ' ', '_', '_', '_']]
word_list = ["aardvark", "potato", "battlefield", "puppy", "warriors"]
chosen_word = word_list[random.randint(0, len(word_list)-1)]

gameOver=False
lives = 6
message = ""

empty_chars = []
string_chars = split(chosen_word)

formatEmptyChars(string_chars)
printImage(image)
printEmptyChars(empty_chars)

while not gameOver:
    good_guess = guess(empty_chars, string_chars)
    if good_guess:
        if '_ ' not in empty_chars:
            message = "You Win!"
            gameOver = True
    else:
        lives -= 1
        if lives == 5:
            image[2][1] = 'O'
        if lives == 4:
            image[3][1] = '|'
        if lives == 3:
            image[3][0] = '/'
        if lives == 2:
            image[3][2] = '\\'
        if lives == 1:
            image[4][0] = '/'
        if lives <= 0:
            image[4][2] = '\\'
            message = "You are out of lives. Game Over."
            gameOver = True

    #draw stick figure method
    printImage(image)
    printEmptyChars(empty_chars)
    print(message)
