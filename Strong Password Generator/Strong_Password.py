# -----------------------------------------------
# + Author: George Ezat
# ? Date:   08 - 07 - 2025
# -----------------------------------------------

if __name__ == '__main__':
    import string
    import random
    from termcolor import colored as cr

    # -----------------------------------------------

    def header():
        print(cr('-' * 20, color='cyan'))
        print(cr('Password Generator'.center(20), color='cyan'))
        print(cr('-' * 20, color='cyan'))

    # -----------------------------------------------

    def valid_length():
        try:
            length = int(input('Enter password length: ').strip())
            if length > 70:
                raise Exception
            return length
        except:
            print(cr('\nInvalid Length!\n', color='red', attrs=['bold']))
            return valid_length()

    # -----------------------------------------------

    def allow_duplicates():
        duplicates = input('Allow char duplicates? y/N ').strip().upper()
        return duplicates == 'Y'

    # -----------------------------------------------

    def rand_char():
        # Total length of characters is 70
        characters = string.digits + string.ascii_letters + '!@#$%^&*'

        rand_index = random.randint(0, len(characters) - 1)
        char = characters[rand_index]

        return char

    # -----------------------------------------------

    def generate(length, duplicates=True):
        password = ''

        if duplicates:
            while length > 0:
                length -= 1
                char = rand_char()
                password += char

        else:
            while length > 0:
                length -= 1

                while True:
                    char = rand_char()

                    if (char not in password):
                        password += char
                        break

        return password

    # -----------------------------------------------

    def strong_password():
        header()
        print(cr('Info:\n - Maximum length is 70.\n - Duplicates are not allowed by default.', color='yellow'))
        length = valid_length()
        duplicates = allow_duplicates()
        password = generate(length, duplicates)
        print('Your password is:', cr(f"{password}", color='green', attrs=['bold']))

    # -----------------------------------------------

    # App Execution
    strong_password()
