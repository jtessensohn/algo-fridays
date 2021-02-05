def guess_number():
    secret_number = 69
    number_guess = int(input("Hey user! Can you guess the secret number? "))
    if number_guess == secret_number:
        print("Nice.")
    else:
        print("Wrong number!")
        guess_number()

guess_number()