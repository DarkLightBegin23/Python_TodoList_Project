import tkinter
import tkinter.messagebox

def delete_selected(listbox):
    # 선택된 항목들의 인덱스를 가져와서 거꾸로 삭제
    selected_items = listbox.curselection()
    for index in reversed(selected_items):
        listbox.delete(index)