import tkinter as tk
from tkinter import filedialog, messagebox

def read_file():
    try:
        with open("notes.txt", "r") as file:
            file_content = file.read()
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, file_content)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")

def insert_line():
    new_line = entry_insert.get()
    with open("notes.txt", "a") as file:
        file.write("\n" + new_line)
    read_file()

def count_lines():
    try:
        with open("notes.txt", "r") as file:
            line_count = sum(1 for line in file)
            messagebox.showinfo("Line Count", f"Number of lines in the file: {line_count}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")

def find_longest_words():
    try:
        with open("notes.txt", "r") as file:
            words = file.read().split()
            longest_words = [word.strip(".,") for word in words if len(word.strip(".,")) == max(len(w.strip(".,")) for w in words)]
            messagebox.showinfo("Longest Words", f"The longest word(s) in the file: {', '.join(longest_words)}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")

def append_text():
    new_text = entry_append.get()
    with open("notes.txt", "a") as file:
        file.write("\n" + new_text)
    read_file()

# Create the main window
root = tk.Tk()
root.title("File Operations")

# Read file button
button_read = tk.Button(root, text="Read File", command=read_file)
button_read.pack()

# Insert line
entry_insert = tk.Entry(root, width=50)
entry_insert.pack()
button_insert = tk.Button(root, text="Insert Line", command=insert_line)
button_insert.pack()

# Count lines button
button_count = tk.Button(root, text="Count Lines", command=count_lines)
button_count.pack()

# Find longest words button
button_longest_words = tk.Button(root, text="Find Longest Words", command=find_longest_words)
button_longest_words.pack()

# Append text
entry_append = tk.Entry(root, width=50)
entry_append.pack()
button_append = tk.Button(root, text="Append Text", command=append_text)
button_append.pack()

# Text output widget
text_output = tk.Text(root, height=10, width=50)
text_output.pack()

# Run the main loop
root.mainloop()
