import tkinter as tk
import dbwrapper




class pwdApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.createWidgets()
    
    def createWidgets(self):
        menubar =tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar)
        file_menu.add_command(
                 label='DbSettings',
                 command=self.destroy,
                  )
        menubar.add_cascade(
        label="DbSettings",
         menu=file_menu,
         underline=0
         )
        
        mainframe=tk.Frame(self,width=200,height=200)
        unamef=tk.Entry(mainframe,)
        unamef.pack(side='left')
        pwdent=tk.Entry(mainframe,)
        pwdent.pack(side='left')
        savebutt=tk.Button(mainframe,text="save")
        savebutt.pack()
        self.title("password manager")
        
        mainframe.pack()
        
        searchframe=mainframe=tk.Frame(self,width=200,height=200)
        searchbox=unamef=tk.Entry(searchframe,)
        searchbox.pack(side='left')
        searchbutt=tk.Button(searchframe,text="search")
        searchbutt.pack()
        savebutt.pack()
        searchframe.pack(side="left")


if __name__ == "__main__":
    app = pwdApp()
    app.mainloop()



     
    