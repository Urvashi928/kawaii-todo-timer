import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import time

# 🌸 Theme settings
themes = {
    "Sakura Pink": {"bg": "#f8abca", "btn": "#ffd6e7", "text": "#663366"},
    "Sky Blue": {"bg": "#e0f7ff", "btn": "#cceeff", "text": "#003366"},
    "Mint Green": {"bg": "#e6fff5", "btn": "#ccffe6", "text": "#336655"}
}
current_theme = themes["Sakura Pink"]

root = tk.Tk()
root.title("Kawaii To-Do & Timer 🌸")
root.geometry("420x540")
root.config(bg=current_theme["bg"])

font_main = ("Comic Sans MS", 12)
font_title = ("Comic Sans MS", 16, "bold")
tasks = []

# 🌈 Theme switcher
def switch_theme(theme_name):
    global current_theme
    current_theme = themes[theme_name]
    root.config(bg=current_theme["bg"])
    task_entry.config(bg="#ffffff")
    add_btn.config(bg=current_theme["btn"])
    delete_btn.config(bg=current_theme["btn"])
    start_btn.config(bg=current_theme["btn"])
    theme_menu.config(bg=current_theme["btn"])
    task_listbox.config(bg="#fff8fb", fg=current_theme["text"])
    timer_label.config(bg=current_theme["bg"], fg=current_theme["text"])
    title_label.config(bg=current_theme["bg"], fg=current_theme["text"])

# ✅ Task handling
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, "🍓 " + task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Write a task first!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
        tasks.pop(selected[0])
    else:
        messagebox.showwarning("Oops!", "Select a task to delete!")

# 🐰 Show cheering GIF
def show_cheering_gif():
    gif_window = tk.Toplevel(root)
    gif_window.title("Yay Senpai! 🌸")
    gif_window.geometry("300x300")
    gif_window.config(bg=current_theme["bg"])

    frames = []
    try:
        img = Image.open("yay.gif")  # Make sure 'yay.gif' is in the same folder
        for frame in range(0, img.n_frames):
            img.seek(frame)
            frame_image = ImageTk.PhotoImage(img.copy())
            frames.append(frame_image)
    except Exception as e:
        print("GIF Error:", e)
        return

    label = tk.Label(gif_window, bg=current_theme["bg"])
    label.pack()

    def update(index):
        frame = frames[index]
        label.configure(image=frame)
        gif_window.after(100, update, (index + 1) % len(frames))

    update(0)
    gif_window.after(5000, gif_window.destroy)  # Close after 5 sec

# ⏰ Countdown Timer
def start_timer():
    def run_timer():
        total_secs = 1* 60  # 25 minutes
        while total_secs > 0:
            mins, secs = divmod(total_secs, 60)
            timer_label.config(text=f"⏳ {mins:02d}:{secs:02d}")
            time.sleep(1)
            total_secs -= 1
        timer_label.config(text="🍵 Break Time!")
        show_cheering_gif()
        messagebox.showinfo("Break Time!", "Take 5 min, you earned it 🧋")

    threading.Thread(target=run_timer).start()

# 🖼️ GUI Widgets
title_label = tk.Label(root, text="🌸 Kawaii To-Do & Timer 🌸", font=font_title, bg=current_theme["bg"], fg=current_theme["text"])
title_label.pack(pady=10)

task_entry = tk.Entry(root, font=font_main, bg="#ffffff")
task_entry.pack(pady=8)

add_btn = tk.Button(root, text="Add Task 🧁", command=add_task, font=font_main, bg=current_theme["btn"])
add_btn.pack()

delete_btn = tk.Button(root, text="Delete Task 🗑️", command=delete_task, font=font_main, bg=current_theme["btn"])
delete_btn.pack(pady=5)

task_listbox = tk.Listbox(root, font=font_main, width=35, bg="#fff8fb", fg=current_theme["text"])
task_listbox.pack(pady=10)

timer_label = tk.Label(root, text="⏰ No Timer Running", font=("Comic Sans MS", 14), bg=current_theme["bg"], fg=current_theme["text"])
timer_label.pack(pady=10)

start_btn = tk.Button(root, text="Start Pomodoro 🍓", command=start_timer, font=font_main, bg=current_theme["btn"])
start_btn.pack(pady=10)

theme_var = tk.StringVar(root)
theme_var.set("Sakura Pink")
theme_menu = tk.OptionMenu(root, theme_var, *themes.keys(), command=switch_theme)
theme_menu.config(font=font_main, bg=current_theme["btn"])
theme_menu.pack(pady=15)

root.mainloop()
import random

affirmations = [
    "You’re doing amazing, senpai! 🌸",
    "Small steps still move mountains 🧁",
    "You're soft and strong like mochi 💖",
    "Productivity can be cute too! 🍓"
]

# Call this once on app start:
messagebox.showinfo("Daily Affirmation 🐰", random.choice(affirmations))
try:
    pet_image = ImageTk.PhotoImage(Image.open("kawaii_pet.gif"))
    pet_label = tk.Label(root, image=pet_image, bg=current_theme["bg"])
    pet_label.place(x=10, y=410)
except Exception as e:
    print("Pet image error:", e)

