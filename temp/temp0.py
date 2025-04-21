from IO.todo_func import Todo_list

task1 = Todo_list()

task1.add_todo(["공부"])  # 항목 받을 때 문자열의 경우 리스트로 받기
task1.print_Todo()


'''
def add_todo(self, file):
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
'''