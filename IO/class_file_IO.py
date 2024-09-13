# class file

class Todo_list:

    todo_list = []

    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True
    
    def add_todo(self):
        while True:
            new_task = input("할 일을 입력해주세요!(끝 입력시 종료): ")
            if new_task == '끝':
                break
            Todo_list.todo_list.append(new_task)
            with open("C:/Users/SAMSUNG/Desktop/자습/Python/Todo_List_Project/txtsave/todo_list.txt",'w') as file:
                for task_1 in Todo_list.todo_list:
                    file.write(task_1 + '\n')
            with open("C:/Users/SAMSUNG/Desktop/자습/Python/Todo_List_Project/txtsave/todo_list.txt",'r') as file:
                Todo_list.todo_list = [task.strip() for task in file.readlines()]

        print("최신 할 일 목록 :", Todo_list.todo_list)
        
    def taskremove(self):
        while True:
            remove_task = input("삭제할 일을 입력해주세요!(끝 입력시 종료):")
            if remove_task == '끝':
                break
            if remove_task in Todo_list.todo_list:
                Todo_list.todo_list.remove(remove_task)
            if Todo_list.todo_list == []:
                break
            print("최신 할 일 목록 :", Todo_list.todo_list)

    def delete(self):
        import os
        file_path = "C:/Users/SAMSUNG/Desktop/자습/Python/Todo_List_Project/txtsave/todo_list.txt"

        if os.path.exists(file_path):
            os.remove(file_path)

    def print_Todo(self):
        print("현재 할 일 :", Todo_list.todo_list)
