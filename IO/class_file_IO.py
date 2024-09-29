# class file

class Todo_list:

    todo_list = []

    def __init__(self, description="Default description"):  # 기본 값을 설정
        self.description = description

    def mark_done(self):
        self.done = True
    
    def add_todo(self, tasks):
        file_path = 'C:/Users/SAMSUNG/Desktop/자습/Python/Todo_List_Project/txtsave/todo_list.txt'

        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(task + '\n') 
        with open(file_path,'r') as file:
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
