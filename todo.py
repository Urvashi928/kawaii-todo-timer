import tkinter as tk
from tkinter import messagebox
import time
import threading

# 🍓 Main app window
root = tk.Tk()
root.title("Kawaii To-Do & Timer 🌸")
root.geometry("400x500")
root.config(bg="#ffe6f0")  # pastel pink background

# 🎀 Fonts & Colors
font_main = ("Comic Sans MS", 12)
button_color = "#ffd6e7"
text_color = "#663366"

# 📋 Task list
tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, "🧸 " + task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Please enter a task first!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
        tasks.pop(selected[0])
    else:
        messagebox.showwarning("Oops!", "No task selected!")

# 📌 Timer
def start_timer():
    def run_timer():
        for i in range(25, 0, -1):
            timer_label.config(text=f"🍓 Study Time: {i} min")
            time.sleep(60)
        messagebox.showinfo("Break Time!", "🎉 Yay! Time for a 5 min break, senpai!")
        timer_label.config(text="⏰ Ready for next session!")

    threading.Thread(target=run_timer).start()

# 📝 Widgets
task_entry = tk.Entry(root, font=font_main, bg="#fff0f5")
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task 🍡", command=add_task, font=font_main, bg=button_color)
add_btn.pack()

delete_btn = tk.Button(root, text="Delete Task 🗑️", command=delete_task, font=font_main, bg=button_color)
delete_btn.pack(pady=5)

task_listbox = tk.Listbox(root, font=font_main, bg="#fff8fb", fg=text_color, width=35)
task_listbox.pack(pady=10)

timer_label = tk.Label(root, text="⏰ No Timer Running", font=("Comic Sans MS", 14), bg="#ffe6f0")
timer_label.pack(pady=10)

start_btn = tk.Button(root, text="Start Pomodoro 🍓", command=start_timer, font=font_main, bg="#ffd6e7")
start_btn.pack(pady=10)

# 🌸 Run app
root.mainloop()
