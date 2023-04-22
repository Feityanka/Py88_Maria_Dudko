import json

with open("db.json", "r") as f_json:
    data = json.load(f_json)


def check_name(data):
    """Here we are getting a nickname for a new users registration and checking it for individuality"""
    active = True
    while active:
        username = input('Enter your nickname for a registration.' "\n")
        if username in data.keys():
            print("This nickname is already taken")
        elif 10 < len(username) or 2 > len(username):
            print("The name must consists of less than 10 chars and more than 1")
        else:
            return username


def get_password():
    password = input('Create your password'"\n")
    while input("Repeat your password:"'\n') != password:
        pass
    print("The registration is over. Now you can log-in"'\n')
    return password


def login():
    active = True
    while active:
        login = input('Please, enter your username''\n')
        if login in data.keys():
            print(f'Correct')
            break
        else:
            print('Authentication error. Try again.''\n')
    while active:
        login2 = input('Please, enter your password''\n')
        if (login, login2) in data.items():
            print(f'Hello,{login}!')
            break
        else:
            print('Authentication error. Try again.''\n')


answer = input("Are you already registered?"'\n')
"""Here we are asking if the user is already registered. If 'yes', we are starting the logging function. And if not, 
we are starting the registration function"""
if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes' or answer == '+':
    def login():
        active = True
        while active:
            login = input('Please, enter your username''\n')
            if login in data.keys():
                print(f'Correct')
                break
            else:
                print('Authentication error. Try again.''\n')
        while active:
            login2 = input('Please, enter your password''\n')
            if (login, login2) in data.items():
                print(f'Hello,{login}!')
                break
            else:
                print('Authentication error. Try again.''\n')
    login()
else:
    username = check_name(data)
    password = get_password()
    data[username] = password
    with open('db.json', 'w', encoding='utf8') as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False))
    login()

