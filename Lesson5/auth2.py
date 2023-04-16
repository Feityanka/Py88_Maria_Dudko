Users = {
    'Feityanka': 'Clownnumber1',
    'Yasos': 'Biba',
    'Yazagit': 'Lera'
}


def get_name():
    username = input('Enter your nickname for a registration.' "\n")
    check_name(username)
    return username


def check_name(name):
    if len(name) < 2:
        print("Error. The name is too short. The name must contain more than 1 character.")
        return
    elif len(name) > 10:
        print("Error. The name is too long. The name must contain less than 11 characters.")
        return
    else:
        return name


name = get_name()


def get_password():
    password = input('Create your password'"\n")
    return password


password = get_password()

while input("Repeat your password:"'\n') != password:
    pass
print("The registration is over. Now you can log-in"'\n')

Users.update({
    name: password
})

active = True
while True:
    login = input('Please, enter your username''\n')
    login2 = input('Please, enter your password''\n')
    if login and login2 in Users.values():
        print(f'Hello, {login}!')
        break
    else:
        print('Authentication error. Try again.''\n')
