import random


print("Welcome to the Mad Libs exercise program.")
print("I will ask you for your noun(s), adverb(s), adjective(s) and verb(s) to generate a random mad lib. Please enter N to exit the program after your first game.")


run_program = True
list_of_user_words = {}


list_of_mad_libs = []

def get_inputs(typeOfWord): 
    return input("Please enter your {}: ".format(typeOfWord))



while(run_program):
    list_of_user_words_dictionary = {}    
    
    with open("mad_libs.txt", "r") as f:
        list_of_mad_libs = f.readlines()
    
    mad_lib = list_of_mad_libs[random.randrange(len(list_of_mad_libs))]
    
    # parse for number of nouns
    index = mad_lib.count('[noun]')
    for i in range(index):
        noun = get_inputs("noun")
        mad_lib = mad_lib.replace('[noun]', noun)


    # parse for number of verb
    index = mad_lib.count('[verb]')
    for i in range(index):
        verb = get_inputs("verb")
        mad_lib = mad_lib.replace('[verb]', verb)

    mad_lib.count('[verb]')
    # parse for number of adjective
    index = mad_lib.count('[adjective]')
    for i in range(index):
        adjective = get_inputs("adjective")
        mad_lib = mad_lib.replace('[adjective]', adjective, 1)

    # parse for number of adverb
    index = mad_lib.count('[adverb]')
    for i in range(index):
        adverb = get_inputs("adverb")
        mad_lib = mad_lib.replace('[adverb]', adverb)

    print("Your mad lib is: ", mad_lib)

    continueGame = input("Do you want to play again? Y/N")
    if continueGame == 'Y':
        run_program = True
    else:
        run_program = False
   






