todo_list = ['공부', '운동']

while True:
    remove_task = input("삭제할 일을 입력해주세요!(끝 입력시 종료):")
    if remove_task == '끝':
        break
    if remove_task in todo_list:
        todo_list.remove(remove_task)
    if todo_list == []:
        break
print("최신 할 일 목록 :", todo_list)