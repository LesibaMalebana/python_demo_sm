

def reg_user():
    with open("user.txt", "a+") as login_file:
        file_content = login_file.readlines()
        if menu == 'r' and user_name == 'admin':
            # - Request input of a new username
            enter_user_name = input("Enter a new User .")

            # Validating a User name:
            for lines in file_content:
                if enter_user_name in lines:
                    print("User Name already exist ,Try another one.")
                # elif enter_user_name != users_name:
                #     login_file.write(enter_user_name)
                #     login_file.write(', ')
                #     login_file.write(enter_confirm_password)
                #     login_file.write("\n")

            # - Request input of password confirmation.
            enter_password = input("Enter password of the New User.")
            # Check if the new password and confirmed password are the same.
            enter_confirm_password = input("Confirm the Password.")
            # accessing the file to the texts in.

            with open("user.txt", "a+") as login_file:

                if enter_password == enter_confirm_password:
                    # task_files = open("tasks.txt", "w")
                    login_file.write(enter_user_name)
                    login_file.write(', ')
                    login_file.write(enter_confirm_password)
                    login_file.write("\n")
                    print("The New User Name has been Added to the Registry..")

                elif enter_password != enter_confirm_password:
                    print("Password Do Not Match ,Try again")
        elif menu == 'r' and user_name != "admin":
            print("You are not the Administrator ,Enter correct log in details.")


 # accessing the text file in read and writing mode.
with open("user.txt", "r+") as login_file:
    # using the readlines function to read from the text file
    file_content = login_file.readlines()
    # condition to keeping the code from running
    valid_login = True
    while valid_login:
        # requesting data from the user and converting all the text to lower case
        user_name = input("Please Enter your user Name:").lower()
        # Requesting Data from the user and converting all the text to lower case
        user_password = input("Please Enter your Password.").lower()
        for charlines in file_content:
            username, password = charlines.strip().split(', ')
            if password == user_password and user_name == username:
                valid_login = False
                print("Great , you have logged on Successfully!!!")
                break
            elif password != user_password and user_name == username:
                continue
            elif password == user_password and user_name != username:
                continue
        else:
            print("Sorry ,Enter the correct Credentials....")



#
# with open ("exer.txt" ,"r+") as inside_files:
#     file_content = inside_files.readlines()
#     while True:
#         user_input = input("Please Enter your User Name.")
#         valid_login = False
#         for charlines in file_content:
#             username, password = charlines.strip().split(', ')
#             if username == user_input:
#                 valid_login = true
#                 print("Correct User Name..")
#         if valid_login:
#             break
#         else:
#             print("Incorrect Credentials ,Please try again")