# from TE_project import appearance, Appearance
from TE_project import __init__, Initialize
import sys
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QApplication, QMainWindow, QTextEdit, QFileDialog, QStyleFactory
from PySide6.QtGui import QKeySequence, QPainter, QPaintEvent, QTextCharFormat, QSyntaxHighlighter
from PySide6.QtCore import QSize, Qt, QRegularExpression
import re


class TextEditor(Initialize, QMainWindow):
        
    def add_tab(self):
        text_widget = QTextEdit(self)
        self.tabs.addTab(text_widget, "Untitled")
        self.highlighter = SyntaxHighlighter(text_widget.document())
        self.setup_editor(text_widget)
        
    
    def setup_editor(self, text_widget):
        layout = QHBoxLayout()
        self.line_numbers = LineNumbers(text_widget)
        layout.addWidget(self.line_numbers)
        layout.addWidget(text_widget)
        widget = QWidget()
        widget.setLayout(layout)
        if self.tabs.currentWidget():
            self.tabs.currentWidget().layout().addWidget(widget)
        else:
            self.tabs.addTab(widget, "untitled")

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
        
class LineNumbers(QTextEdit):
    def __init__(self, text_widget):
        super().__init__(text_widget)
        self.text_widget = text_widget
        self.setStyleSheet("background-color: black;")
        self.update_line_numbers()
        
    def update_line_numbers(self):
        block = self.text_widget.document().begin()
        content = []
        while block.isValid():
            block_number = block.blockNumber() + 1
            content.append(str(block_number))
            block = block.next()
        self.setPlainText('/n'.join(content))
        
    def sizeHint(self):
        return QSize(self.width(), 0)
        
        
        
class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighter_rules = []
        
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.darkBlue)
        keywords = ["def", "class", "if", "else", "elif", "for", "while", "return"]
        self.add_mapping("\\b(" + "|".join(keywords) + ")\\b", keyword_format)
        
        
    def add_mapping(self, pattern, format):
        self.highlighter_rules.append((re.compile(pattern), format))
        

    def highlightBlock(self, text):
        for pattern, format in self.highlighter_rules:
            for match in pattern.finditer(text):
                start, end = match.span()
                self.setFormat(start, end - start, format)
                
                
                
                
    # Add line numbers and gutter area
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec())
    
    