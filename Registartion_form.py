import mysql.connector

# Class for password validation
class Password:
    def __init__(self, pas):
        self.pas = pas
        self.error_messages = []

    def upper(self):
        if any(65 <= ord(i) <= 90 for i in self.pas):  # Uppercase letters
            return True
        self.error_messages.append("At least one uppercase letter is required in the password.")
        return False

    def lower(self):
        if any(97 <= ord(i) <= 122 for i in self.pas):  # Lowercase letters
            return True
        self.error_messages.append("At least one lowercase letter is required in the password.")
        return False

    def number(self):
        if any(48 <= ord(i) <= 57 for i in self.pas):  # Digits
            return True
        self.error_messages.append("At least one number is required in the password.")
        return False

    def special(self):
        if any(32 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or 123 <= ord(i) <= 126 for i in
               self.pas):  # Special characters
            return True
        else:
            self.error_messages.append("At least one special character is required in the password.")
            return False

    def validate(self):
        return self.upper() and self.lower() and self.number() and self.special()


# Function for mobile verification
def mobile_verify(num):
    return len(num) == 10 and num.isdigit()


# Function for mail validation part-1 (username)
def mail_part_1(username):
    return username.islower() or username.isnumeric()


# Function for mail validation part-2 (domain) and part-3 (tld)
def mail_part_2(domain, tld):
    return (len(domain) - 1) >= 1 and tld in ['com', 'in']


# Function to verify email
def email_verify(email):
    try:
        username = email[:email.index('@')]
        domain = email[email.index('@') + 1:email.index('.')]
        tld = email[email.index('.') + 1:]
        return mail_part_1(username) and mail_part_2(domain, tld)
    except ValueError:
        return False

# Registration function
def registration():
    f_name = input("Enter first name:\n")
    l_name = input("Enter last name:\n")
    m_no = input("Enter mobile number:\n")
    mail = input("Enter email:\n")
    password_input = input("Enter a password:\n")

    # Validate inputs
    password_obj = Password(password_input)
    mobile_valid = mobile_verify(m_no)
    email_valid = email_verify(mail)
    password_valid = password_obj.validate()

    # Check validations and print appropriate messages
    if mobile_valid and email_valid and password_valid:
        # Insert into the database
        try:
            mydb = mysql.connector.connect(
                user='root',
                host='localhost',
                password='Venkey@123',
                database='sql_connector'
            )
            cursor = mydb.cursor()
            query = '''
                INSERT INTO datainfo (email, password)
                VALUES (%s, %s)
            '''
            data = (mail, password_input)
            cursor.execute(query, data)
            mydb.commit()
            print("Registration Successful!")
            # Prompt for login or exit
            next_action = input("Do you want to log in now? (yes/no): ").strip().lower()
            if next_action == 'yes':
                login()
            else:
                print("Exiting the program. Goodbye!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            mydb.close()
    else:
        if not mobile_valid:
            print("Invalid mobile number. It must be exactly 10 digits.")
        if not email_valid:
            print("Invalid email format.")
        if not password_valid:
            print("Password validation failed:")
            for msg in password_obj.error_messages:
                print("-", msg)


# Function for login
def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Check if the details are in the database
    login_result = check_database(email, password)
    if login_result == "login_success":
        print("Enter into website")

    elif login_result == "password_incorrect":
        print("Password does not match")
        forgot_password = input("Forgot password? (yes/no): ").strip().lower()
        if forgot_password == 'yes':
            forgotten_password(email)
    else:
        print("Details not in database, please register.")
        registration()


# Function to handle forgotten password
def forgotten_password(email=None):
    if not email:
        email = input("Enter email: ")
    # Check if the email is in the database
    if check_database(email) == "email_exists":
        print("Create new password : ")
        new_password = input("Enter new password: ")
        pass_obj = Password(new_password)
        password_valid = pass_obj.validate()
        if password_valid:
            update_password(email, new_password)
            print("Password updated")
            # Prompt for login or exit
            next_action = input("Do you want to log in now? (yes/no): ").strip().lower()
            if next_action == 'yes':
                login()
            else:
                print("Exiting the program. Goodbye!")
        else:
            print("Password validation failed:")
            for msg in pass_obj.error_messages:
                print("-", msg)

                # again for creating password
                print("Create new password : ")
                new_password = input("Enter new password: ")
                pass_obj = Password(new_password)
                password_valid = pass_obj.validate()
                if password_valid:
                    update_password(email, new_password)
                    print("Password updated")
                    # Prompt for login or exit
                    next_action = input("Do you want to log in now? (yes/no): ").strip().lower()
                    if next_action == 'yes':
                        login()
                    else:
                        print("Exiting the program. Goodbye!")
    else:
        print("Email not found in the database.")


# Function to simulate checking the database

# Function to simulate checking the database
def check_database(email, password=None):
    try:
        mydb = mysql.connector.connect(
            user='root',
            host='localhost',
            password='Venkey@123',
            database='sql_connector'
        )

        with mydb.cursor() as cursor:
            # Check if the email exists
            query = "SELECT password FROM datainfo WHERE email=%s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()

            if result is None:
                # Email does not exist
                return "email_not_found"

            stored_password = result[0]

            if password:
                if stored_password != password:
                    # Email exists but password does not match
                    return "password_incorrect"
                else:
                    # Email and password match
                    return "login_success"
            else:
                # Email exists, password not checked
                return "email_exists"

    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")
        return "error"

    finally:
        if mydb.is_connected():
            mydb.close()


# Function to update the password in the database
def update_password(email, new_password):
    try:
        mydb = mysql.connector.connect(
            user='root',
            host='localhost',
            password='Venkey@123',
            database='sql_connector'
        )
        cursor = mydb.cursor()
        query = "UPDATE datainfo SET password=%s WHERE email=%s"
        cursor.execute(query, (new_password, email))
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        mydb.close()


# Main function to handle user interaction
def main():
    user_action = int(input("Enter\n1 --> Registration \n2 --> Login \n3 --> Forgotten Password\n"))

    if user_action == 1:
        registration()
    elif user_action == 2:
        login()
    elif user_action == 3:
        forgotten_password()
    else:
        print("Invalid option, please try again.")


# Run the main function
if __name__ == "__main__":
    main()
