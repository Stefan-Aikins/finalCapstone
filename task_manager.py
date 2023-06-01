# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(
        task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


# ====Login Section====
'''This code reads usernames and password from the user.txt file to
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    user = user.split(';')
    username = user[0]
    password = user[1]
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True
 # this function register a user


def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = input("New Username: ")
    # this condition will not allow users to duplicate an existing username
    while new_username in username_password.keys():
        print('Username already exist, try again!')
        # - Request input of a new username
        new_username = input("New Username: ")
        # proceed to ask password when username does not already exist
        if new_username not in username_password.keys():
            print('Username accepted')
            continue
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")


def add_task():
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following:
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and
             - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")

    while task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        # continue to ask for username until a valid username is entered
        task_username = input("Name of person assigned to task: ")
        if task_username in username_password.keys() is False:
            continue

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    global curr_date
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    task_list_to_write = []
    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


# the user should access a particular task by entering the task number
disp_task_list = []
mark_list_to_write = []
usr_list_to_write = []
dt_list_to_write = []

# this function will change the due date of a task


def change_due_date():
    while True:
        try:
            new_due_date = input("\nNew Due date for this task (YYYY-MM-DD): ")
            new_due_date_time = datetime.strptime(
                new_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
        with open('tasks.txt', 'w') as task_file:
            disp_task_list[task_num_access -
                           1][3] = new_due_date_time.strftime(DATETIME_STRING_FORMAT)
            for dt in disp_task_list:
                dt_list_to_write.append(';'.join(dt))
            task_file.write('\n'.join(dt_list_to_write))
            print("Due Date successfully updated!")
            break


'''this function will update the user name and write to the tasks.txt file
    The ptogram will proceed according to the usder's choice
    The user is allowed to decide whether to change or keep user name'''


def edit_username():
    choice = input('\nDo you want to change your username?: ').lower()
    if choice == 'no':
        print(
            f'Great!, you have decided to keep your username {disp_task_list[task_num_access-1][0]}\n')
    if choice == 'yes':
        usr_name = input('Please enter a new username: ')
        # update the task file
        with open('tasks.txt', 'w') as task_file:
            # clearlist items in this list to avoid duplications when running the app again without closing it
            usr_list_to_write = []
            disp_task_list[task_num_access-1][0] = usr_name
            for line in disp_task_list:
                usr_list_to_write.append(';'.join(line))
            task_file.write('\n'.join(usr_list_to_write))
            print("username successfully updated!")


def access_and_edit_task():
    # making these variables various accessible in the entire program
    global task_num_access
    global list_of_tasks
    global sub_ls

    with open('tasks.txt', 'r') as task_file:
        task_data = task_file.readlines()
        for line in task_data:
            sub_ls = line.strip().split(';')
            disp_task_list.append((sub_ls))

    while True:
        try:
            # the program will proceed only when the user enters an integer
            task_num_access = int(input(f'''\nwhich task number do you want to access?
Enter [ -1 ] to return to main menu: '''))
            '''return to main menu when user enters -1
            return to main menu when user is not assigned to that task'''
            if task_num_access == -1:
                print('\nBack to Main Menu!\n')
                break
            # user cannot access information from a task that they are not assigned
            if disp_task_list[task_num_access-1][0] != curr_user:
                print(f'\n{curr_user}, you are not assigned to this task!\n')
                break

        except ValueError:
            print('Invalid input!, Please enter a number.')

        '''Display the task requested by the user
            Allow user to maker further request'''

        # if disp_task_list[task_num_access-1][0] != curr_user:
        #     print(f'\n{curr_user}, you are not assigned to this task!\n')
        #     break

        for number in range(0, len(disp_task_list)):
            if number == task_num_access-1:
                if disp_task_list[task_num_access-1][0] == curr_user:
                    print(f'''
        Task: {task_num_access}
Task: {disp_task_list[task_num_access-1][1]}
Assigned to: {disp_task_list[task_num_access-1][0]}
Task Description: {disp_task_list[task_num_access-1][2]}
Date Assigned: {disp_task_list[task_num_access-1][3]}
Due Date: {disp_task_list[task_num_access-1][4]}
Completed: {disp_task_list[task_num_access-1][5]}''')

                    '''This function enables user to change their username and mark a specifi task complete
                        User can only change username if the task is incomplete'''
                    if disp_task_list[task_num_access-1][5].lower() == 'yes':
                        print('This task is complete')
                    else:
                        # mark task complete or return to main menu when tasks is already complete
                        mark_complete = input(
                            '\nDo you want to mark this task complete?: ').lower()
                        while mark_complete != 'yes' or mark_complete != 'no':
                            if mark_complete == 'no':
                                print(
                                    f'''Thank you! {disp_task_list[task_num_access-1][0]}, you have decided to complete this task later''')
                                # Edit the username
                                edit_username()
                                change_due_date()
                                break
                            elif mark_complete == 'yes':
                                with open('tasks.txt', 'w') as task_file:
                                    disp_task_list[task_num_access -
                                                   1][5] = 'Yes'
                                    for item in disp_task_list:
                                        mark_list_to_write.append(
                                            ';'.join(item))
                                    task_file.write(
                                        '\n'.join(mark_list_to_write))
                                    print("Task successfully completed!")
                                # Edit the username
                                edit_username()
                                change_due_date()
                                break
                            else:
                                print('Goodbye!')
                                break


def view_mine():
    user = ''
    ts_num = 0
    while user != curr_user:
        user = input(
            '''\nPlease enter your username to view all tasks assigned to you: 
            
