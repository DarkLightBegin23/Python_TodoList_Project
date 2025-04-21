class Savefile():
    def __init__(self, file_todo_list):
        self.file_todo_list = file_todo_list

    def filesave():
        todo_list = []
        todo_list_add = input()
        todo_list.append(todo_list_add)
        
        with open("Python_TodoList_Project/txtsave/todo_list.txt",'w') as file:
            for task_1 in todo_list:
                file.write(task_1 + '\n')
            with open("Python_TodoList_Project/txtsave/todo_list.txt",'r') as file:
                todo_list = [task.strip() for task in file.readlines()]