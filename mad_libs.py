import random


print("Welcome to the Mad Libs exercise program.")
print("I will ask you for your noun, adverb, adjective and verb to generate a random mad lib. Please enter N to exit the program after your first game.")


run_program = True
list_of_user_words = {}


list_of_mad_libs = ["He said bye as he adverb verb into his convertible noun and drove off with his adjective wife.",
 "Six adjective cats verb adverb on the adjective noun.",
 "Oranges and noun balance adverb on the adjective table while she verb. ",
 "She jumped adverb and verb behind a adjective noun.",
 "The child ran adverb to his adjective green noun and verb angrily.",
 "The adjective fox jumped adverb over the litte brown noun who verb."]

def get_inputs(): 
    noun_word = input("Please enter your noun:")
    adverb = input("Please enter your adverb: ")
    adjective = input("Please enter your adjective: ")
    verb = input("Please enter your verb: ")

    list_of_user_words_dictionary['noun'] = noun_word
    list_of_user_words_dictionary['adverb'] = adverb
    list_of_user_words_dictionary['adjective'] = adjective
    list_of_user_words_dictionary['verb'] = verb


while(run_program):
    list_of_user_words_dictionary = {}    
    get_inputs()
    

    mad_lib = list_of_mad_libs[random.randrange(6)]
    mad_lib = mad_lib.replace('noun', list_of_user_words_dictionary['noun'])
    mad_lib = mad_lib.replace('adverb', list_of_user_words_dictionary['adverb'])
    mad_lib = mad_lib.replace('adjective', list_of_user_words_dictionary['adjective'])
    mad_lib = mad_lib.replace('verb', list_of_user_words_dictionary['verb'])
    

    print("Your mad lib is: ", mad_lib)

    continueGame = input("Do you want to play again? Y/N")
    if continueGame == 'Y':
        run_program = True
    else:
        run_program = False
   






