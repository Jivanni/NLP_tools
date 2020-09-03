# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from tkinter import *
from tkinter import messagebox
import langid, ARI, soundex


# %%
class Error(Exception):
    pass
class No_plugin_selected(Error):
    pass
class No_text_inserted(Error):
    pass


# %%
class Application(Frame):
    def __init__(self, master=None, active_plugin = None, string = None):
        Frame.__init__(self,master)
        self.createWidgets()
        self.pack()
        self.string = string
        self.active_plugin = active_plugin

    def set_current_plugin(self, plugin_name):
        self.active_plugin = plugins_list[plugin_name]
    
    def createWidgets(self):
        self.Input_box1 = Text(self)
        self.Input_box1["height"] = 10
        self.Input_box1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "NW")

        self.Output_box1 = Text(self)
        self.Output_box1["height"] = 10
        self.Output_box1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "NW")
    
        self.Action_button = Button(self, padx = 50, pady = 20, text = "Run", command= self.print_text)
        self.Action_button.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "NW")

        self.Clear_button = Button(self, padx = 50, pady = 20, text = "Clear", command= self.clearall)
        self.Clear_button.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "NW")

        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        
        self.menubar.add_cascade(label="Plugins", menu=self.filemenu)
        self.master.config(menu=self.menubar)
    
    def print_text(self):
        self.string = self.Input_box1.get("1.0","end-1c")
        try:
            if self.active_plugin is None:
                raise No_plugin_selected
            
            elif not self.string:
                raise No_text_inserted
            
            self.Output_box1.delete("1.0",END)
            tx = self.active_plugin(self.string)
            self.Output_box1.insert("1.0", tx)

        except (No_plugin_selected, TypeError):
            messagebox.showerror(title = "No Plugin", message = "Please select a Plugin")
        except No_text_inserted:
            messagebox.showerror(title = "No Text", message = "Please enter text")
        

    def clearall(self):
        self.Input_box1.delete("1.0",END)
        self.Output_box1.delete("1.0",END)

    def add_plugins_from_list(self,array):
        for plugin in plugins_list.keys():
            self.filemenu.add_radiobutton(label=plugin, command= lambda local_plugin = plugin: self.set_current_plugin(local_plugin))


# %%
if __name__ == '__main__':
    
    plugins_list = {
                "Language Detector": langid.lang_id,
                "ARI Calculator": ARI.ARI_rawtext, 
                "Soundex": soundex.Soundex
                }
    
    app = Application(master=Tk())
    app.add_plugins_from_list(plugins_list)
    app.mainloop()


