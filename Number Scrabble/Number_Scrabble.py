# -----------------------------------------------
# + Author: George Ezat
# ? Date:   08 - 07 - 2025
# -----------------------------------------------

if __name__ == '__main__':
    import os
    from termcolor import colored as cr

    # -----------------------------------------------

    def clear_screen():
        if os.name == 'nt':  # 'nt' refers to Windows
            os.system('cls')
        else:  # 'posix' for Unix-like systems (Linux, macOS)
            os.system('clear')

    # -----------------------------------------------

    def header():
        clear_screen()
        print(cr('-' * 21, color='cyan'))
        print(cr('Number Scrabble'.center(21), color='cyan'))
        print(cr('-' * 21, color='cyan'))

    # -----------------------------------------------

    def instructions():
        header()
        print(cr('Instructions:', color='magenta', attrs=['bold']))
        print("- Two players take turns picking numbers from 1 to 9, without repeating any number.")
        print("- Each player tries to collect any three numbers that add up to 15.")
        print("- On your turn, enter a number from the available list.")
        print("- If a player gets any combination of three numbers that sum to 15, they win.")
        print("- If all numbers are picked and no one wins, the game ends in a draw.")
        print("- Good luck and have fun!\n")

    # -----------------------------------------------

    def valid_number(numbers, pick):
        if pick in numbers:
            return True
        return False

    # -----------------------------------------------

    def valid_pick(numbers):
        try:
            pick = int(input("Pick a number: "))
            if not valid_number(numbers, pick):
                raise Exception
            return pick
        except:
            print(cr('\nInvalid Pick!\n', color='red', attrs=['bold']))
            return valid_pick(numbers)

    # -----------------------------------------------

    def is_win(player):
        player_picks = set(player)

        possible_wins = [{1, 5, 9}, {2, 4, 9}, {1, 6, 8}, {2, 5, 8}, {3, 4, 8}, {2, 6, 7}, {3, 5, 7}, {4, 5, 6}]

        for i in possible_wins:
            if i.issubset(player_picks):
                return True

        return False

    # -----------------------------------------------

    def finished(player_number):
        print(cr(f'\nCongrats Player{player_number}! You are the winner ;)\n', color='green', attrs=['bold']))

    # -----------------------------------------------

    def number_scrabble():
        instructions()
        input("Press enter to continue...")
        header()

        numbers = [i for i in range(1, 10)]
        player_one = []
        player_two = []

        var = player_one

        while len(numbers) > 0:
            header()
            print(cr(f'Available Numbers: {numbers}', attrs=['bold']))
            print(cr(f'Player 1: {player_one}', on_color='on_blue', attrs=['bold']))
            print(cr(f'Player 2: {player_two}', on_color='on_yellow', attrs=['bold']))

            pick = valid_pick(numbers)
            numbers.pop(numbers.index(pick))

            var.append(pick)
            if is_win(var):
                finished((len(numbers) % 2) + 1)
                return

            var = player_one if var == player_two else player_two

        print(cr('DRAW!', color='yellow', attrs=['bold']))

    # -----------------------------------------------

    # Game Execution
    number_scrabble()
