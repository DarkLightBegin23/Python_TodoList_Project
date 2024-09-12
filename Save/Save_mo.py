todo_list = ["공부하기"]

with open("todo_list.txt",'w') as file:
    for task_1 in todo_list:
        file.write(task_1 +"\n")

with open("todo_list.txt",'r') as file:
    todo_list = file.readlines()