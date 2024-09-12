# class file
todo_list = []

class Todo_list:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True
    
    def add(self):
        while True:
            new_task = input("할 일을 입력해주세요!(끝 입력시 종료): ")
            if new_task == '끝':
                break
            todo_list.append(new_task)
        print("최신 할 일 목록 :", todo_list)
        
    def delete(self):

        while True:
            remove_task = input("삭제할 일을 입력해주세요!(끝 입력시 종료):")
            if remove_task == '끝':
                break
            if remove_task in todo_list:
                todo_list.remove(remove_task)
            if todo_list == []:
                break
            print("최신 할 일 목록 :", todo_list)

    def printTodo():
        print("현재 할 일 :", todo_list)