[ NB: username should match login details ]: ''')
        if user == curr_user:
            '''assign numbers to the the tasks. The numbers can be user to access task for editing
                display all tasks assigned to a specific username'''
            with open('tasks.txt', 'r') as task_file:
                task_data = task_file.readlines()
            for line in task_data:
                sub_ls = line.strip().split(';')
                # display all tasks that matches the username entered
                ts_num += 1
                if user == sub_ls[0]:
                    print(f'''
            Task: {ts_num}
    Task: {sub_ls[1]}
    Assigned to: {sub_ls[0]}
    Task Description: {sub_ls[2]}
    Date Assigned: {sub_ls[3]}
    Due Date: {sub_ls[4]}
    Completed: {sub_ls[5]}''')

    # Access a task by entering its number
    access_and_edit_task()
# This function will generate report


sub_task_data = []
sub_user_data = []


def generate_reports():
   # Create task_overview.txt if it doesn't exist
    if not os.path.exists('task_overview.txt'):
        with open("task_overview.txt", "w") as task_overview_file:
            pass

    # Use the information collected to generate the report
    with open('tasks.txt', 'r') as task_file:
        task_data = task_file.read().split('\n')
        for ts in task_data:
            sb_ts = ts.split(';')
            sub_task_data.append(sb_ts)

    total_completed = 0
    total_not_completed = 0
    # display the total number of tasks completed
    for t in sub_task_data:
        if t[5] == 'Yes':
            total_completed += 1
        elif t[5] == 'No':
            total_not_completed += 1

    # today's date
    today = datetime.now()
    datetime.strptime(
        task_components[3], DATETIME_STRING_FORMAT)

    # assigned = datetime.strptime(sub_task_data[4], DATETIME_STRING_FORMAT)
    # due = datetime.strptime(sub_task_data[3], DATETIME_STRING_FORMAT)

    # date_complete = datetime.strptime(
    #     '2023-06-01', DATETIME_STRING_FORMAT).date()

    # percentage overdue calculations
    total_overdue_tasks = 0
    total_task_overdue_not_completed = 0
    total_task_overdue_completed = 0
    total_tasks_overdue_not_completed_by_user = 0
    for overdue in sub_task_data:
        if overdue[5] == 'Yes' and overdue[4] > overdue[3]:
            total_task_overdue_completed += 1
        if overdue[5] == 'No' and overdue[4] > overdue[3]:
            total_task_overdue_not_completed += 1
        if overdue[4] > overdue[3]:
            total_overdue_tasks += 1
        if overdue[5] == 'No' and overdue[4] > overdue[3] and overdue[0] == curr_user:
            total_tasks_overdue_not_completed_by_user += 1

            # display task report
    task_report = f'''
    Task Report:
Total number of completed tasks: {total_completed}
Total number of Uncompleted Tasks: {total_not_completed}
Percentage of Completed Tasks: {round((total_completed / len(sub_task_data)) * 100)}%
Percentage of Incomplete tasks: {round((total_not_completed / len(sub_task_data)) * 100)}%
Percentage of Total Task Overdue: {round(total_overdue_tasks / len(sub_task_data) * 100)}%
Percentage of Total Task Overdue Not Completed: {round(total_task_overdue_not_completed / len(sub_task_data) * 100)}%
Percentage of Total Task Overdue Completed: {round(total_task_overdue_completed / len(sub_task_data) * 100)}%
Total number of Tasks: {len(sub_task_data)}'''

    # write to the text file
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write(task_report)
    print(task_report)

    # Create user_overview.txt if it doesn't exist
    if not os.path.exists("user_overview.txt"):
        with open("user_overview.txt", "w") as user_overview_file:
            pass

    # Use the information collected to generate the report
    with open('user.txt', 'r') as user_file:
        user_data = user_file.read().split('\n')
        for usr in user_data:
            usr_dt = usr.strip().split(';')
            sub_user_data.append(usr_dt)

    # percentage total number of tasks assigned to the current user
    total_completed_by_user = 0
    total_not_completed_by_user = 0

    for user in sub_task_data:
        if user[5] == 'Yes' and user[0] == curr_user:
            total_completed_by_user += 1

        if user[5] == 'No' and user[0] == curr_user:
            total_not_completed_by_user += 1

    # Percentage calculations for user
    percentage_completed = (total_completed_by_user / len(sub_task_data)) * 100
    percentage_not_completed = (
        total_not_completed_by_user/len(sub_user_data)) * 100

    total_tasks_assigned = 0

    for user_d in sub_task_data:
        if user_d[0] == curr_user:
            total_tasks_assigned += 1
            percentage_of_tasks_assigned = (
                total_tasks_assigned / len(sub_task_data)) * 100

    user_report = f'''
    User Report
Total number of registered users: {len(user_data)}
Total number of Tasks: {len(sub_task_data)}

    {curr_user}'s Report:
Total number of Tasks Assigned to user: {total_tasks_assigned}
Percentage of Tasks Assigned: {round(percentage_of_tasks_assigned)}%
Percentage of Tasks completed: {round(percentage_completed)}%
Percentage Tasks Not completed: {round(100 - percentage_not_completed)}%
Percentage Tasks Not completed and Overdue {round((total_tasks_overdue_not_completed_by_user/ len(sub_task_data)) * 100)}%
    '''
    # percentage not yet completed and over

    # write to the user_overview.txt file
    with open('user_overview.txt', 'w') as user_overview_file:
        user_overview_file.write(user_report)

    print(user_report)


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    # generate report is a new addition to the menu
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        # register a new user
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)

    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine()

    elif menu == 'gr':
        generate_reports()

    elif menu == 'ds' and curr_user == 'admin':
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        with open('tasks.txt', 'r') as task_file:
            task_data = task_file.read().split('\n')

        with open('user.txt', 'r') as user_file:
            user_data = user_file.read().split('\n')

        num_users = len(user_data)
        num_tasks = len(task_data)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
