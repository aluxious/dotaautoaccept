import tkinter as tk
import pyautogui as pag

win = tk.Tk()
win.geometry('200x50+550+250')
win.title('Mos Loc')
win.config(bg='#323232')
win.attributes('-topmos', 1)

frame = tk.Frame()


lab = tk.Label(text='')
lab.pack()


def update():
    lab.configure(text=pag.position())
    frame.after(20, update)


update()
frame.mainloop()