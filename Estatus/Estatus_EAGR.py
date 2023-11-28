import psutil
import time
import tkinter as tk
from tkinter import messagebox

def word():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == 'WINWORD.EXE':
            return True
    return False

def show_message():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    messagebox.showinfo("Word Cerrado", "Microsoft Word se ha cerrado...")
    root.destroy()

while True:
    if not word():
        show_message()
        break
    time.sleep(1)  # Espera 1 segundo antes de volver a verificar
