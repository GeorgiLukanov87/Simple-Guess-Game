import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Simple -> Guess the number game:
# Simple game , you have 3 shots to pick a number and try to guess what is the computer number.
# Rules: 1 correct number -> You win ! or 3 wrong answers -> You lose !

print(bcolors.HEADER + 'Welcome to the -> "GUESS THE NUMBER" <-' + bcolors.BOLD)
print(bcolors.OKBLUE + 'You need to pick a number between 1 and 9 , Are you ready ? Go !' + bcolors.BOLD)
print()
possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tries = 3
random.shuffle(possible_numbers)
winning_number = possible_numbers[0]

while True:
    try:
        tries -= 1
        print()
        player_number = int(input(bcolors.OKGREEN + 'Pick a number: ' + bcolors.BOLD))
        if player_number == winning_number:
            print(bcolors.OKGREEN + 'Well Done ! You win ! :)')
            break

        else:
            print(bcolors.FAIL + 'Wrong Number ! ' + bcolors.BOLD)
            print(f'{bcolors.FAIL}Try Again -> tries left : {bcolors.HEADER}{tries}{bcolors.BOLD}')

            if winning_number > player_number:
                print(bcolors.OKCYAN + 'JOKER - > Winning number is Bigger!' + bcolors.BOLD)
            else:
                print(bcolors.OKCYAN + 'JOKER - > Winning number is Lower!' + bcolors.BOLD + bcolors.ENDC)
            print()

        if tries == 0:
            print('Sorry, You LOST !:(')
            answer = input('Wanna try again ? -> y / n')
            wrong_answers = 0
            while answer not in ['y', 'n']:
                print('You need to choose -> "y" or "n" !')
                answer = input('"y" or "n"')
                wrong_answers += 1
                if wrong_answers == 2:
                    break

            if answer == 'y':
                tries = 3
                continue
            else:
                print(bcolors.HEADER + 'Program ending...Good Bye!' + bcolors.ENDC)
                break

    except ValueError:
        print(bcolors.WARNING + 'INVALID DATA? , you need to pick a ' + bcolors.HEADER + 'NUMBER!' + bcolors.BOLD)
        tries += 1
        continue
