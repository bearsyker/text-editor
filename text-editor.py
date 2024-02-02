import tkinter as tk
from tkinter import ttk, filedialog
from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token



class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Customizable Text Editor")

        self.theme_var = tk.StringVar()
        self.font_var = tk.StringVar()

        self.theme_var.set("default")
        self.font_var.set("TkDefaultFont")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand="yes", fill="both")

        self.add_tab()

        self.create_menu()
        self.create_customization_options()

    def add_tab(self):
        frame = ttk.Frame(self.notebook)
        frame.pack(fill="both", expand=True)

        text_widget = tk.Text(frame, wrap="word", undo=True)
        text_widget.pack(expand="yes", fill="both")

        self.notebook.add(frame, text="Untitled")
        self.notebook.select(frame)

        
        self.notebook.bind("<<NotebookTabChanged>>", self.update_customization)

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        file_menu_items = [
            ("New", self.new_file),
            ("Open", self.open_file),
            ("Save", self.save_file),
            ("Exit", self.root.destroy)
        ]

        for label, command in file_menu_items:
            self.file_menu.add_command(label=label, command=command)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        edit_menu_items = [
            ("Undo", self.undo),
            ("Redo", self.redo),
            ("Copy", self.copy),
            ("Cut", self.cut),
            ("Paste", self.paste)
        ]

        for label, command in edit_menu_items:
            self.edit_menu.add_command(label=label, command=command)

        # Create a submenu for customization
        self.customization_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Customize", menu=self.customization_menu)

    def create_customization_options(self):
        theme_menu = tk.Menu(self.customization_menu, tearoff=0)
        self.customization_menu.add_cascade(label="Theme", menu=theme_menu)
        themes = ["default", "clam", "alt", "classic"]
        for theme in themes:
            theme_menu.add_radiobutton(label=theme, variable=self.theme_var, value=theme, command=self.update_customization)

        font_menu = tk.Menu(self.customization_menu, tearoff=0)
        self.customization_menu.add_cascade(label="Font", menu=font_menu)
        fonts = ["TkDefaultFont", "Helvetica", "Courier"]
        for font in fonts:
            font_menu.add_radiobutton(label=font, variable=self.font_var, value=font, command=self.update_customization)
            

    def undo(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]
        text_widget.edit_undo()

    def redo(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]
        text_widget.edit_redo()

    def copy(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]
        text_widget.event_generate("<<Copy>>")

    def cut(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]
        text_widget.event_generate("<<Cut>>")

    def paste(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]
        text_widget.event_generate("<<Paste>>")

    def update_customization(self, event=None):
        
        current_tab = self.notebook.select()
        text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]

        
        theme = self.theme_var.get()
        font = self.font_var.get()

        
        self.root.tk_setPalette(background="SystemButtonFace", foreground="SystemButtonText")
        text_widget.config(bg="SystemButtonFace", fg="SystemButtonText", insertbackground="SystemButtonText")


        text_widget.config(font=font)

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()