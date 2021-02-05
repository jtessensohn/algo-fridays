const user_num = prompt('Please enter a number: ')

function add_up_to(num) {
    let count = 0
    let equation_array = []
    while (count < user_num) {
        count += 1
        equation_array.append(count)
    }
    print(sum(equation_array))
}

add_up_to(user_num)