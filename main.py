import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("ShutdownPC")
root.geometry('300x200')
root.configure(bg='RoyalBlue4')
root.resizable(width=False,height=False)
root.iconbitmap('icon.ico')


# Функция для выключения компьютера
def shutdown_computer():
    hours = int(entry_hours.get())
    minutes = int(entry_minutes.get())
    seconds = int(entry_seconds.get())

    total_seconds = hours * 3600 + minutes * 60 + seconds

    os.system(f'shutdown -s -t {total_seconds}')

    messagebox.showinfo("Shutdown", f"Computer will turn off in {total_seconds} seconds.")

# Создание полей для ввода и меток
label_hours = tk.Label(root, text="Hours:")
label_hours.pack()
entry_hours = tk.Entry(root)
entry_hours.insert(0, "0")  # Вставка "0" в поле ввода
entry_hours.pack()

label_minutes = tk.Label(root, text="Minutes:")
label_minutes.pack()
entry_minutes = tk.Entry(root)
entry_minutes.insert(0, "0")  # Вставка "0" в поле ввода
entry_minutes.pack()

label_seconds = tk.Label(root, text="Seconds:")
label_seconds.pack()
entry_seconds = tk.Entry(root)
entry_seconds.insert(0, "0")  # Вставка "0" в поле ввода
entry_seconds.pack()

# Создание кнопки для выключения компьютера
button_shutdown = tk.Button(root, text="Shutdown", font= 'Italic 20', command=shutdown_computer)
button_shutdown.pack()
button_shutdown.place(x = 80, y = 125)

root.mainloop()