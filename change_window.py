from tkinter import Toplevel, Label, Button
import keyboard
import os

def change_key(button, file_line, main_update_callback):
    key_pressed = keyboard.read_event().name
    button.config(text=key_pressed)

    file_path = "dados.txt"

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(["0\n", "F2\n", "F3\n", "F4\n"])

    with open(file_path, "r", encoding="utf-8") as arquivo:
        lines = arquivo.readlines()

    while len(lines) <= file_line:
        lines.append("\n")

    lines[file_line] = f"{key_pressed}\n"

    with open(file_path, "w", encoding="utf-8") as arquivo:
        arquivo.writelines(lines)

    main_update_callback()

#FUNÇÃO DA JANELA
def open_change_window(actual_key, actual_key2, actual_key3, main_update_callback):
    changekey_window = Toplevel()
    changekey_window.title('Change Bind')

    top_text = Label(changekey_window, text='Binds')
    top_text.grid(column=0, row=0, columnspan=3)

    input1 = Label(changekey_window, text='Add Deaths')
    input1.grid(column=0, row=1)

    button_change = Button(changekey_window, text=f'{actual_key}', command=lambda: change_key(button_change, 1, main_update_callback), width=20)
    button_change.grid(column=1, row=1)

    button1_text = Label(changekey_window, text='Press a bind to CHANGE!')
    button1_text.grid(column=2, row=1)

    input2 = Label(changekey_window, text='Decrease Deaths')
    input2.grid(column=0, row=2)

    button_change2 = Button(changekey_window, text=f'{actual_key2}', command=lambda: change_key(button_change2, 2, main_update_callback), width=20)
    button_change2.grid(column=1, row=2)

    button2_text = Label(changekey_window, text='Press a bind to CHANGE!')
    button2_text.grid(column=2, row=2)

    input3 = Label(changekey_window, text='Remove Deaths')
    input3.grid(column=0, row=3)

    button_change3 = Button(changekey_window, text=f'{actual_key3}', command=lambda: change_key(button_change3, 3, main_update_callback), width=20)
    button_change3.grid(column=1, row=3)

    button3_text = Label(changekey_window, text='Press a bind to CHANGE!')
    button3_text.grid(column=2, row=3)
