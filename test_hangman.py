import hangman
import sys
import io

dictionary_file = 'dictionary_short.txt'

# Custom input function
def custom_input(prompt):
    return "4"

if __name__ == '__main__':
    # test import_dictionary(filename)
    dict_standard = {2:['ad'],
                     3:['bat'],
                     4:['card'],
                     5:['dress'],
                     6:['engine'],
                     7:['T-shirt'],
                     8:['gasoline'],
                     9:['gathering'],
                     10:['evaluation'],
                     11:['self-esteem'],
                     12:['unemployment']}
    dictionary = hangman.import_dictionary(dictionary_file)
    assert dictionary == dict_standard

    # test get_game_options()
    output_standard = 'Please choose a size of a word to be guessed [3 - 12, default any size]:\nThe word size is set to 4.\nPlease choose a number of lives [1 - 10, default 5]:\nYou have 4 lives.\n'
    hangman.input = lambda prompt=None: custom_input(prompt)  # Use custom input function
    stdout = sys.stdout
    sys.stdout = io.StringIO()   # redirect stdout
    size, lives = hangman.get_game_options()
    output = sys.stdout.getvalue()
    sys.stdout = stdout          # restore stdout
    print("Output:", output)
    print("Expected Output:", output_standard)
    assert size == 4
    assert lives == 4
    assert output == output_standard

    print('Everything looks good! No assertion errors!')