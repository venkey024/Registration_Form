# Registration_Form

## User Registration and Login System
========================================
# Overview
This project is a simple User Registration and Login system implemented in Python. It includes functionality for validating user inputs, storing user data in a sql Database, and handling user authentication.

## 📘Features
========================================

1.**User Registration**
   - Validates the username (email format), first name, last name, and mobile number.
   - Validates the password based on specified criteria.
   - Stores valid user credentials in a database.

2.**User Login**
   - Authenticates user credentials against the stored data.
   - Provides options for password retrieval or reset.

3.**Forgot Password**
   - Allows users to reset their password.

# 📗Usage
## Step 1: Provide an Input
Upon running the main script, the user will be prompted to choose one of the following options. If no input is provided, the script will not run.

    - Registration - Press 1
    - Login - Press 2
    - Forgot Password - Press 3

## Step 2: Runs Based on Input Provided by User
**If User Provides 1 - Registration**

**Enter the following details as prompted**

    - First Name
    - Last Name
    - Mobile Number
    - Email Address 
    - Password

**First Name and Last Name Validation Rules**

   - Must not be empty.
     
   - Must not contain special characters or numbers.

**Mobile Number Validation Rules**

   - Must be a valid phone number format (e.g., 10 digits for US numbers).
   
   - Must not contain letters or special characters.

**E-mail Validation Rules**

   - Must contain "@" followed by "."

   - Valid Examples: sherlock@gmail.com, nothing@yahoo.in

**Invalid Examples: @gmail.com, my@.in**

Must not start with special characters or numbers

**Invalid Examples: 123#@gmail.com**

**Password Validation Rules**

   - Length must be between 6 and 16 characters.
   - Must contain at least one special character.
   - Must contain at least one digit.
   - Must contain at least one uppercase letter.
   - Must contain at least one lowercase letter.

**If User Provides 2 - Login**

   - Enter your username and password as prompted.

**If User Provides 3 - Forgot Password**

   - Provide your E-mail.
   - You will be prompted to set a new one if the username exists in the database
