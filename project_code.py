
password_list = []

def check_password():
    usr_input = input("\nPlease enter a password to test strength: ")
    special_characters = "~`!@#$%^&*()_-+={[}]|:;'<,>.?/"
    length = 0
    upper_char = 0
    lower_char = 0
    special_character = 0
    number = 0

    with open('/users/jacobwhite/downloads/10-million-password-list-top-1000000.txt', 'r') as f:
        words = f.read().splitlines()

    for char in usr_input:
        length += 1
        if char.isupper():
            upper_char +=1
        elif char.islower():
            lower_char += 1
        elif char in special_characters:
            special_character += 1
        elif char.isdigit():
            number +=1

    pct_upper = round(float((upper_char/length)*100), 2)
    pct_special = round(float((special_character/length)*100), 2)
    pct_number = round(float((number/length)*100), 2)

    if usr_input not in words:
        while length > 12:
            if pct_upper > 20:
                print("\nGood amount of capital letters")
                if pct_number > 10:
                    print("\nGood amount of numbers")
                    if pct_special > 10:
                        print("\nGood amount of special characters")
                    else:
                        print("\nYou should try again with more special characters")
                else:
                    print("\nYou should try again with more numbers")
            else:
                print("\nYou should try again with more uppercase characters")
            break
    else:
        print("\nThis is a common password, try again with something different")
                    

    print("\nMake sure you did not use something predictable like a birthday or name. Also, you shouldn't reuse passwords.")


def add_password():

    password_to_add = input('\nEnter password you want to add to database. ')
    if password_to_add not in password_list:
        print('Adding '+password_to_add)
        password_list.append(password_to_add)
        print(password_list)
    else:
        print('\nPassword already in list. ')


def remove_password():
    password_to_remove = input("\nWhich password do you want to remove? ")
    if password_to_remove in password_list:
        print('Removing '+password_to_remove)
        password_list.remove(password_to_remove)
        print(password_list)
    else:
        print('Password not found. Please try again. ')

def show_passwords():
    print("\n",password_list)

def main():
    while True:
        print("""
        Welcome to the Password Checker

        [1] - Check Password
        [2] - Add Password
        [3] - Remove Password
        [4] - Show Passwords
        [5] - Exit
        """)

        action = input('\nWhat would you like to do? (Enter a number) ')
        
        if action == '1':
            check_password()
        elif action == '2':
            add_password()
        elif action == '3':
            remove_password()
        elif action == '4':
            show_passwords()
        elif action == '5':
            exit()
        else:
            print("\nPlease enter valid option")
        
if __name__ == '__main__':
    main()