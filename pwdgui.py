import tkinter as tk
import dbwrapper




class pwdApp(tk.Frame):
    def __init__(self):
        super().__init__()
    
    def createWidgets(self):
        mainframe=tk.Frame(self)
        mainframe.pack()


if __name__ == "__main__":
    app = pwdApp()
    app.mainloop()



     
    