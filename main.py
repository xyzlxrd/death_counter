from tkinter import *
import keyboard
from change_window import open_change_window

#VARIÁVEIS
total_dead = 0
actual_key = "F2"
actual_key2 = 'F3'
actual_key3 = 'F4'
key_pressed = { 'key1': False, 'key2': False, 'key3': False }

#FUNÇÃO PRA LER O ARQUIVO
def read_archive():
    global total_dead, actual_key, actual_key2, actual_key3
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            lines = arquivo.readlines()
            total_dead = int(lines[0].strip()) if lines else 0
            actual_key = lines[1].strip() if len(lines) > 1 else "F2"
            actual_key2 = lines[2].strip() if len(lines) > 2 else "F3"
            actual_key3 = lines[3].strip() if len(lines) > 3 else "F4"
    except FileNotFoundError:
        total_dead = 0
        actual_key = 'F2'
        actual_key2 = 'F3'
        actual_key3 = 'F4'


#FUNÇÃO PARA ATUALIZAR AS TECLAS
def update_keys():
    global actual_key, actual_key2, actual_key3
    try:
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            lines = arquivo.readlines()
            actual_key = lines[1].strip() if len(lines) > 1 else "F2"
            actual_key2 = lines[2].strip() if len(lines) > 2 else "F3"
            actual_key3 = lines[3].strip() if len(lines) > 3 else "F4"
    except FileNotFoundError:
        actual_key = 'F2'
        actual_key2 = 'F3'
        actual_key3 = 'F4'

#FUNÇÃO PARA ATUALIZAR O DISPLAY
def update_display():
    display.config(text=f'TIMES DIED: {total_dead}')

#FUNÇÃO PRA FECHAR
def close():
    main_window.quit()

#PROPRIEDADES DA JANELA PRINCIPAL
main_window = Tk()
main_window.title('TDC - Times Died Counter')

#BARRA DE MENU
menu_bar = Menu(main_window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Change Binds", command=lambda: open_change_window(actual_key, actual_key2, actual_key3, update_keys))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close)

menu_bar.add_cascade(label="Options  |", menu=file_menu)
main_window.config(menu=menu_bar)

#DISPLAY
display = Label(main_window, text=f'TIMES DIED: {total_dead}', background='black', foreground='white', width=20, height=2, font=('Cascadia Code', 25))
display.grid(column=0, row=2)

def modify_deaths():
    global total_dead, key_pressed

    if total_dead < 0:
        total_dead = 0

    if keyboard.is_pressed(actual_key) and not key_pressed['key1']:
        total_dead += 1
        key_pressed['key1'] = True
        update_display()

    elif keyboard.is_pressed(actual_key2) and not key_pressed['key2']:
        if total_dead > 0:
            total_dead -= 1
        key_pressed['key2'] = True
        update_display()

    elif keyboard.is_pressed(actual_key3) and not key_pressed['key3']:
        total_dead = 0
        key_pressed['key3'] = True
        update_display()

    if not keyboard.is_pressed(actual_key):
        key_pressed['key1'] = False

    if not keyboard.is_pressed(actual_key2):
        key_pressed['key2'] = False

    if not keyboard.is_pressed(actual_key3):
        key_pressed['key3'] = False

    main_window.after(100, modify_deaths)

modify_deaths()

read_archive()

main_window.mainloop()
