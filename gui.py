import os
import tkinter as tk
from tkinter import  messagebox
import subprocess
from tkinter import simpledialog
from config import cascade_path, distance_threshold, camera_id
from Face_Checker import FaceChecker
from settings import ManagerApp
photo_file = 'photo_file.txt'

def load_photo_file():
    photo_file_array = []
    try:
        with open(photo_file, 'r', encoding='utf-8') as File:
            for line in File:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split('|')
                if len(parts) == 2:
                    photo = parts[0].strip()
                    file = parts[1].strip()
                    photo_file_array.append((photo, file))
    except FileNotFoundError:
        pass
    return photo_file_array

def choose_file_dialog(photo_file):
    files = []
    for photo_path, protected_file in photo_file:
        files.append(protected_file)
    root = tk.Tk()
    root.withdraw()
    file_number = "Enter file number to open:\n"

    for i, file_path in enumerate(files):
        file_number += f"{i+1}. {os.path.basename(file_path)}\n"

    selected_number = simpledialog.askstring("Select File", file_number)
    root.destroy()

    if selected_number and selected_number.isdigit():
        i = int(selected_number) - 1
        if 0 <= i < len(files):
            return files[i]
    return None

def open_protected_file():
    photo_file = load_photo_file()
    if not photo_file:
        messagebox.showerror("Error", "photo_file.txt is empty.")
        return

    selected_file = choose_file_dialog(photo_file)
    if not selected_file:
        return

    ref_photo = None
    for photo, file in photo_file:
        if file == selected_file:
            ref_photo = photo
            break

    if not ref_photo or not os.path.exists(ref_photo):
        messagebox.showerror("Error", "Reference photo not found.")
        return

    checker = FaceChecker(ref_photo, cascade_path, distance_threshold, camera_id)
    if checker.authentificate():
        subprocess.Popen(['cmd', '/c', 'start', '', selected_file], shell=True)
    else:
        messagebox.showerror("Access Denied", "Face not recognized. Access denied.")

def open_settings():
    manager = ManagerApp()
    manager.mainloop()

def run_gui():
    root = tk.Tk()
    root.title("Protected Folder Access")
    root.geometry("300x150")

    tk.Label(root, text="Choose a protected file to open:").pack(pady=20)
    tk.Button(root, text="Open File", command=open_protected_file).pack(pady=10)
    tk.Button(root, text="Settings", command=open_settings).pack(pady=5)
    tk.Label(root, text="Press 'q' to quit").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()