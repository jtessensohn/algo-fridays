def same_frequency():
    num1 = input("First number: ")
    num2 = input("Second number: ")
    if sorted(num1) == sorted(num2):
        print(True)
    else:
        print(False)

same_frequency()