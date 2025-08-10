import json
from utils import clear_screen

class TodoApp:
    def __init__(self):
        self.filename = 'tasks.json'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        for i, t in enumerate(self.tasks, start=1):
            status = '✔' if t['done'] else '✘'
            print(f"{i}. {t['task']} [{status}]")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = True
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def run(self):
        while True:
            clear_screen()
            print('--- Todo CLI ---')
            print('1. View tasks')
            print('2. Add task')
            print('3. Mark task done')
            print('4. Delete task')
            print('5. Exit')
            choice = input('Choose an option: ')

            if choice == '1':
                self.view_tasks()
                input('Press Enter...')
            elif choice == '2':
                task = input('Enter task: ')
                self.add_task(task)
            elif choice == '3':
                self.view_tasks()
                index = int(input('Enter task number to mark done: ')) - 1
                self.mark_done(index)
            elif choice == '4':
                self.view_tasks()
                index = int(input('Enter task number to delete: ')) - 1
                self.delete_task(index)
            elif choice == '5':
                break
            else:
                print('Invalid choice')
                input('Press Enter...')