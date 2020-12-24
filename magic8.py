from random import randrange

##what to add
# confirmation of if that is their question where if the answer no they will be asked again
# after question has be answered ask if they would like another question to be answered(done)
# recognize a 42 reference and respond with a custom reponse (done)
# add custom list of "questions" to inform user to ask a question. (Requested by: (Requested by: Lamar "Goku" Brooks)
# add custom list of "acknowledgements" when user wants to ask more questions. (Requested by: Lamar "Goku" Brooks)

pattern_magic = '\n*POOF* MAGIC8 HAS JUST {} THE SHADOWS!!! *POOF*\n'
pattern_respond = '\nMagic8: So that\'s what you want to know, is that right?\nMagic8: Well, {}\n'

def magic8():
    
    question = str(magic8_question())
    if "meaning of life" in question:
        response = pattern_respond.format(str(42))
    else:
        response = pattern_respond.format(str(magic8_response()))
    print(response)
    magic8_again()
    

def magic8_question():
    print('Magic8: Ask me your wildest desires!')
    question = input('Ask Magic8 a question: \t')
    return question

def magic8_response():
    list_of_responses = get_list_of_responses()
    num = int(randrange((int(len(list_of_responses))-1)))
    response = list_of_responses[num]
    return response

def get_list_of_responses():
    # The File magic8.txt contains the original responses found on the icosahedron (20-sided figure) inside the ball
    infile = open("magic8_responses.txt", 'r')
    list_responses = [line.rstrip() for line in infile]
    infile.close()
    return list_responses

def magic8_again():
    ask_again = input('Would you like to ask Magic8 another question?(y/n) \t')
    ask_again = ask_again.lower()
    
    if ask_again == 'y':
        print('\nMagic8: Oh, you want to know more do you!')
        magic8()
    elif ask_again == 'n':
        print(pattern_magic.format(str('DISAPPEARED INTO')))
        return
    else:
        print('Invalid Entry.\n')
        magic8_again()

print(pattern_magic.format(str('APPEARED FROM')))
magic8()
print('This has been brought to you by: Thorh13')
