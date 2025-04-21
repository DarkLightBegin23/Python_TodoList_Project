todo_list = []
while True:
    new_task = input("할 일을 입력해주세요!(끝 입력시 종료): ")
    if new_task == '끝':
        break
    todo_list.append(new_task)

print("최신 할 일 목록 :", todo_list)