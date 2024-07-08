import mysql.connector
# for checking password each and every character
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

# Function for Mail Validation in three parts
# 1.Function for mail validation for part-1 (ex: venkatesh@gmail.com -- venkatesh)

def mail_part_1(username):
    return username.islower() or username.isnumeric()

# 2.Function for mail validation for part-2 and part -3 (ex: venkatesh@gmail.com -- gmail or yahoo, com or in)
def mail_part_2(domain, tld):
    return (len(domain) - 1) >= 1 and tld in ['com', 'in']


# Function for defining parts into three
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


def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Check if the details are in the database
    if check_database(email, password):
        print("Enter into website")
    else:
        print("Details not in database, please register.")
        registration()

# if user forgotten password  then check the database with mail
def forgotten_password():
    email = input("Enter email: ")

    # Check if the email is in the database
    if check_database(email):
        print("Create new password : ")
        new_password = input("Enter new password: ")
        update_password(email, new_password)
        print("Password updated")
    else:
        print("Email not found in database, please register.")
        registration()


# Function to simulate checking the database
def check_database(email, password=None):
    try:
        mydb = mysql.connector.connect(
            user='root',
            host='localhost',
            password='Venkey@123',
            database='sql_connector'
        )
        cursor = mydb.cursor()
        if password:
            query = "SELECT * FROM datainfo WHERE email=%s AND password=%s"
            cursor.execute(query, (email, password))
        else:
            query = "SELECT * FROM datainfo WHERE email=%s"
            cursor.execute(query, (email,))
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        cursor.close()
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