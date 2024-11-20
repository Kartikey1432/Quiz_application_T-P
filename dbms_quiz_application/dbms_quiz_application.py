import random as ran
import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='1234',  
            database='quiz_app'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def register_user(username, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            if user:
                print("You have already registered.")
            else:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                connection.commit()
                print("Registration successful!")
        except Error as e:
            print(f"Error while registering user: {e}")
        finally:
            cursor.close()
            connection.close()


def login_user(username, password):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            if user and user[0] == password:
                return True
            else:
                return False
        except Error as e:
            print(f"Error while logging in: {e}")
            return False
        finally:
            cursor.close()
            connection.close()


def save_score(username, score):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT username FROM scores WHERE username = %s", (username,))
            existing_score = cursor.fetchone()
            if existing_score:
                cursor.execute("UPDATE scores SET score = %s WHERE username = %s", (score, username))
            else:
                cursor.execute("INSERT INTO scores (username, score) VALUES (%s, %s)", (username, score))
            connection.commit()
        except Error as e:
            print(f"Error while saving score: {e}")
        finally:
            cursor.close()
            connection.close()


def get_score(username):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT score FROM scores WHERE username = %s", (username,))
            score = cursor.fetchone()
            if score:
                return score[0]
            else:
                return 0
        except Error as e:
            print(f"Error while fetching score: {e}")
            return 0
        finally:
            cursor.close()
            connection.close()


python_quiz_questions = [
    {"question": "In which year was the Python language developed?", "choices": ["1. 1991", "2. 1985", "3. 1885"], "answer": 1},
    {"question": "In which language is Python written?", "choices": ["1. Java", "2. C", "3. PHP"], "answer": 2},
    {"question": "Which one of the following is the correct extension of the Python file?", "choices": ["1. .python", "2. .p", "3. .py"], "answer": 3},
    {"question": "Single Line comments in Python begin with Symbol", "choices": ["1. #", "2. @", "3. %"], "answer": 1},
    {"question": "Which of the Following are the fundamental building block of python Programming", "choices": ["1. Constants", "2. Tokens", "3. Identifiers"], "answer": 2},
    {"question": "The reserved words used by Python Interpreter to recognize the structure of the Program are termed as", "choices": ["1. Tokens", "2. Literals", "3. Keywords"], "answer": 3},
    {"question": "What can be the maximum possible length of the Identifier", "choices": ["1. 31", "2. 79", "3. None of these"], "answer": 3},
    {"question": "Which of the following statement is correct about List", "choices": ["1. List can contain value of mixed data type", "2. A List with no element is called empty List", "3. All of these"], "answer": 3},
    {"question": "Which operator can be used with List", "choices": ["1. in", "2. not in", "3. both (1) & (2)"], "answer": 3},
    {"question": "Which of the following commands will create a list", "choices": ["1. List=list()", "2. List1=[]", "3. All of these"], "answer": 3}
]


java_quiz_questions = [
    {"question": "Which of the following is the correct way to declare a Java variable?", "choices": ["1. int x;", "2. x int;", "3. variable x int;"], "answer": 1},
    {"question": "Which keyword is used to define a class in Java?", "choices": ["1. class", "2. define", "3. create"], "answer": 1},
    {"question": "What is the default value of a boolean variable in Java?", "choices": ["1. false", "2. true", "3. null"], "answer": 1},
    {"question": "What does JVM stand for in Java?", "choices": ["1. Java Virtual Machine", "2. Java Variable Machine", "3. Java Value Model"], "answer": 1},
    {"question": "Which of the following is not a primitive data type in Java?", "choices": ["1. int", "2. String", "3. double"], "answer": 2},
    {"question": "What is the size of the float data type in Java?", "choices": ["1. 4 bytes", "2. 8 bytes", "3. 2 bytes"], "answer": 1},
    {"question": "Which method is used to start a thread in Java?", "choices": ["1. run()", "2. start()", "3. begin()"], "answer": 2},
    {"question": "Which of the following is the parent class of all classes in Java?", "choices": ["1. Object", "2. Class", "3. Super"], "answer": 1},
    {"question": "Which of the following is the correct way to declare an array in Java?", "choices": ["1. int[] arr;", "2. int arr[];", "3. both of these"], "answer": 3},
    {"question": "Which keyword is used to create an object of a class in Java?", "choices": ["1. new", "2. create", "3. make"], "answer": 1}
]

cplus_quiz_questions = [
    {"question": "Which of the following is used to declare a pointer in C++?", "choices": ["1. *", "2. &", "3. %"], "answer": 1},
    {"question": "Which of the following is the correct syntax to include a header file in C++?", "choices": ["1. #include <iostream>", "2. include <iostream>", "3. #include <stdio.h>"], "answer": 1},
    {"question": "What is the default value of a static variable in C++?", "choices": ["1. 0", "2. NULL", "3. undefined"], "answer": 1},
    {"question": "Which operator is used to access members of a class in C++?", "choices": ["1. .", "2. ::", "3. ->"], "answer": 1},
    {"question": "Which of the following is used to allocate memory dynamically in C++?", "choices": ["1. malloc()", "2. calloc()", "3. new"], "answer": 3},
    {"question": "Which of the following is a constructor in C++?", "choices": ["1. ClassName()", "2. void ClassName()", "3. constructor()"], "answer": 1},
    {"question": "Which of the following is not a valid C++ loop?", "choices": ["1. for", "2. while", "3. loop"], "answer": 3},
    {"question": "Which of the following is used to handle exceptions in C++?", "choices": ["1. try-catch", "2. try-except", "3. catch-throw"], "answer": 1},
    {"question": "Which keyword is used to define a class in C++?", "choices": ["1. class", "2. struct", "3. object"], "answer": 1},
    {"question": "Which of the following can be used to return multiple values in C++?", "choices": ["1. array", "2. tuple", "3. pointers"], "answer": 3}
]


current_user = None
while True:
    print("""
        1. Registration
        2. View Users
        3. Login
        4. Attempt Quiz
        5. Result
        6. Exit
    """)
    oper = input("Enter the Operation: ")
    
    if oper == '1':
        print("          Register Yourself          \n")
        username = input("Enter the user name: ").lower()
        password = input("Enter the password: ")
        register_user(username, password)
    
    elif oper == '2':
        print("Users List:")
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT username FROM users")
            users = cursor.fetchall()
            for user in users:
                print(user[0])
            cursor.close()
            connection.close()

    elif oper == '3':
        print("          Login          \n")
        username = input("Enter the User Name: ").lower()
        password = input("Enter the Password: ")
        if login_user(username, password):
            current_user = username
            print(f"Login successful! Welcome, {username}")
        else:
            print("Invalid User Name or Password")
    
    elif oper == '4':
        print("          Attempt Quiz          \n")
        if current_user:
            subject = input("Choose the subject (Python/Java/C++): ").lower()
            if subject == 'python':
                selected_question = ran.sample(python_quiz_questions, 5)
            elif subject == 'java':
                selected_question = ran.sample(java_quiz_questions, 5)
            elif subject == 'c++':
                selected_question = ran.sample(cplus_quiz_questions, 5)
            else:
                print("Invalid subject choice.")
                continue

            score = 0
            for i, question in enumerate(selected_question):
                print(f"Q{i + 1}: {question['question']}")
                for choice in question['choices']:
                    print(choice)
                answer = int(input("Choose the correct answer (1, 2, or 3): "))
                if answer == question['answer']:
                    score += 1

            print(f"Quiz Over! Your score: {score}/{len(selected_question)}")
            save_score(current_user, score)
        else:
            print("You need to log in first to attempt the quiz.")

    elif oper == '5':
        print("**********          Result          **********\n")
        if current_user:
            score = get_score(current_user)
            print(f"{current_user}'s score: {score}")
        else:
            print("Please log in and attempt the quiz first.")

    elif oper == '6':
        break

    else:
        print("Please enter the correct option")
