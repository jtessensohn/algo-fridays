user_num = int(input('Please enter a number: '))

def add_up_to(num):
    count = 0
    equation_array = []
    while count < user_num:
        count += 1
        equation_array.append(count)
    print(sum(equation_array))

add_up_to(user_num)