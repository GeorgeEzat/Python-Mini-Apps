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
        print(cr('-' * 20, color='cyan'))
        print(cr('Hundred Game'.center(20), color='cyan'))
        print(cr('-' * 20, color='cyan'))

    # -----------------------------------------------

    def instructions():
        header()
        print(cr('Instructions:', color='magenta'))
        print("- This game is a two-player-game.")
        print("- The SUM is zero at the start of the game.")
        print("- Players alternatively add a number between 1 and 10 to the sum.")
        print("- The player who reaches 100 first wins.")
        print(cr('Notes:', color='yellow'))
        print("- When the sum is greater than or equal to 90, a player cannot choose number that makes the sum over 100.")
        print("  e.g. when the sum = 93 you can choose any number between 1 and 7.\n")

    # -----------------------------------------------

    def valid_number(n):
        if n <= 10 and n >= 1:
            return True
        return False

    # -----------------------------------------------

    def valid_input():
        try:
            valid = int(input("Enter a number: "))
            if not valid_number(valid):
                raise Exception
            return valid
        except:
            print(cr('\nInvalid Number!\n', color='red', attrs=['bold']))
            return valid_input()

    # -----------------------------------------------

    def after_90(sum):
        max_add = 100 - sum

        try:
            valid = valid_input()
            if valid > max_add:
                raise Exception
            return valid
        except:
            print(cr('\nInvalid Number!\n', color='red', attrs=['bold']))
            print(cr(f'Note: Maximum input is {max_add}\n', color='yellow'))
            return after_90(sum)

    # -----------------------------------------------

    def player_move(sum):
        if sum > 90:
            player = after_90(sum)
        else:
            player = valid_input()

        sum += player
        header()
        print(f"The sum = {sum}")
        return sum

    # -----------------------------------------------

    def is_finished(sum):
        return sum == 100

    # -----------------------------------------------

    def finished(player_number):
        print(
            cr(f'\nCongrats Player{player_number}! You are the winner ;)\n', color='green', attrs=['bold']))

    # -----------------------------------------------

    def hundred_game():
        instructions()
        input("Press enter to continue...")
        clear_screen()
        header()

        sum, player = 0, 1
        print(f"The sum is {sum}. Let's start now ;)")

        while sum < 100:
            print(cr(f'Player {player}', on_color='on_blue', attrs=['bold']))
            sum = player_move(sum)

            if is_finished(sum):
                finished(player)
                break

            player = 1 if player == 2 else 2

    # -----------------------------------------------

    # Game Execution
    hundred_game()
