


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
            



def update_customization(self, event=None):
        
    current_tab = self.notebook.select()
    text_widget = self.notebook.nametowidget(current_tab).winfo_children()[0]

        
    theme = self.theme_var.get()
    font = self.font_var.get()

        
    self.root.tk_setPalette(background="SystemButtonFace", foreground="SystemButtonText")
    text_widget.config(bg="SystemButtonFace", fg="SystemButtonText", insertbackground="SystemButtonText")


    text_widget.config(font=font)