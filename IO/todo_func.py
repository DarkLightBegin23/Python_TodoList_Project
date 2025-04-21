import os

# print(os.getcwd())

class Todo_list:
    todo_list = []  # 클래스 변수로 할 일 목록 관리
    file_path = 'Python_TodoList_Project/txtsave/todo_list.txt'

    def __init__(self, description="Default description"):
        self.description = description

    def import_todo(self):
        """
        파일에서 할 일 목록을 불러와 메모리 변수에 저장합니다.
        """
        if os.path.exists(self.file_path):  # exists 메소드 사용
            with open(self.file_path, 'r') as file:
                Todo_list.todo_list = [task.strip() for task in file.readlines()]
            print("할 일 목록이 파일에서 불러와졌습니다:", Todo_list.todo_list)
        else:
            print("할 일 목록 파일이 존재하지 않습니다.")

    def add_todo(self, tasks):
        """
        할 일 목록을 파일에 저장하고, 메모리 변수에 업데이트합니다.
        """
        with open(self.file_path, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        
        # 파일에서 다시 읽어 최신화
        self.import_todo()

    def delete_task(self):
        """
        사용자 입력을 기반으로 할 일 목록에서 항목 삭제 후 파일에 업데이트.
        """
        self.import_todo()  # 파일에서 최신 할 일 목록 불러오기

        if not Todo_list.todo_list:
            print("삭제할 할 일이 없습니다.")
            return

        while True:
            print(f"현재 할 일 목록: {Todo_list.todo_list}")
            remove_task = input("삭제할 할 일을 입력하세요 (끝 입력시 종료): ")

            if remove_task == '끝':
                print("삭제 작업이 종료되었습니다.")
                break

            if remove_task in Todo_list.todo_list:
                Todo_list.todo_list.remove(remove_task)
                print(f"'{remove_task}' 항목이 삭제되었습니다.")
            else:
                print(f"'{remove_task}' 항목을 찾을 수 없습니다.")

            # 할 일 목록이 비었으면 종료
            if not Todo_list.todo_list:
                print("할 일 목록이 비었습니다. 작업을 종료합니다.")
                break

        # 파일에 최신 목록을 다시 저장
        with open(self.file_path, 'w') as file:
            for task in Todo_list.todo_list:
                file.write(task + '\n')
        print("변경된 할 일 목록이 파일에 저장되었습니다.")

    def print_todo(self):
        """
        현재 메모리에 있는 할 일 목록을 출력합니다.
        """
        if Todo_list.todo_list:
            print("현재 할 일:", Todo_list.todo_list)
        else:
            print("할 일이 없습니다.")
