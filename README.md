# Task Manager
### About
This Tax manager applications registers and stores records of users and tasks assigned to them. 
It allows new user to sign up to the account and use their details to sign in to the account and manage it.
A registered User can perform the following tasks using the app:
- Register A User
- Add A Task
- View All Tasks
- View Mine
- Generate Report
- Display Statistics
- Exit the App

## Installation
Any IDE with python interpreter can run this application. Download the file directory on to your local computer
For example a visual studio IDE(VS Code) can open the directory from your destination folder such downloads and display all the files.
In your VS code menu click run and select Run without Debugging. Alternatively you can click Run at the top right corner 
of you VS Code application

## Usage
After Running the application in your Integrated Development Environment (IDE), a user login request will appear in your terminal.
For first time users, enter admin as username and password as your login password. You can crete an acount and use a new password later
#### Register a User
Register a new user by entering a new username and new password. You will be asked to confirm password before accepting your details
and creating your account. You can login with thses details on you next visit. Your user information is saved in the 'user.txt' file.
#### Add a Task
To add a new Task, first log in to your account and proceed to enter the following details upon request. They follow in this order:
- Username
- Title of Task
- Description of Task
- Due Date

Your task complete status is auto set to 'No' which means Not complete. Your Assigned Date is the date when the task is created
Your task is successfully created when your details pass all checks
#### View All Tasks
This menu items lets you view a cataloque of all tasks assigned to All user including you. This enables you to see what others users have been assigned to do.
#### View Mine
Choosing this option will allow you to view all tasks assigned to you only. You can procreed to change your user name, due date and mark the task complete. You can access each task by entering the task number and then edit the task.
#### Generate Report
Selecting this menu item will generate on all tasks and users. This includes:
- Total number of Tasks
- Total and Percentage of tasks completed
- Total and Percentage not Completed
- Total number of users registered
- Percentage and total number Tasks completed by each user
- Percentage and total number uncompleted Tasks by each user
- etc...

#### Display Statistics
This menu item displays total number of tasks assigned and total number of registered users in the task manger app
#### Exit
Exit will close the application

## Credit
This app was a collaboration between my self, Stefan Aikins and the HyperionDev Team. The start and application template was built by 
the HyperionDev Team and I refactored the code and added more functionality to make it complete.
Thanks [HyperionDev](https://www.hyperiondev.com/)

## Future Developments
I look forward to incorporating a Graphical User Interface and adding more functionality.
