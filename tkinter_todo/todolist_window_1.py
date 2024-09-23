import tkinter
import tkinter.messagebox

todolist_window = tkinter.Tk()

todolist_window.title("Todo List")  # 제목
todolist_window.geometry("640x480+100+100")  # 창 크기 좌표
todolist_window.resizable(True, True)  # 창 크기 조절 여부(상하, 좌우)

title=tkinter.Label(todolist_window, text="Todo List 항목을 작성해주세요", width=25, height=5, fg="black", relief="ridge",bg="cyan")  # tltie 위젯 설정
title.pack()

def input_Todo():
    tkinter.messagebox.showinfo("메시지를 입력하세요")

def list_in_Todo():
    inputs = ent.get()  # Entry에서 입력받은 값을 가져옴
    if inputs:  # 입력된 값이 있을 때만 실행
        listbox.insert(tkinter.END, inputs)  # Listbox의 마지막에 입력값을 추가
        ent.delete(0, tkinter.END)  # 입력 필드를 초기화
        print(f'입력된 값: {inputs}')

listbox = tkinter.Listbox(todolist_window, selectmode='extended', height=0)
listbox.pack(pady=10)

ent = tkinter.Entry(todolist_window, width=30)
ent.pack(pady=10)

button = tkinter.Button(todolist_window, text="입력", width=15, command=list_in_Todo)
button.pack(pady=10)  # 위아래로 패딩 10을 추가하여 배치

todolist_window.mainloop()