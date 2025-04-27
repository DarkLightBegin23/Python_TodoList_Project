import os
import sys

# print(os.getcwd())

class Todo_list:
    
    """PyInstaller 환경에서도 파일 경로를 정확히 잡아주는 함수"""
    
    def resource_path(relative_path):
        try:
            # PyInstaller로 패키징 된 경우
            base_path = sys._MEIPASS
        except Exception:
        # 개발 환경(파이썬으로 직접 실행)인 경우
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    todo_list = []  # 클래스 변수로 할 일 목록 관리
    file_path = "./txtTodo/TodoList.txt"
    
    file_name = resource_path("todo_list.txt")
    
    # 파일이 없으면 새로 생성
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write("")
    else:
        pass

    # 파일 읽기
    with open(file_name, 'r', encoding='utf-8') as f:
        contents = f.readlines()
        # 파일 내용 todo_list에 저장
        todo_list.extend(contents)


    def __init__(self, description="Default description"):
        self.description = description
        
    def import_todo(self):
        """
        파일에서 할 일 목록을 불러와 메모리 변수에 저장합니다.
        
        1. 파일이 저장될 디렉토리가 존재하는지 확인합니다.
        2. 디렉토리가 없다면 새로 생성합니다.
        3. 할 일 목록 파일이 존재하는지 확인합니다.
        4. 파일이 없다면 빈 파일을 생성합니다.
        5. 파일을 읽어 각 줄을 리스트 요소로 저장합니다.
        """

        # self.file_path에서 디렉토리 경로만 추출합니다.
        dir_path = os.path.dirname(self.file_path)

        # 디렉토리가 존재하지 않으면 새로 생성합니다.
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)  # makedirs는 상위 경로까지 자동으로 생성합니다.

        # 할 일 목록 파일이 존재하지 않으면 빈 파일을 생성합니다.
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                pass  # 빈 파일을 만들어 놓기만 합니다.

        # 파일을 읽기 모드로 열어, 한 줄씩 읽어 리스트에 저장합니다.
        with open(self.file_path, 'r') as file:
            # 파일의 각 줄에서 개행문자를 제거하고 리스트에 저장합니다.
            Todo_list.todo_list = [task.strip() for task in file.readlines()]

        # 불러온 할 일 목록을 출력합니다 (디버깅 및 확인용).
        print("할 일 목록이 파일에서 불러와졌습니다:", Todo_list.todo_list)
        
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
