# -----------------------------------------------
# + Author: George Ezat
# ? Date:   08 - 07 - 2025
# -----------------------------------------------

if __name__ == '__main__':
    import os
    from termcolor import colored as cr

    # ---------------------------------------------------

    def header():
        print(cr('-' * 20, color='cyan'))
        print(cr('Factors Calculator'.center(20), color='cyan'))
        print(cr('-' * 20, color='cyan'))

    # ---------------------------------------------------

    def valid_number():
        try:
            valid = int(input("Enter a number: "))
            return valid
        except:
            print(cr('\nInvalid Number!\n', color='red', attrs=['bold']))
            return valid_number()

    # ---------------------------------------------------

    def calc_factors():
        num = valid_number()
        if num > 0:
            factors = [i for i in range(1, num + 1) if num % i == 0]
        elif num < 0:
            factors = [i for i in range(-1, num - 1, -1) if num % i == 0]
        else:
            print(cr('Zero has no factors!', color='yellow'))
            return

        print(cr(f'Factors of {num} are: {factors}', attrs=['bold']))

    # ---------------------------------------------------

    def factors_calculator():
        header()
        calc_factors()

    # ---------------------------------------------------

    # App Execution
    factors_calculator()

