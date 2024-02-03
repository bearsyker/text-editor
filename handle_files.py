


def new_file(self):
    self.add_tab()

def open_file(self):
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            self.add_tab()
            current_tab = self.notebook.select()
            text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, content)

def save_file(self):
    current_tab = self.notebook.select()
    text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_widget.get(1.0, tk.END))
