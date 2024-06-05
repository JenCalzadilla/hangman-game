import os
import random


# It remove the accents of a string
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


# choose the word from data
def choose_word():
    random_word = random.randint(0, 50)
    with open('./files/data.txt', 'r', encoding='utf-8') as data:
        # removes line breaks (\n)
        words = {str.rstrip(word) for word in data}
        words = dict(enumerate(words)) 
    word = [letter.lower() for letter in normalize(words.get(random_word))] # Select a word at random and separate its letters into a list.
    return word

# game mechanism
def game(secret_word, number_clue, system):
    guessed_letters = set()
    attempts = 0
    win = victory()
    lose = defeat()
    ini = msj_initial()
    cade = ""
        
    while attempts <= 7:
        system_clean(system.lower())
        
        print(ini)
        print(secret_word)
        print(draw_hangman(attempts))
        
        # Show the guessed letters for now
        guessed_word = ''.join([letter if letter in guessed_letters else  '-' for letter in secret_word])
        print("Guessed letters:", guessed_word)
        
        # Check if the user insert a valid letter
        try:
            # ask a letter to user
            letter = input('Enter a letter: ')
            assert letter.isalpha(), input('Please insert a valid letter')
            assert len(letter) == 1, input('Please insert only single letter')
        except AssertionError as e:
            print(e)
            continue
        
        #if not letter.isalpha() or len(letter) != 1:
        #    raise ValueError('Please insert a valid single letter')
            
                    
        # Check the letter in the secret word
        if letter.lower() in secret_word:
            # Add the letter in the correct index
            guessed_letters.add(letter.lower())     
        else:
            attempts += 1
            
        # verify if the user guessed the word
        if set(secret_word) == guessed_letters:
            cade = "".join(map(str, secret_word))
            print("You Win! the word is:", cade.upper())
            print(win)
            break        
    else: 
        print(lose)
        

# message displayed when winning
def victory():
    msj_victory = f'''
    
       _______________________________
      |   __      __   _     __  _    | 
______|   \ \    / /  | |   |  \| |   |_______
\     |    \ \/\/ /   | |   | |\  |   |      /
 \    |     \_/\_/    |_|   |_| \_|   |     /
 /    |_______________________________|     \
/________)                        (__________\
    
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠴⡶⠶⢒⡒⠶⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠙⠋⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢓⣺⣮⣧⡀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡗⣆⠀
⣰⡿⣿⣿⣄⠀⠀⠀⠀⠀⠀⣰⣯⣿⣿⣷⣶⣤⣤⡀⠀⠀⠀⠀⠀⣤⣶⣾⣿⢿⡿⢿⣷⡄⠀⠀⠀⠀⠀⣰⢿⣿⡿⠈⡇
⣿⣲⣼⣿⣿⣦⡀⠀⠀⠀⢠⡿⠋⠉⠁⠉⠉⠉⠙⢻⡀⠀⠀⠀⣰⠋⠉⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⣠⠞⠛⣪⣟⣧⣶⠟
⠙⠛⠻⠿⠷⣦⣉⡓⢦⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⣴⣿⣠⣶⡶⠤⠀⠀⠀⢀⣿⣟⣷⣿⣧⠴⠋⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⢻⡄⠙⠀⠀⠀⣠⣤⣤⣦⣤⣵⡂⠀⠀⠀⢸⣿⣿⣯⣴⣿⣷⠾⣿⣬⣿⣿⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠈⠙⠿⠤⣿⣿⣷⡿⠋⠀⠀⠀⠀⠉⢻⡿⠾⠿⣿⣷⠿⠟⠋⠈⠈⢷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠉⠛⠛⠉⡁⠀⠀⠀⠀⠀⠀⠀⠈⢿⡶⣤⡀⠀⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⣠⣞⣀⣀⡀⠀⠀⠀⠀⢀⣠⣿⣷⣾⣷⣄⣀⡀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⣠⣶⠾⠋⠈⠙⠛⠛⠻⠶⣿⣿⣿⣿⣿⣿⡿⠿⠿⣉⠛⢷⠀⢠⠐⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣷⠘⡇⠀⠸⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠘⠁⠠⢴⣤⣄⣀⣠⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣾⣿⣿⣿⢿⡄⢿⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠈⠙⢿⣉⢹⡏⢻⡟⠉⠛⡟⠉⢹⣇⣽⣿⣿⠟⣡⣿⣧⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣷⣶⣾⡿⠿⢿⡿⠟⠋⣡⣾⡟⠹⣿⡿⣄⣼⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣉⣉⣉⣭⣤⣶⠟⣉⣸⡋⠀⣿⠀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢿⢿⣿⠁⢰⣇⣠⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⠆⠿⠀⣠⣥⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣷⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤⣤⣤⣤⣤⣤⣶⣾⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    '''
    return msj_victory


