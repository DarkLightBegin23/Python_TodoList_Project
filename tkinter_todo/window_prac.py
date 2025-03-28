import tkinter
import tkinter.filedialog
import tkinter.messagebox
from PIL import ImageTk 

window=tkinter.Tk()  # 상위 레벨 윈도우 창 생성

window.title("Todo List")  # 제목
window.geometry("640x480+100+100")  # 창 크기 좌표
window.resizable(True, True)  # 창 크기 조절 여부(상하, 좌우)

def input_Todo():
    tkinter.messagebox.showinfo("메시지를 입력하세요")
def get_entry_value():
    user_input = ent.get()
    print(f'입력된 값: {user_input}')

def flash():
    checkbutton1.flash()
ent = tkinter.Entry(window, width=30)
ent.pack()

button = tkinter.Button(window, text="입력값 확인", width=15, command=get_entry_value)
button.pack(pady=10)  # 위아래로 패딩 10을 추가하여 배치

checkVariety_1 = tkinter.IntVar()

checkbutton1 = tkinter.Checkbutton(window, text="Temp", variable=checkVariety_1)

checkbutton1.pack()

count=0

def countUP():
    global count
    count+=1
    Upbutton.config(text=str(count))

def countDOWN():
    global count
    count-=1
    Downbutton.config(text=str(count))

title=tkinter.Label(window, text="Todo List입니당.", width=15, height=5, fg="black", relief="ridge",bg="green")  # tltie 위젯 설정
title.pack()  # 위젯 배치

Upbutton = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100, cursor="circle")
Upbutton.pack()
Downbutton = tkinter.Button(window, overrelief="solid", width=15, command=countDOWN, repeatdelay=1000, repeatinterval=100, cursor="circle")
Downbutton.pack()

listbox = tkinter.Listbox(window, selectmode='extended', height=0, highlightcolor="yellow", highlightbackground="white", takefocus="True")

for i in ["1번", "2번", "3번", "4번"]:
    listbox.insert(tkinter.END, i)  # (위치, 항목) - END 마지막 위치

listbox.place(x=150, y=250)

def flash():
    checkbutton1.flash()

checkVariety_1=tkinter.IntVar()
checkVariety_2=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="O", variable=checkVariety_1, activebackground="cyan", command=flash)
checkbutton2=tkinter.Checkbutton(window, text="△", variable=checkVariety_2, width=10, height=20)

checkbutton1.pack()
checkbutton2.pack()

window.mainloop()  # 윈도우 종료될 때까지 실행