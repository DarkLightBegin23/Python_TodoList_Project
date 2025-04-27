import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
from IO.todo_func import Todo_list

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("640x480+100+100")

        self.todo_list = Todo_list()
        
        title = tk.Label(root, text="Todo List 항목을 작성해주세요", width=25, height=5, fg="black", relief="ridge", bg="ivory")
        title.pack()

        self.listbox = tk.Listbox(root, selectmode='extended', height=0)
        self.listbox.pack(pady=10)

        # 할 일 추가 버튼
        add_button = tk.Button(root, text="할 일 추가", width=15, command=self.add_todo_popup)
        add_button.pack(pady=10)

        # 할 일 삭제 버튼
        delete_button = tk.Button(root, text="선택 항목 삭제", width=15, command=self.delete_selected_todo)
        delete_button.pack(pady=10)

        # 완료 버튼
        finish_button = tk.Button(root, text="저장", width=15, command=self.finish)
        finish_button.pack(pady=10)

        quit_button = tk.Button(root, text="종료", width=15, command=self.retryButton)
        quit_button.pack(pady=10)
        
        # 할 일 목록 초기화
        self.refresh_listbox()

    def add_todo_popup(self):
        """
        팝업창을 통해 할 일을 입력받아 목록에 추가합니다.
        """
        task = tk.simpledialog.askstring("할 일 추가", "추가할 할 일을 입력하세요:")  # "창 이름", "페이지 안의 글씨"
        if task:  # 입력값이 있을 때만 추가
            self.listbox.insert(tk.END, task)
            self.todo_list.todo_list.append(task)  # 메모리 목록에 추가

    def delete_selected_todo(self):
        """
        선택한 항목을 삭제하는 함수
        """
        selected_tasks = self.listbox.curselection()
        if not selected_tasks:
            tk.messagebox.showwarning("삭제 오류", "삭제할 항목을 선택하세요.")
            return

        for index in selected_tasks[::-1]:  # 역순으로 삭제
            task = self.listbox.get(index)
            self.listbox.delete(index)
            self.todo_list.todo_list.remove(task)  # 메모리 목록에서도 삭제

        tk.messagebox.showinfo("삭제 완료", "선택한 할 일이 삭제되었습니다.")

    def finish(self):
        """
        현재 할 일 목록을 파일에 저장합니다.
        """
        tasks = self.listbox.get(0, tk.END)
        self.todo_list.add_todo(tasks)
        tk.messagebox.showinfo("저장 완료", "할 일 목록이 파일에 저장되었습니다.")

    def refresh_listbox(self):
        """
        파일에서 할 일 목록을 불러와 Listbox에 표시합니다.
        """
        self.todo_list.import_todo()  # 파일에서 할 일 목록을 불러옴
        self.listbox.delete(0, tk.END)  # 기존 항목 초기화
        for task in self.todo_list.todo_list:
            self.listbox.insert(tk.END, task)
            
    def quit(self):
        self.root.quit()
        
    def retryButton(self):
        reButton = tk.messagebox.askokcancel("종료", "종료하시겠습니까?")
        if reButton == True:
            self.root.quit()
        else:
            tk.messagebox.showinfo("종료 취소", "취소되었습니다.")

# tkinter 윈도우 생성 및 실행
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
