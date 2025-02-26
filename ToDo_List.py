from datetime import date

# masha changes

class User:

    max_tasks_renamed = 10000  #  was 10

    def __init__(self, login, username, password):
        """
        Initialize a user
        """
        self.login = login
        self.username = username
        self.password = password
        self.tasks = []
        self.date_history = {}

    def add_task(self, task, task_date=None):
        """
        Add a task to the user's to-do list.
        """
        if len(self.tasks) < self.max_tasks:
            if task_date is None:
                task_date = date.today()
            if task_date not in self.date_history:
                self.date_history[task_date] = []
            self.date_history[task_date].append({'task': task, 'completed': False})
            self.tasks.append({'task': task, 'completed': False})
            return 'Task added!'
        else:
            return 'Day overloaded. Maybe plan this one for another day? You might burn out!'

    def show_tasks(self, task_date=None):
        """
        Show tasks for the chosen date or all tasks if date not mentioned
        """
        if task_date is None:
            return [(task['task'], task['completed']) for task in self.tasks]
        elif task_date in self.date_history:
            return [(task['task'], task['completed']) for task in self.date_history[task_date]]
        else:
            return 'No tasks for this date.'

    def delete_task(self, number, task_date=None):
        """
        Delete a task by its number and chosen date.
        """
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
        """
        Mark a task as completed by its number and chosen date.
        """
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
    """
    Create a new user and add to the users dict.
    """
    print('Great day to make new friends!')
    login = input('\tLogin: ')
    if login in users:
        print('Login already exists. Please think of a different one.')
        return None

    password = input('\tPassword: ')
    username = input('\tAnd how should I call you? ')
    users[login] = User(login, username, password)
    print(f'We are friends now, {username}!')
    return users[login]


def log_in(users):
    """
    Log in as an existing user from the users dict.
    """
    print('Good to see you again.')
    login = input('\tLogin: ')
    password = input('\tPassword: ')
    user = users.get(login)
    if user and user.password == password:
        print(f"Welcome back, {user.username}! \nLet's get to the planning!")
        return user
    else:
        print('Incorrect login or password. Try again.')
        return None


def add_task(user):
    """
    Add a task for the logged-in user.
    """
    task_date = input('Date (YYYY-MM-DD) for the task: ')
    task = input('To do: ')
    if task_date:
        task_date = date.fromisoformat(task_date)
    else:
        task_date = date.today()
    print(user.add_task(task, task_date))


def show_tasks(user):
    """
    Show tasks for a chosen date or all tasks if no date mentioned.
    """
    task_date = input('Date (YYYY-MM-DD) of the task: ')
    if task_date:
        task_date = date.fromisoformat(task_date)
    tasks = user.show_tasks(task_date)
    if isinstance(tasks, str):
        print(tasks)
        return

    print(f'Tasks for {task_date}:')
    for task_num, (task, completed) in enumerate(tasks, start=1):
        if completed:
            print(f"{task_num}. {task.replace('', '\u0336')}")
        else:
            print(f'{task_num}. {task}')

    if not tasks:
        print('No plans for this day.')


def delete_task(user):
    """
    Delete a task for the logged-in user.
    """
    task_date_input = input('Date (YYYY-MM-DD) of the tasks: ')
    if task_date_input:
        try:
            task_date = date.fromisoformat(task_date_input)
        except ValueError:
            print("Invalid date format. Here are all your tasks.")
            task_date = None
    else:
        task_date = None

    tasks = user.show_tasks(task_date)
    if isinstance(tasks, str):
        print(tasks)
        return

    print(f'Tasks for {task_date}:')
    for task_num, task in enumerate(tasks, start=1):
        print(f'{task_num}. {task[0]}')

    if not tasks:
        print('No tasks found.')
        return

    while True:
        choice = input("Delete task number ('cancel' to go back): ").lower()
        if choice == 'cancel':
            print('Going back.')
            return

        if choice.isdigit():
            number = int(choice) - 1
            if 0 <= number < len(tasks):
                confirm = input(f"Delete task '{tasks[number][0]}' (yes/no)?: ").lower()
                if confirm == 'yes':
                    user.delete_task(number, task_date)
                    print('Task deleted successfully!')
                    return
                elif confirm == 'no':
                    print('Going back.')
                    return
                else:
                    print("Didn't catch that. Delete task '{tasks[number][0]}'? (yes/no):")
            else:
                print("Invalid task number. Try again")
        else:
            print("Didn't catch that. Delete task '{tasks[number][0]}' (yes/no) ('cancel' to go back)?: ")


def complete_task(user):
    """
    Mark a task as completed for the logged-in user.
    """
    task_date_input = input('Date (YYYY-MM-DD) of the tasks: ')

    if task_date_input:
        try:
            task_date = date.fromisoformat(task_date_input)
        except ValueError:
            print('Invalid date format. Here are all your tasks.')
            task_date = None
    else:
        task_date = None

    tasks = user.show_tasks(task_date)
    if isinstance(tasks, str):
        print(tasks)
        return

    print(f'Tasks for {task_date}:')
    for task_num, (task, completed) in enumerate(tasks, start=1):
        if completed:
            print(f"{task_num}. {task.replace('', '\u0336')}")
        else:
            print(f'{task_num}. {task}')

    if not tasks:
        print('No tasks found.')
        return

    while True:
        choice = input("Done task number ('cancel' to go back): ").lower()
        if choice == 'cancel':
            print('Cancelled.')
            return

        if choice.isdigit():
            number = int(choice) - 1
            if 0 <= number < len(tasks):
                if user.complete_task(number, task_date):
                    print('Task marked as completed!')
                    return
                else:
                    print("Didn't catch that. Try again.")
            else:
                print("Invalid task number. Try again.")
        else:
            print("Didn't catch that. What task number mark as done ('cancel' to go back)?:")


print('-' * 10)
print('Welcome to your to-do list - a minimalistic guide to help you get through the day and plan the ones that are coming!')
print('-' * 10)

def main():
    """
    Main entry point.
    """

    users = {}

    while True:
        choice = input('\nWhat would you like to do today?\n\t1. Sign up\n\t2. Log in\n\t3. Exit\n')

        if choice == '1' or choice.lower() == 'sign up':
            user = create_user(users)
            if user:
                logged_in = True
        elif choice == '2' or choice.lower() == 'log in':
            user = log_in(users)
            if user:
                logged_in = True
        elif choice == '3' or choice.lower() == 'exit':
            print('Have a good rest of your planned day!')
            break
        else:
            print("Didn't catch that.")

        if logged_in:
            while True:
                print('\nWhat would you like to do now?\n\t1. Add a task\n\t2. Show tasks\n\t3. Delete a task\n\t4. Complete a task\n\t5. Log out\n')
                option = input()

                if option == '1' or option.lower() == 'add a task':
                    add_task(user)
                elif option == '2' or option.lower() == 'show tasks':
                    show_tasks(user)
                elif option == '3' or option.lower() == 'delete a task':
                    delete_task(user)
                elif option == '4' or option.lower() == 'complete a task':
                    complete_task(user)
                elif option == '5' or option.lower() == 'log out':
                    print(f'Logged out {user.username}.')
                    break
                else:
                    print("Didn't catch that.")
main()
