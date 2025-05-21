import tkinter as tk
from tkinter import filedialog, messagebox

photo_file = 'photo_file.txt'

def load_photo_file():
    photos_files = []
    try:
        with open(photo_file, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split('|')
                if len(parts) == 2:
                    photos_files.append((parts[0].strip(), parts[1].strip()))
    except FileNotFoundError:
        pass
    return photos_files

def save(photos_files):
    with open(photo_file, 'w', encoding='utf-8') as File:
        for photo, file in photos_files:
            File.write(f"{photo} | {file}\n")

class ManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Face Check")
        self.geometry("700x400")

        self.photos_files = load_photo_file()

        # list with files 
        self.listbox = tk.Listbox(self, font=("Arial", 10))
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10) # pack() is a layout manager that places the widget in a window.

        tk.Button(btn_frame, text="Add", command=self.add).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete).pack(side=tk.LEFT, padx=5)

        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for photo, file in self.photos_files:
            display = f"Photo: {photo}  ->  Protects: {file}"
            self.listbox.insert(tk.END, display)

    def add(self):
        photo_path = filedialog.askopenfilename(title="Select your face photo", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if not photo_path:
            return
        file_path = filedialog.askopenfilename(title="Select file/folder for protection")
        if not file_path:
            return

        # validation
        for p, f in self.photos_files:
            if p == photo_path and f == file_path:
                messagebox.showinfo("Info", "This file and path combination already exists.")
                return

        self.photos_files.append((photo_path, file_path))
        save(self.photos_files)
        self.refresh_list()

    def delete(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Info", "Select a file and path to delete.")
            return
        i = selection[0]
        del self.photos_files[i]
        save(self.photos_files)
        self.refresh_list()

if __name__ == "__main__":
    app = ManagerApp()
    app.mainloop()
