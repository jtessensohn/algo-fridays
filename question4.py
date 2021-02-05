from random import randrange

def magic_ball():
    responses = {
        '1': 'Yes',
        '2': 'No',
        '3': 'Maybe one day',
        '4': 'Outlook uncertain',
        '5': 'Ask again later',
    }
    ask_question = input("Ask Magic8 Ball a question: ")
    random_response = str(randrange(4))
    print(responses[random_response])

magic_ball()