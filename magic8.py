from random import randrange

##what to add
#confirmation of if that is their question where if the answer no they will be asked again
# after question has be answered if tey would like another question to be answered
# reconize a 42 reference with custome reponse
pattern_respond = 'Magic8: So that\'s what you want to know, is that right?\nMagic8: Well, {}'

def magic8():
    magic8_question()
    response = pattern_respond.format(str(magic8_response()))
    print(response)

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
    infile = open("magic8.txt", 'r')
    list_responses = [line.rstrip() for line in infile]
    infile.close()
    return list_responses

magic8()
