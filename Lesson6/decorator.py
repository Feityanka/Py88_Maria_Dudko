from datetime import datetime


def some_decorator(what_time):
    def the_wrapper():
        current_datetime = datetime.now()
        time = datetime.now()
        print(time)
        what_time()
        print(time)

    return the_wrapper


@some_decorator
def some_function():
    username = input('Hello! What is your name?''\n')
    print(f'Hello, {username}!')
    return username


some_function()


@some_decorator
def more_questions():
    decision = input('Nice! And mine is Mary. Do you like cats?''\n')
    if decision == 'Yes' or decision == 'yes' or decision == 'y' or decision == 'Y':
        print('Yay! Same')
    else:
        print('Boo-hoo! And I do love them!')
    return decision


questionmark = more_questions()
