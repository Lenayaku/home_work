import random

GREETING = '''
I WANT YOU TO GUESS A NUMBER BETWEEN ONE AND TEN!
PLEASE ENTER THE NUMBER:
'''


def game():
    while True:
        input_data = input(GREETING)
        if input_data == 'q':
            break

        if not input_data.isnumeric():
            print('Invalid data')
            continue

        pc_choice = random.randint(1, 11)
        user_choice = int(input_data)

        if pc_choice == user_choice:
            print("YOU'RE RIGHT! \nCONGRATULATIONS!")
            return True
        else:
                if pc_choice > user_choice:
                    print('MORE! \n Try again!')

                elif pc_choice < user_choice:
                    print('LESS! \n Try again!')





game()