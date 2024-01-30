import tkinter as tk
from tkinter import filedialog
from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Text Editor")
        self.text_widget = tk.Text(self.root, wrap="word", undo=True)
        self.text_widget.pack(expand="yes", fill="both")

        self.create_menu()
        
        self.lexer = None

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
        
        self.create_edit_menu()
        
        
    def create_edit_menu(self):
            
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
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            with open(file_path, "r") as file:
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))
                
    
    def undo(self):
        self.text_widget.edit_undo()
        
    def redo(self):
        self.text_widget.edit_redo()
    
    def copy(self):
        self.text_widget.event_generate("<<Copy>>")
        
    def cut(self):
        self.text_widget.event_generate("<<Cut>>")
        
    def paste(self):
        self.text_widget.event_generate("<<Paste>>")
    
    
    def update_highlights(self):
        content = self.text_widget.get("1.0, tk.END")
        lexer = self.get_lexer_for_lang("python")
        tokens = lex(content, lexer)
        self.apply_syntax_highlights(tokens)
        
    def get_lexer_for_lang(self, lang):
        return get_lexer_by_name(lang, stripall=True)
    
    def apply_highlights(self, tokens):
        self.text_widget.tag_configure("Token.Keyword", foreground="cyan")
        self.text_widget.tag_configure("Token.Comment", foreground="green")
        self.text_widget.tag_configure("Token.String", foreground="purple")
        self.text_widget.tag_configure("Token.Number", foreground="orange")
        
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