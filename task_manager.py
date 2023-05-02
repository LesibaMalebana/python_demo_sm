# =====importing libraries===========


# calling the Datetime function to be used to create date like this 20 Jan 1990
from datetime import date

# ====Login Section====

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

while True:

    menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()  # Converting all the text to lower case

    if menu == 'r' and user_name == 'admin':
        # - Request input of a new username
        enter_user_name = input("Enter a new User .")
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

    elif menu == 'a':
        pass
        # Requesting User input
        task_assigned_to = input("Who are you Assigning the Task To ?")
        # Requesting User input
        task_title = input("What is the name of the Title of the Task ?")
        # Requesting User input
        task_Description = input("Please provide Description of the Task.")
        # Requesting the user to enter a date at a particular
        task_due_now = input("What is the Due date of this Task : E.g 16 Jun 1980")
        # Declaring the date Object adn using the today methods
        task_today_date = date.today()
        # assigned Date object, - re-formating it as per example on the task text file.
        task_today_updated = task_today_date.strftime("%d %b %Y")
        # Requesting User input
        task_completion = "No"
        # Requesting User input`
        with open("tasks.txt", "a+") as task_files:

            # Writing all the variables to the texts file.
            task_files.write(
                f"\n{task_assigned_to}, {task_title}, {task_Description}, {task_due_now}, {task_today_updated}, {task_completion}")
            # closing the Text file after is being used.

            print(" ")
            print("Registry has been filled.")



    elif menu == 'va':
        # Opening/ accessing a text file with the mode : reading and writing
        task_files = open("tasks.txt", "r+")
        # Reading thru the task file thru the variable Task files
        for lines in task_files:
            # spliting the content in the file with coma and space
            tasks_line_details = lines.split(", ")
            # printing out the first index in the file
            # Heading of my table
            print("Task:\t\t\t\t\tAssign Initial Tasks")
            # printing the first index
            print(f"username:\t\t\t\t{tasks_line_details[0]}")
            # printing the fifth index
            print(f"Date assigned:\t\t\t{tasks_line_details[4]}")
            # printing the forth index
            print(f"Due date:\t\t\t\t{tasks_line_details[3]}")
            # printing the last index
            print(f"Task Complete:\t\t\{tasks_line_details[-1]}")
            # printing the third index
            print(f"Task Description: \t\t\t\t \n{tasks_line_details[2]}")
            print("\n")
        # closing the text file tasks

    elif menu == 'vm':
        # Opening/ accessing a text file with the mode : reading and writing
        temp_list = []

        task_files = open("tasks.txt", "r")
        #
        for Line in task_files:
            #
            task_view = Line.split(", ")
            # print(task_view)
            if username == task_view[0]:
                print("Task:\t\t\t\t\tAssign Initial Tasks")
                # printing the first index
                print(f"username:\t\t\t\t{task_view[0]}")
                # printing the first index
                print(f"Date assigned:\t\t\t{task_view[4]}")
                # printing the fifth index
                print(f"Due date:\t\t\t\t{task_view[3]}")
                # printing the forth index
                print(f"Task Complete:\t\t\t{task_view[-1]}")
                # printing the last index
                print(f"Task Description: \t\t\t\t \n{task_view[2]}")
                # printing the third index
                print("\n")
        # closing the text file tasks


    elif menu == 'e':
        print('Goodbye!!!')
        # terminating the program
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
    login_file.close()
