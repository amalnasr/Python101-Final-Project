def search(number):

    all_numbers = {'1111111111': 'Amal', '2222222222': 'Mohammed', '3333333333': 'Khadijah',
                   '4444444444': 'Abdullah', '5555555555': 'Rawan', '6666666666': 'Faisal',
                   '7777777777': 'Layla'}

    if number in all_numbers:
        print('This number for: '+all_numbers[number])
    elif (number.isdecimal() == False) or (len(number) < 10):
        print('This is invalid number')
    else:
        print('Sorry, the number is not found')


print('Welcome to Phone Directory!!!')
phone_number = input('Enter the number you want:')
search(phone_number)


