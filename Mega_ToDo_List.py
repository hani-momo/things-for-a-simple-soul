from datetime import date
class User:
    max_tasks = 10

    def __init__(self, login, username, password):
        self.login = login
        self.username = username
        self.password = password
        self.tasks = []
        self.date_history = {}

    def add_task(self, task, task_date=None):
        if len(self.tasks) < self.max_tasks:
            if task_date is None:
                task_date = date.today()
            if task_date not in self.date_history:
                self.date_history[task_date] = []
            self.date_history[task_date].append({'task': task, 'completed': False})
            self.tasks.append({'task': task, 'completed': False})
            return 'Task added!'
        else:
            return 'Day overloaded. Maybe plan this one for another day?'

    def show_tasks(self, task_date=None):
        if task_date is None:
            return [(task['task'], task['completed']) for task in self.tasks]
        elif task_date in self.date_history:
            return [(task['task'], task['completed']) for task in self.date_history[task_date]]
        else:
            return 'No tasks for this date.'

    def delete_task(self, number, task_date=None):
        if task_date is None:
            if 0 <= number < len(self.tasks):
                del self.tasks[number]
                return True
            else:
                return 'No such task!'
        else:
            if task_date in self.date_history and 0 <= number < len(self.date_history[task_date]):
                del self.date_history[task_date][number]
                return True
            else:
                return 'No such task!'

    def complete_task(self, number, task_date=None):
        if task_date is None:
            if 0 <= number < len(self.tasks):
                self.tasks[number]['completed'] = True
                return True
            else:
                return 'No such task!'
        else:
            if task_date in self.date_history and 0 <= number < len(self.date_history[task_date]):
                self.date_history[task_date][number]['completed'] = True
                return True
            else:
                return 'No such task!'



def create_user(users):
    login = input('Great day to make new friends! Think of a login: ')
    if login in users:
        print('Someone already has a login like this. Think of a different one: ')
        return None

    password = input('Good! Now for a password: ')
    username = input('We are almost there!\nNow how can I call you? ')
    users[login] = User(login, username, password)
    print(f'We are friends now, {username}!')
    return users[login]


def log_in(users):
    login = input('Login: ')
    password = input('Password: ')
    user = users.get(login)
    if user and user.password == password:
        print(f'Welcome back, {user.username}!')
        return user
    else:
        print('Something is wrong. Try again. ')
        return None


def add_task(user):
    task = input('New task: ')
    task_date = input('Date (YYYY-MM-DD) for the task. Leave blank for today: ')
    if task_date:
        task_date = date.fromisoformat(task_date)
    else:
        task_date = date.today()
    print(user.add_task(task, task_date))


def show_tasks(user):
    task_date = input('Date (YYYY-MM-DD) of the task or leave blank to see all tasks: ')
    if task_date:
        task_date = date.fromisoformat(task_date)
    tasks = user.show_tasks(task_date)
    if isinstance(tasks, str):
        print(tasks)
        return

    print(f'Tasks for {task_date}:')
    for task_num, (task, completed) in enumerate(tasks, start=1):
        if completed:
            print(f'{task_num}. {task} \u0336')  # Display completed tasks with strikethrough
        else:
            print(f'{task_num}. {task}')

    if not tasks:
        print('No tasks on this day.')


def delete_task(user):
    task_date = input('Date (YYYY-MM-DD) of the task or leave blank for today: ')
    if task_date:
        task_date = date.fromisoformat(task_date)
    tasks = user.show_tasks(task_date)
    if isinstance(tasks, str):
        print(tasks)
        return

    print(f'Tasks for {task_date}:')
    for task_num, task in enumerate(tasks):
        print(f'{task_num}. {task["task"]}')

    if not tasks:
        print('No tasks on this day.')
        return

    while True:
        choice = input("Task under what number to delete ('cancel' to go back)? ").lower()
        if choice == 'cancel':
            print('Going back!')
            return

        if choice.isdigit():
            number = int(choice)
            confirm = input(f"Delete '{tasks[number]['task']}'? (yes/no): ").lower()
            if confirm == 'yes':
                user.delete_task(number, task_date)
                print('Task deleted!')
                return
            elif confirm == 'no':
                print('Going back!')
                return
            else:
                print("Please answer 'yes' or 'no': ")


def complete_task(user):
    task_date = input('Date (YYYY-MM-DD) of the task or leave blank for today: ')
    if task_date:
        task_date = date.fromisoformat(task_date)
    tasks = user.show_tasks(task_date)
    if isinstance(tasks, str):
        print(tasks)
        return

    print(f'Tasks for {task_date}:')
    for task_num, task in enumerate(tasks):
        print(f'{task_num}. {task}')

    if not tasks:
        print('No tasks on this day.')
        return

    while True:
        choice = input("Task under what number to mark as completed ('cancel' to go back)? ").lower()
        if choice == 'cancel':
            print('Going back!')
            return

        if choice.isdigit():
            number = int(choice)
            confirm = input(f"Mark '{tasks[number]}' as completed? (yes/no): ").lower()
            if confirm == 'yes':
                user.complete_task(number, task_date)
                print('Task marked as completed!')
                return
            elif confirm == 'no':
                print('Marking as completed canceled.')
                return
            else:
                print("Please answer 'yes' or 'no': ")



print('\n' + '-' * 10 + '\nWelcome to your to-do list - a minimalistic guide to help you get through the day and plan the ones that are coming!\n' + '-' * 10)
users = {}

logged_in = False
# main loop
while True:
    choice = input('\nWhat are we doing today?\n\t1. Sign up\n\t2. Log in\n\t3. Exit\n')

    if choice == '1' or choice.lower() == 'sign up':
        user = create_user(users)
        if user:
            logged_in = True
    elif choice == '2' or choice.lower() == 'log in':
        user = log_in(users)
        if user:
            logged_in = True
    elif choice == '3' or choice.lower() == 'exit':
        print('Bye-bye!')
        break
    else:
        print("Sorry, I didn't catch that.")

    if logged_in:
        while True:
            action = input('\nWhat are we doing here?\n\t1. Add task\n\t2. Show tasks\n\t3. Delete task\n\t4. Mark done task\n\t5. Log out\n')

            if action == '1' or action.lower() == 'add task':
                add_task(user)
            elif action == '2' or action.lower() == 'show tasks':
                show_tasks(user)
            elif action == '3' or action.lower() == 'delete task':
                delete_task(user)
            elif action == '4' or action.lower() == 'mark done task':
                complete_task(user)
            elif action == '5' or action.lower() == 'log out':
                print('See you around!')
                break
            else:
                print("\nSorry, I didn't catch that. What are we doing here?")

        logged_in = False
