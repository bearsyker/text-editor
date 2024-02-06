from PySide6.QtWidgets import QMenu, QAction, QRadioButton, QStyleFactory
from PySide6.QtCore import Qt

class Customization:
    def __init__(self, parent):
        self.parent = parent
        self.theme_var = "default"
        self.font_var = "TkDefaultFont"
        self.custom_menu()
        
    def custom_menu(self):
        menubar = self.parent.menuBar()
        
        self.customize_menu = menubar.addMenu('Customize')
        
        theme_menu = QMenu('Theme', self.customize_menu)
        self.customize_menu.addMenu(theme_menu)
        themes = ['default', 'clam', 'alt', 'classic']
        for theme in themes:
            action = QAction(theme, theme_menu, checkable=True)  #Also add option to uncheck others when checked 1
            action.toggled.connect(self.update_custom)
            theme_menu.addAction(action)
            
        font_menu = QMenu('Font', self.customize_menu)
        self.customize_menu.addMenu(font_menu)
        fonts = ["default", "Helvetica", "Courier"]
        for font in fonts:
            action = QAction(font, font_menu, checkable=True)
            action.toggled.connect(self.update_custom)
            font_menu.addAction(action)
            
    
    def update_custom(self):
        current_tab = self.parent.tabs.currentIndex()
        txt_widget = self.parent.tabs.widget(current_tab)
        
        theme = self.theme_var
        font = self.font_var
        
        self.parent.setStyle(QStyleFactory.create(theme))
        
        txt_widget.setStyleSheet(f"background-color: {self.get_background_color(theme)}; color: {self.get_text_color(theme)}")
        txt_widget.setTextColor(Qt.black)
        txt_widget.setTextBackgroundColor(Qt.white) 
        txt_widget.setFontPointSize(self.get_font_size(font))  

    
    # background color
    
    # text color
    
    # font size