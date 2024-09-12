import tkinter

window=tkinter.Tk()  # 상위 레벨 윈도우 창 생성

window.title("Todo List")  # 제목
window.geometry("640x480+100+100")  # 창 크기 좌표
window.resizable(True, True)  # 창 크기 조절 여부(상하, 좌우)


count=0

def countUP():
    global count
    count+=1
    button.config(text=str(count))

def countDOWN():
    global count
    count-=1
    button.config(text=str(count))

title=tkinter.Label(window, text="Todo List입니당.", width=15, height=5, fg="black", relief="ridge",bg="green")  # tltie 위젯 설정
title.pack()  # 위젯 배치

button = tkinter.Button(window, overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100, cursor="circle")
button.pack()
button2 = tkinter.Button(window, overrelief="solid", width=15, command=countDOWN, repeatdelay=1000, repeatinterval=100, cursor="circle")
button2.pack()

listbox = tkinter.Listbox(window, selectmode='extended', height=0, highlightcolor="yellow", highlightbackground="white", takefocus="True")
listbox.insert(0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "3번")
listbox.insert(3, "4번")
listbox.place(x=150, y=250)

entry = tkinter.Entry(window)
entry.pack()

def flash():
    checkbutton1.flash()

checkVariety_1=tkinter.IntVar()
checkVariety_2=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="O", variable=checkVariety_1, activebackground="cyan")

checkbutton1.pack()

window.mainloop()  # 윈도우 종료될 때까지 실행