import sys
from PySide6.QtWidgets import QWidget, QSizePolicy, QApplication, QMenu, QMainWindow, QTextEdit, QFileDialog, QTabWidget, QStyleFactory, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt
from pygments import lex
from pygments.lexers import get_lexer_by_name
#from customization import Customization



class   Initialize():
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

        #self.central_widget = QWidget()
        #self.setCentralWidget(self.central_widget)

        #layout = QVBoxLayout(self.central_widget)

        #self.text_edit = QTextEdit()
        #layout.addWidget(self.text_edit)
        #self.theme_button = QPushButton("Apply Dark Theme")
        #self.theme_button.clicked.connect(self.toggle_theme)
        #layout.addWidget(self.theme_button)

        #self.default_stylesheet = QApplication.instance().styleSheet()
        
        #self.custom_menu()