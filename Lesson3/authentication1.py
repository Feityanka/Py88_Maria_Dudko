def get_name():
    username = input('Enter your nickname for a registration.' "\n")
    check_name(username)
    return username
def check_name(name):
    if len(name)<2:
        print("Error. The name is too short. The name must contain more than 1 character.")
        return None
    elif len(name)>10:
        print("Error. The name is too long. The name must contain less than 11 characters.")
        return None
    else:
        return name
name = get_name()
users = ["Feityanka", "Loh", "Yasosbiba", name]
def get_password():
    password = input('Create your password'"\n")
    return password
password = get_password()
while input("Repeat your password:"'\n') != password:
    pass
print("The registration is over. Now you can log-in"'\n')
base = ["Feityanka"+"123", "Loh"+"itaparol", "Yasosbiba"+"clown", name + password]
active = True
while True:
    login = input('Please, enter your username''\n')
    if login in users:
        print(f'Correct')
        break
    else:
        print('Authentication error. Try again.''\n')
active = True
while True:
    login2 = input('Please, enter your password''\n')
    if login+login2 in base:
        print(f'Hello,{login}!')
        break
    else:
        print('Authentication error. Try again.''\n')