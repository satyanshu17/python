win_num=45
num=int(input('Enter the number'))

Game_over=False

while not Game_over:
    if num==win_num:
        print('you won!!!')
        Game_over=True
    else:
        if num<win_num:
            print('too low')
            num=int(input('Enter the number again'))
        else:
            print('too high')
            num=int(input('Enter the number again'))
