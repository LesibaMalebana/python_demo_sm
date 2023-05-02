

with open ("exer.txt" ,"r+") as inside_files:
    file_content = inside_files.readlines()
    valid_login = True
    while valid_login:
        user_name = input("Please Enter your User Name.")
        user_password = input("Please Enter the Password.")
        for charlines in file_content:
            username, password = charlines.strip().split(', ')
            if password == user_password and user_name == username:
                valid_login = False
                print("Correct User Name..")
            elif password != user_password and user_name != username:
                print("Enter Correct Log in details")

        # for char_password in file_content:
        #     if password == user_input:
        #         valid_login = True
        #         print("Password Succesful.")
        #
        #         valid_login = True
        #         print("You have logged on to the system.")
        #         break


        # if valid_login:
        #     break
        # else:admin1
        #     print("Incorrect Credentials ,Please try again")
        # elif password == user_input and user_input == user_input:
        #     print("You have logged succesfully")
        # if password == user_input and user_input == username:
        #     print("You have logged on to the system.")
        #     break