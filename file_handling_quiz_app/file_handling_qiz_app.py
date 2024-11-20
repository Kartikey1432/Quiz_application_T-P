import random as ran


def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass  
    return users


def save_users(users):
    with open("users.txt", "w") as file:
        for username, password in users.items():
            file.write(f"{username},{password}\n")


def load_scores():
    scores = {}
    try:
        with open("scores.txt", "r") as file:
            for line in file:
                username, score = line.strip().split(",")
                scores[username] = int(score)
    except FileNotFoundError:
        pass  
    return scores


def save_scores(scores):
    with open("scores.txt", "w") as file:
        for username, score in scores.items():
            file.write(f"{username},{score}\n")


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
    {"question": "Which of the following function is used to output data in C++?", "choices": ["1. printf()", "2. print()", "3. cout"], "answer": 3},
    {"question": "What is the size of the char data type in C++?", "choices": ["1. 1 byte", "2. 2 bytes", "3. 4 bytes"], "answer": 1},
    {"question": "Which of the following is a correct constructor in C++?", "choices": ["1. MyClass(){}", "2. MyClass{}", "3. MyClass();"], "answer": 1},
    {"question": "Which operator is used to allocate memory dynamically in C++?", "choices": ["1. malloc()", "2. free()", "3. new"], "answer": 3},
    {"question": "What is used to declare a constant in C++?", "choices": ["1. const", "2. #define", "3. both"], "answer": 3}
]


users = load_users()
user_scores = load_scores()

current_user = None

while(True):
    print("""
                    1. Registration
                    2. View Users
                    3. Login
                    4. Attempt Quiz
                    5. Result
                    6. Exit
        """)

    oper = input("Enter the Operation: ")
    print()

    if oper == '1':
        print("          Register Yourself          \n")
        username = input("Enter the user name: ").lower()
        
        print("""
              Your Password Should Contain
                    1. 1 lower case letter
                    2. 1 upper case letter
                    3. 1 digit
                    4. 8 < length < 20
                    5. 1 special character except (@#%_$)
        """)
        while(True):
            userpassword = input("Enter the Password: ")
            length = len(userpassword)
            l, u, d, s = 0, 0, 0, 0
            if(length >= 8 and length <= 20):
                for i in userpassword:
                    if i.islower(): l += 1
                    if i.isupper(): u += 1
                    if i.isdigit(): d += 1
                    if (i in '@' or i in '#' or i in '%' or i in '_' or i in '$'): s += 1
            if username in users:
                print("**********************************************")
                print("You have Already Registered")
                print("**********************************************")
                break
            elif (l >= 1 and u >= 1 and d >= 1 and s >= 1):
                print("**********************************************")
                print("Your Password is Accepted")
                print("**********************************************")
                users[username] = userpassword
                save_users(users)
                print("**********************************************")
                print("Registration Successfully")
                print("**********************************************")
                break
            else:
                print("**********************************************")
                print("Your Password is not Accepted")
                print("**********************************************")
    
    elif oper == '2':
        print(list(users))

    elif oper == '3':
        print("          Login          \n")
        print("------------")
        username = input("Enter the User Name: ").lower()
        password = input("Enter the Password: ")
        print("------------")
        if username in users and users[username] == password:
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
            print(f"{current_user}, let's start the quiz!\n")
            for i, question in enumerate(selected_question):
                print(f"Q{i + 1}: {question['question']}")
                for choice in question['choices']:
                    print(choice)
                answer = int(input("Choose the correct answer (1, 2, or 3): "))
                if answer == question['answer']:
                    score += 1
            print(f"Quiz Over! Your score: {score}/{len(selected_question)}")
            user_scores[current_user] = score
            save_scores(user_scores)
        else:
            print("You need to log in first to attempt the quiz.")

    elif oper == '5':
        print("**********          Result          **********\n")
        if current_user:
            print(f"{current_user}'s score: {user_scores.get(current_user, 0)}")
        else:
            print("Please log in and attempt the quiz first.")

    elif oper == '6':
        break
    else:
        print("Please Enter the Correct option")