# message displayed when lose 
def defeat():
    msj_defeat = f'''
    
 __^__                                      __^__
( ___ )------------------------------------( ___ )
 | / |                                      | \ |
 | / |       YOU FAILED, GAME OVER!         | \ |
 |___|                                      |___|
(_____)------------------------------------(_____)

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⠊⠉⠉⠉⠒⠲⢤⣀⠀⠀⠀⠀⠀⣀⣤⠤⠶⠒⠶⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣀⣠⠤⢤⣀⣀⡀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠉⠙⠲⢤⣹⣀⣀⡤⠤⠤⠤⠤⠤⠤⢄⣀⣈⣇⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣙⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠒⣊⡭⠥⠔⠒⠲⠦⠤⢭⣉⣳⣄⣤⣴⣒⣊⡭⠭⠭⠭⠭⠭⣿⣶⣻⣦⣀⠀
⠀⠀⠀⢀⡴⠚⢹⠃⠀⠀⠀⠀⠀⠀⢀⡤⠖⢚⣡⠖⠋⠁⠀⠀⠀⠀⠀⢀⣀⣀⣀⣙⣿⡛⠉⠁⠀⢀⣀⣀⣠⣤⣤⣤⠤⣭⣝⣿⣄
⠀⠀⢠⡞⠁⠀⣾⠀⠀⠀⠀⠀⠀⣾⣛⣛⠋⠉⢀⣀⣀⡠⠤⢶⣶⢿⣿⣿⣤⡀⠀⠀⠈⡷⠒⠚⠉⠉⢠⣿⡿⢿⣿⣿⣦⡀⠀⠉⢻
⠀⢀⡏⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠯⣉⠀⠀⠀⢠⣿⣿⣶⣿⠛⢻⣿⡆⠀⣰⠁⠀⠀⠀⠀⣿⣿⠿⣿⣏⣹⣿⣧⢀⣠⡞
⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⢬⣙⠒⠤⢼⠿⢿⡿⠿⠿⠿⠛⠛⢉⡼⠛⠓⠒⠒⠶⠟⠛⠛⠛⠛⠛⠋⢩⡿⠛⠀
⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠒⠒⠒⠒⠒⠒⣲⡾⠉⠉⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠋⠁⠀⠀⠀⠀⠈⠛⠢⢤⣤⠤⠤⠴⠒⢿⡁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠁⡀⠀⣀⡀⠀⠉⠉⠙⠓⠒⠲⠦⠤⠤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⠤⠶⠚⠉⢉⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡅⠀⠀⠉⠉⠉⠉⠉⠓⠒⠶⠤⢤⣤⣀⣀⣀⣀⡀⠀⠀⠉⠉⠉⠉⠁⣀⣀⣀⣀⣠⣴⠟⠁⠀⠀
⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠙⠒⠒⠒⠒⠒⠲⠦⠤⠤⣀⣀⣀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⢀⣿⠀⠀⠀⠀
⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠛⠒⠒⠒⠒⠶⠶⠶⠶⢶⡦⠶⠒⠋⠁⠀⠀⠀⠀
⠟⠿⢿⡶⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠓⠦⣭⣉⠓⠒⠶⠦⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡤⠖⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠲⠦⢤⣤⣤⣀⣀⣀⣉⣉⣉⣉⣉⡉⢉⣉⣉⣉⣉⣩⣭⠟⠛⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    
    '''
    return msj_defeat


# initial message hangman game
def msj_initial():
    hangman_letter = f'''
    
$$\                                                                       
$$ |                                                                      
$$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\  
$$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ 
$$ |  $$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |
\__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|
                              $$\   $$ |                                  
                              \$$$$$$  |                                  
                               \______/                                   

                            by Jen Calzadilla
    '''
    return hangman_letter


# drawing of the hangman
def draw_hangman(key):
    hangman = [
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        '''
        ,
        '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        '''
        ,
        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        '''
        ,
        '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        '''
        ,
        '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        '''
        ,
        '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        '''
        ,
        '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        '''
        ,
        '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
           ===
        '''
    ]
    return hangman[key]


#check if the system is equal to windows
def system_clean(system):
    if system == 'y':
        os.system('cls')
    else:
        os.system('clear')


def run():
    secret_word = choose_word()
    #guessed_letters = ['_' for letter in secret_word]
    #attempts = 0
    number_clue = len(secret_word)
    win = victory()
    lose = defeat()
    
    # Check what is your operating system 
    system = input('Are you using OS Windows y/n: ')
    
    # play the game
    game(secret_word, number_clue, system)


if __name__ == '__main__':
    run()