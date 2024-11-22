
password_list = []

min_length = 12
min_upper = 3
min_number = 2
min_special = 2

def check_password():
    usr_input = input("\nMake sure to not use something predictable like a birthday or name. Also, you shouldn't reuse passwords between accounts.\nPlease enter a password to test strength: ")
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

    print("\nPassword analysis: ")
    print("- Length:",length,"characters")
    print("- Uppercase letters:", upper_char)
    print("- Numbers:", number)
    print("- Special Characters:", special_character,"\n")

    if length < min_length:
        print("This password is not long enough. It needs at least",min_length,"characters.")
    if upper_char < min_upper:
        print("This password needs more uppercase characters. It needs at least", min_upper,"uppercase characters.")
    if number < min_number:
        print("This password needs more numbers. It needs at least", min_number,"numbers.")
    if special_character < min_special:
        print("This password needs more special characters. It needs at least", min_special, "special characters.")

    if usr_input in words:
        print("\nThis is a very common password. Please try something else.")
    elif (length >= min_length and
        upper_char >= min_upper and
        number >= min_number and
        special_character >= min_special):
        print("\nThis is a strong password!")
    elif not (length >= min_length and
        upper_char >= min_upper and
        number >= min_number and
        special_character >= min_special) and (
        length >= min_length or
        upper_char >= min_upper or
        number >= min_number or
        special_character >= min_special):
        print("\nThis is a moderately strong password. Check the analysis above and change according to that.")
    else:
        print("\nThis is a weak password. Try again after looking at the password analysis. ")


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