# Registration_Form

## User Registration and Login System
========================================
# Overview
This project is a simple User Registration and Login system implemented in Python. It includes functionality for validating user inputs, storing user data in a sql Database, and handling user authentication.

## Features
=====================================
# step - 1: -  User Registration
---------------------------------
Validates the username (email format).
Validates the password based on specified criteria.
Stores valid user credentials in a file.

# step -2:-  User Login
-----------------------------------
Authenticates user credentials against the stored data.
Provides options for password retrieval or reset.

# step 3:-  Registration
-------------------------------------
To register a new user:
Enter a valid email address and password as prompted.
Username (Email) Validation Rules
Must contain "@" followed by "."
Valid Examples: sherlock@gmail.com, nothing@yahoo.in
Invalid Examples: @gmail.com, my@.in
Must not start with special characters or numbers
Invalid Examples: 123#@gmail.com
Password Validation Rules
Length must be between 6 and 16 characters.
Must contain at least one special character.
Must contain at least one digit.
Must contain at least one uppercase letter.
Must contain at least one lowercase letter.

# Login
To log in with an existing user:

Enter your username and password as prompted.
Forgot Password
If you forgot your password:

Choose the "Forgot Password" option during login.
Provide your username.
You will be prompted to set a new one if the user mail exists in the database.
