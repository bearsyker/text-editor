import sys
from PySide6.QtWidgets import QWidget, QSizePolicy, QApplication, QMenu, QMainWindow, QTextEdit, QFileDialog, QTabWidget, QStyleFactory, QVBoxLayout, QPushButton
from PySide6.QtGui import QKeySequence, QAction, QColor, QPainter, QPalette
from PySide6.QtCore import Qt
from pygments import lex
from pygments.lexers import get_lexer_by_name
#from customization import Customization



class TextEditor(QMainWindow):
    def __init__(self ):
        super().__init__()

        self.setWindowTitle("My Text Editor")
        
        self.tabs = QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.add_tab()
        self.create_menu()
        self.setCentralWidget(self.tabs)
        
        # theme and customization
        
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)
        

    def add_tab(self):
        
        text_widget = QTextEdit(self)
        self.tabs.addTab(text_widget, "Untitled")
        

    def create_menu(self):
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu('File')
        file_menu.addAction('New', self.new_file, QKeySequence.New)
        file_menu.addAction('Open', self.open_file, QKeySequence.Open)
        file_menu.addAction('Save', self.save_file, QKeySequence.Save)
        file_menu.addSeparator()
        file_menu.addAction('Exit', self.close, QKeySequence.Quit)
        
        edit_menu = menubar.addMenu('Edit')
        edit_menu.addAction('Undo', self.undo, QKeySequence.Undo)
        edit_menu.addAction('Redo', self.redo, QKeySequence.Redo)
        edit_menu.addAction('Copy', self.copy, QKeySequence.Copy)
        edit_menu.addAction('Cut', self.cut, QKeySequence.Cut)
        edit_menu.addAction('Paste', self.paste, QKeySequence.Paste)
    
    def new_file(self):
        self.add_tab()
        
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)')
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.add_tab()
                current_tab = self.tabs.currentIndex()
                text_widget = self.tabs.widget(current_tab)
                text_widget.setPlainText(content)
                self.update_highlights(text_widget)
        
    def save_file(self):
        current_tab = self.tabs.currentIndex()
        text_widget = self.tabs.widget(current_tab)
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)')
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text_widget.toPlainText())
        
    def close_tab(self, index):
        self.tabs.removeTab(index)
    
    
    def undo(self):
        current_tab = self.tabs.currentIndex()
        text_widget = self.tabs.widget(current_tab)
        text_widget.undo()

    def redo(self):
        current_tab = self.tabs.currentIndex()
        text_widget = self.tabs.widget(current_tab)
        text_widget.redo()

    def copy(self):
        current_tab = self.tabs.currentIndex()
        text_widget = self.tabs.widget(current_tab)
        text_widget.copy()
        
    def cut(self):
        current_tab = self.tabs.currentIndex()
        text_widget = self.tabs.widget(current_tab)
        text_widget.cut()

    def paste(self):
        current_tab = self.tabs.currentIndex()
        text_widget = self.tabs.widget(current_tab)
        text_widget.paste()
        
        # Add syntax highlighting
        
        
        
        
    def update_highlights(self, text_widget):
        content = text_widget.toPlainText()
        lexer = get_lexer_by_name("python")
        tokens = lex(content, lexer)
        self.apply_highlights(text_widget, tokens)
        
        
    
class Customizing:
    def __init__(self, parent):
        self.parent = parent
        self.theme_var = "default"
        self.font_var = "DefaultFont"
        self.custom_menu
    
        
    def custom_menu(self):
        pass


    # Add line numbers and gutter area
    
    # changing initial display size
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    
    editor = TextEditor()
    editor.show()
    
    sys.exit(app.exec())