def setup_editor(self, text_widget):
        self.line_num_area = LineNumbers(self.tabs)  # Pass reference to tabs
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.line_num_area)
        layout.addWidget(text_widget)
        text_widget.setLayout(layout)
        text_widget.blockCountChanged.connect(self.update_line_area)
        text_widget.verticalScrollBar().valueChanged.connect(self.update_line_area)
        self.update_line_area()
        
    
    def update_line_area_width(self):
        width = self.tabs.currentWidget().lineNumberAreaWidth()
        self.tabs.currentWidget().setViewportMargins(width, 0, 0, 0)    
        
    
    def update_line_area(self):
        self.line_num_area.update(0, 0, self.lineNumberAreaWidth(), self.tabs.currentWidget().viewport().height())        


class LineNumbers(QWidget):
    def __init__(self, tabs):
        super().__init__()
        self.tabs = tabs
    
    def sizeHint(self):
        return QSize(self.tabs.currentWidget.lineNumberAreaWidth(), 0)
        
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(event.rect(), Qt.lightGray)
        
        editor = self.tabs.currentWidget()
        if not editor:
            return
        
        
        
        block = editor.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = editor.blockBoundingGeometry(block).translated(editor.contentOffset()).top()
        height = editor.fontMetrics().height()
        
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and top + height >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.width(), height, Qt.AlignRight, number)


            block = block.next()
            top = top + height
            blockNumber += 1