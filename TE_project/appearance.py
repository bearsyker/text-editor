import re
from PySide6.QtWidgets import QWidget, QSizePolicy, QApplication, QMenu, QMainWindow, QTextEdit, QFileDialog, QTabWidget, QStyleFactory
from PySide6.QtGui import QSyntaxHighlighter ,QKeySequence, QAction, QColor, QPainter, QPalette
from PySide6.QtCore import Qt

   
class Appearance():
    def update_highlights(self):
        
        pass
        
        
      
    def custom_menu(self):
        menuBar = self.menuBar()
        self.customize_menu = menuBar.addMenu('Customize')
        
        theme_menu = QMenu('Theme', self.customize_menu)
        self.customize_menu.addMenu(theme_menu)
        themes = ['light', 'dark']
        for theme in themes:
            action = QAction(theme, theme_menu, checkable=True)
            action.toggled.connect(self.update_custom)
            theme_menu.addAction(action)
            
            
    def toggle_theme(self):
        current_stylesheet = self.text_edit.styleSheet()
        
        if "dark" in current_stylesheet:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()
            
            
    def apply_dark_theme(self):
        dark_stylesheet = """
            QTextEdit {
                background-color: #2b2b2b;
                color: #ffffff;
                selection-background-color: #555555;
            }
            QPushButton {
                background-color: #2b2b2b;
                color: #ffffff;
            }
        """
        self.text_edit.setStyleSheet(dark_stylesheet)
        self.theme_button.setText('Dark Theme')
        
    def apply_light_theme(self):
        light_stylesheet = """
            QTextEdit {
                background-color: #ffffff;
                color: #2b2b2b;
                selection-background-color: #555555;
            }
            QPushButton {
                background-color: #ffffff;
                color: #2b2b2b;
            }
        """
        
        self.text_edit.setStyleSheet(self.light_stylesheet)
        self.theme_button.setText('light Theme')
        
        
        
    def update_custom(self):
        if self.tabs is None:
            return 
        
        Current_tab = self.tabs.currentIndex()
        tab_widget = self.tabs.widget(Current_tab)
        
        theme = self.theme_var
        font = self.font_var
        
        QApplication.setStyle(QStyleFactory.create(theme))
        
        if tab_widget:
            tab_widget.setStyleSheet(f"background-color: {self.get_background_color(theme)}; color: {self.get_text_color(theme)}")
            tab_widget.setTextColor(Qt.black)
            tab_widget.setTextBackgroundColor(Qt.white) 
            tab_widget.setFontPointSize(self.get_font_size(font)) 

        self.tabs.setStyleSheet(f"background-color: {self.get_background_color(theme)}")
        
        
class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)

        self._mappings = {}

    def add_mapping(self, pattern, format):
        self._mappings[pattern] = format

    def highlightBlock(self, text):
        for pattern, format in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, format)