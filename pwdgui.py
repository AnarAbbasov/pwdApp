import tkinter as tk
import dbwrapper




class pwdApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.createWidgets()
    
    def createWidgets(self):
        
        
        
        
        mainframe=tk.Frame(self,width=200,height=200)
        unamef=tk.Entry(mainframe,)
        unamef.pack(side='left')
        pwdent=tk.Entry(mainframe,)
        pwdent.pack(side='left')
        savebutt=tk.Button(mainframe,text="save")
        savebutt.pack()
        self.title("password manager")
        menubar = tk.Menu(mainframe)
        mainmenu=tk.Menu(menubar,tearoff=0)
        mainmenu.add_command(label="New",)
        self.config(menu=menubar)
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



     
    