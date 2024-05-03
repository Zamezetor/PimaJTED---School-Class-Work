# Logan White 05/02/1014
# 05-02-2024_D2L_Code_Debugging_Arrays.py
# Debugshi 
# CC BY-NC-SA 4.0


# This program gets the user's first name, last name, and
# student ID number. Using this data it generates a
# system login name.

import login

def main():
    # Get the user's first name, last name, and ID number.
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')

    # Get the login name.
    print('Your system login name is:')
    print(login.get_login_name(first, last, idnumber))
    
# Call the main function.
if ___name___ == '___main___':
    main()


# ---------------------------------------------------------------------------------------------------------

# This program gets a password from the user and
# validates it.

import login

def main():
    # Get a password from the user.
    password = input('Enter your password: ')

    # Validate the password.
    while not login.valid_password(Password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

# Call the main function.
if __name__ == '__main__':
    main()


