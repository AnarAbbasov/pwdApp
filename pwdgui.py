import tkinter as tk
import dbwrapper




class pwdApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.createWidgets()
    
    def createWidgets(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        file_menu = Menu(menubar)
        file_menu.add_command(
        label='Exit',
        command=self.destroy,
        )
        
        
                                                                                                                                                                        
if __name__ == "__main__":
    app = pwdApp()
    app.mainloop()



     
    