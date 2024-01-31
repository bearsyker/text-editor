import tkinter as tk
from tkinter import ttk, filedialog
from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Text Editor")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand="yes", fill="both")
        
        self.add_tab()
        self.create_menu()
        
    
    def add_tab(self):
        frame = ttk.Frame(self.notebook)
        frame.pack(fill="both", expand=True)
        
        text_widget = tk.Text(frame, wrap="word", undo=True)
        text_widget.pack(expand="yes", fill="both")
        
        self.notebook.add(frame,text="Untitled")
        self.notebook.select(frame)
        self.notebook.bind("<<NotebookTabChanged>>", self.update_highlights)
        
        

    def create_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        menu_items = [
            ("New", self.new_file),
            ("Open", self.open_file),
            ("Save", self.save_file),
            ("Exit", self.root.destroy)
        ]
        
        for label, command in menu_items:
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
                self.update_highlights()

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
                
    
    def undo(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook. nametowidget(current_tab).winfo_children()[0]
        text_widget.edit_undo()
        
    def redo(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook. nametowidget(current_tab).winfo_children()[0]
        text_widget.edit_redo()
    
    def copy(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook. nametowidget(current_tab).winfo_children()[0]
        text_widget.event_generate("<<Copy>>")
        
    def cut(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook. nametowidget(current_tab).winfo_children()[0]
        text_widget.event_generate("<<Cut>>")
        
    def paste(self):
        current_tab = self.notebook.select()
        text_widget = self.notebook. nametowidget(current_tab).winfo_children()[0]
        text_widget.event_generate("<<Paste>>")
        
    
    # start highlights
    
    def update_highlights(self, event=None):
        current_tab = self.notebook.select()
        text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]
        content = self.text_widget.get("1.0, tk.END")
        lexer = self.get_lexer_for_lang("python")
        tokens = lex(content, lexer)
        self.apply_syntax_highlights(text_widget, tokens)
        
    def get_lexer_for_lang(self, lang):
        return get_lexer_by_name(lang, stripall=True)
    
    def apply_highlights(self, text_widget, tokens):
        self.text_widget.tag_configure("Token.Keyword", foreground="cyan")
        self.text_widget.tag_configure("Token.Comment", foreground="green")
        self.text_widget.tag_configure("Token.String", foreground="purple")
        self.text_widget.tag_configure("Token.Number", foreground="orange")
        
        text_widget.tag_remove("Token.Keyword", "1.0", tk.END)
        text_widget.tag_remove("Token.Comment", "1.0", tk.END)
        text_widget.tag_remove("Token.String", "1.0", tk.END)
        text_widget.tag_remove("Token.Number", "1.0", tk.END)
        
        for token, content in tokens:
            tag_name = str(token)
            start_index = "1.0"
            while True:
                start_index = self.text_widget.search(content, start_index, tk.END)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(content)}c"
                self.text_widget.tag_add(tag_name, start_index, end_index)
                start_index = end_index

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()              