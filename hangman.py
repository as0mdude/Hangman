# assignment: programming assignment 1
# author: Vincent Fu
# date: 4/11/2023
# file: hangman.py is a program that plays a text-based hangman game.
# input: dictionary file, size of word, guesses count, and letters being guessed
# output: if the letter is in the word, how many guesses left, and the correct word after the total guesses are all finished.

import random

dictionary_file = "dictionary.txt"


def import_dictionary(filename):
    dictionary = {}
    max_size = 12
    
    with open(filename, 'r') as file_object:
        word_list = [line.strip() for line in file_object]
        word_list.pop()

    dict_list = [[] for _ in range(max_size)]

    for word in word_list:
        word_length = len(word)
        if word_length > max_size:
            word_length = max_size
        dict_list[word_length - 1].append(word)

    for i in range(len(dict_list)):
        dictionary[i + 1] = dict_list[i]

    del dictionary[1]
    #print(dictionary)
    
    return dictionary


def get_game_options():
    while True:
        try:
            print("Please choose a size of a word to be guessed [3 - 12, default any size]:")
            user_size = int(input())
            if user_size < 3 or user_size > 12:
                raise ValueError
            size = user_size
        except ValueError:
            size = random.randint(1, 12)
            print("A dictionary word of any size will be chosen.")
        break
    print(f"The word size is set to {size}.")

    while True:
        try:
            print("Please choose a number of lives [1 - 10, default 5]:")
            user_lives = int(input())
            if user_lives < 1 or user_lives > 10:
                raise ValueError
            else:
                lives = user_lives
        except ValueError:
            lives = 5
        break
    print(f"You have {lives} lives.")
    
    return size, lives


if __name__ == '__main__':
    dictionary = import_dictionary(dictionary_file)
    print("Welcome to the Hangman Game!")
    
    while True:
        word_size, lives = get_game_options()

        word = random.choice(dictionary[word_size]).upper()

        chosen_letters = []
        hidden_letters = ['__' for _ in range(word_size)]
        life = ['O' for _ in range(lives)]
        win = False
        lose = False
        repeat = False
        
        while not lose and not win:
            if not repeat:
                print('Letters chosen:', ', '.join(chosen_letters))
                for letter in hidden_letters:
                    print(letter, end='  ')
                print(f' lives: {lives}', ''.join(life))
            
            repeat = False
            try:
                print('Please choose a new letter >')
                letter = input().strip().upper()
                
                if letter in chosen_letters:
                    print("You have already chosen this letter.")
                    raise ValueError
                elif not letter.isalpha() or len(letter) > 1:
                    raise ValueError
                elif letter in word:
                    print("You guessed right!")
                    chosen_letters.append(letter)
                    hidden_letters = [letter if word[i] == letter else hidden_letters[i] for i in range(word_size)]
                else:
                    print("You guessed wrong, you lost one life.")
                    chosen_letters.append(letter)
                    lives -= 1
                    life[lives - 1] = 'X'
                
                hidden_word = ''.join(hidden_letters)
                win = hidden_word == word
                lose = lives <= 0
            except ValueError:
                repeat = True
            
        print('Letters chosen:', ', '.join(chosen_letters))
        for letter in hidden_letters:
            print(letter, end='  ')
        print(f' lives: {lives}', ''.join(life))
        
        if win:
            print(f"Congratulations!!! You won! The word is {word}!")
        if lose:
            print(f"You lost! The word is {word}!")

        try:
            print('Would you like to play again [Y/N]?')
            new_game=input().upper()
            if(new_game == 'Y'):  
                continue
            else:                
                raise ValueError
        except:
            print('Goodbye!')
            break
