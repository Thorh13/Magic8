from random import randrange

##what to add
# confirmation of if that is their question where if the answer no they will be asked again (Questioning)
# after question has be answered ask if they would like another question to be answered(done)
# recognize a 42 reference and respond with a custom reponse (done)
# add custom list of "intros" (Requested by: Lamar "Goku" Brooks) (done)
# add custom list of "questions" to inform user to ask a question. (Requested by: (Requested by: Lamar "Goku" Brooks)
# add custom list of "acknowledgements" when user wants to ask more questions. (Requested by: Lamar "Goku" Brooks)

pattern_magic = '\n*POOF* MAGIC8 HAS JUST {} THE SHADOWS!!! *POOF*\n'
pattern_respond = '\nMagic8: So that\'s what you want to know, is that right?\nMagic8: Well, {}\n'

def magic8_intro():
    list_of_intros = get_list_of_intros()
    num = int(randrange((int(len(list_of_intros))-1)))
    intro = list_of_intros[num]
    print('Magic8: {}'.format(intro))
    magic8()

def magic8():
    question = str(magic8_question())
    if "meaning of life" in question:
        response = pattern_respond.format(str(42))
    else:
        response = pattern_respond.format(str(magic8_response()))
    print(response)
    magic8_again()

def magic8_question():
    question = input('Ask Magic8 a question: \t')
    return question

def magic8_response():
    list_of_responses = get_list_of_responses()
    num = int(randrange((int(len(list_of_responses))-1)))
    response = list_of_responses[num]
    return response

def magic8_again():
    
    #ask user if they would like to ask another question
    ask_again = input('Would you like to ask Magic8 another question?(y/n) \t')
    
    #make it lowercase so program has less to check for
    ask_again = ask_again.lower()

    if ask_again == 'y': #did they put Y or y for Yes ifso ask for another question
        print('\nMagic8: Oh, you want to know more do you!')
        magic8()
        
    elif ask_again == 'n': #did they put N or n for No, end program
        print(pattern_magic.format(str('DISAPPEARED INTO')))
    
    else: #anything else inform them they did not put Y or N and ask again
        print('Invalid Entry.\n')
        magic8_again()

def get_list_of_intros():
    # The File magic8_intros.txt contains the the list of intros
    infile = open("magic8_intros.txt", 'r')
    list_intros = [line.rstrip() for line in infile]
    infile.close()
    return list_intros

def get_list_of_responses():
    # The File magic8_responses.txt contains the original responses found on the icosahedron (20-sided figure) inside the ball
    infile = open("magic8_responses.txt", 'r')
    list_responses = [line.rstrip() for line in infile]
    infile.close()
    return list_responses
#=================================================================
        
print(pattern_magic.format(str('APPEARED FROM')))
magic8_intro()
print('This has been brought to you by: Thorh13')
