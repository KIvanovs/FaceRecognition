from sre_constants import SUCCESS
import tkinter as tk
from tkinter import Label, messagebox
import subprocess
from config import protected_path, ref_image_path, cascade_path, distance_threshold, camera_id
from Face_Checker import FaceChecker

def open_protected_folder():
    checker = FaceChecker(ref_image_path, cascade_path, distance_threshold, camera_id)
    SUCCESS = checker.authentificate()

    if SUCCESS:
        subprocess.Popen(["explorer", protected_path])
    else:
        messagebox.showerror("Authentication Failed", "You are not authorized to access this folder.")

def run_gui():
    root = tk.Tk()
    root.title("Protected Folder Access")

    tk.Label(root, text="Click the button to access the protected folder.").pack(pady=20)
    tk.Button(root, text="Access Folder", command=open_protected_folder).pack(pady=10)
    tk.Label(root, text="Press 'q' to quit").pack(pady=5)

    root.mainloop()
