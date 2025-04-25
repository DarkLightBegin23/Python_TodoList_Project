import tkinter as tk
import tkinter.messagebox
from IO.todo_func import Todo_list

todolist_window = tk.Tk()

todolist_window.title("Todo List")  # 제목
todolist_window.geometry("640x400+100+100")  # 창 크기 좌표
todolist_window.resizable(True, True)  # 창 크기 조절 여부(상하, 좌우)

title=tk.Label(todolist_window, text="Todo List 항목을 작성해주세요", width=25, height=5, fg="black", relief="ridge",bg="skyblue")  # tltie 위젯 설정
title.pack()

def input_Todo():
    tk.messagebox.showinfo("메시지를 입력하세요")

def list_in_Todo():
    inputs = ent.get()  # Entry에서 입력받은 값을 가져옴
    print(f"입력값: {inputs}")  # 사용자 입력값을 출력하여 확인
    if inputs:  # 입력된 값이 있을 때만 실행
        listbox.insert(tk.END, inputs)  # Listbox의 마지막에 입력값을 추가
        ent.delete(0, tk.END)  # 입력 필드를 초기화
    else:
        print("입력 값이 없습니다.")

def finish():
    tasks = listbox.get(0, tk.END)  # Listbox의 모든 항목을 가져옴
    Todofile = Todo_list()  # Todo_list 클래스의 인스턴스 생성
    Todofile.todo_list.add_todo(tasks)  # add_todo 메서드에 할 일 목록 전달
    tk.messagebox.showinfo("저장 완료", "할 일 목록이 파일에 저장되었습니다.")


# 삭제 메서드 투두리스트 파일 액션과 연결 필요

def delete_selected():
    tasks = listbox.get(0, tk.END)
    selected_items = listbox.curselection()  # 선택된 항목의 인덱스 가져오기
    for index in selected_items[::-1]:  # 역순으로 삭제
        task = tasks.listbox.get(index)
        tasks.listbox.delete(index)
        tasks.todo_list.todo_list.remove(task)  # 메모리 목록에서도 삭제

scrollBar = tk.Scrollbar(todolist_window)

listbox = tk.Listbox(todolist_window, selectmode='single', height=0)
listbox.config(yscrollcommand=scrollBar.set)

listbox.pack(pady=10)

DeleteButton = tk.Button(todolist_window, text="항목 선택 후 삭제", width=20, command=lambda: delete_selected()) 
# 참조만이 아닌 호출도 할 수 있도록 처리 (command=sss -> command=sss())
DeleteButton.pack()

scrollBar.config(command=listbox.yview)

ent = tk.Entry(todolist_window, width=30)
ent.pack(pady=40)

button = tk.Button(todolist_window, text="입력", width=15, command=list_in_Todo)
button.pack(pady=10)  # 위아래로 패딩 10을 추가하여 배치

button = tk.Button(todolist_window, text="끝", width=15, command=finish)
button.pack(pady=10)

scrollBar.pack(side="right", fill="y")

todolist_window.mainloop()