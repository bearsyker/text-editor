import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMenu, QMenuBar, QAction, QTabWidget, QDockWidget, QVBoxLayout, QWidget, QStyleFactory
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from pygments import lex
from pygments.lexers import get_lexer_by_name
import customization
import handle_files



class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Text Editor")
        
        self.tabs = QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.theme_var = "default"
        self.font_var = "TkDefaultFont"

        self.add_tab()
        self.create_menu()
        self.create_custom_options()
        self.setCentralWidget(self.tabs)
        
        
        

    def add_tab(self):
        
        text_widget = QTextEdit(self)
        self.tabs.addTab(text_widget, "Untitled")
        

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


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()