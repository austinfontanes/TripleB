import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    
import Sledge_support
import os.path

def vp_start_gui():
        '''Starting point when module is the main routine.'''
        global val, w, root
        global prog_location
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        root = tk.Tk()
        top = Toplevel1 (root)
        Sledge_support.init(root, top)
        root.mainloop()
    
w = None
def create_Toplevel1(rt, *args, **kwargs):
        '''Starting point when module is imported by another module.
           Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
        global w, w_win, root
        global prog_location
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        #rt = root
        root = rt
        w = tk.Toplevel (root)
        top = Toplevel1 (w)
        Sledge_support.init(w, top, *args, **kwargs)
        return (w, top)
    
def destroy_Toplevel1():
        global w
        w.destroy()
        w = None
    
class Toplevel1:
        def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9' # X11 color: 'gray85'
            _ana1color = '#d9d9d9' # X11 color: 'gray85'
            _ana2color = '#ececec' # Closest X11 color: 'gray92'
            self.style = ttk.Style()
            if sys.platform == "win32":
                self.style.theme_use('winnative')
            self.style.configure('.',background=_bgcolor)
            self.style.configure('.',foreground=_fgcolor)
            self.style.configure('.',font="TkDefaultFont")
            self.style.map('.',background=
                [('selected', _compcolor), ('active',_ana2color)])
    
            top.geometry("1141x661+48+25")
            top.minsize(72, 15)
            top.maxsize(1440, 787)
            top.resizable(1,  1)
            top.title("New Toplevel")
            top.configure(background="#000000")
    
            self.Entry1 = tk.Entry(top)
            self.Entry1.place(relx=0.771, rely=0.499, height=75, relwidth=0.142)
            self.Entry1.configure(background="white")
            self.Entry1.configure(font="TkFixedFont")
            self.Entry1.configure(foreground="#000000")
            self.Entry1.configure(insertbackground="black")
            self.Entry1.configure(selectforeground="white")
    
            self.ExitButton = tk.Button(top)
            self.ExitButton.place(relx=0.771, rely=0.893, height=22, width=199)
            self.ExitButton.configure(activebackground="#ececec")
            self.ExitButton.configure(activeforeground="#000000")
            self.ExitButton.configure(background="#d9d9d9")
            self.ExitButton.configure(cursor="fleur")
            self.ExitButton.configure(font="-family {Roboto} -size 13")
            self.ExitButton.configure(foreground="#000000")
            self.ExitButton.configure(highlightbackground="#d9d9d9")
            self.ExitButton.configure(highlightcolor="black")
            self.ExitButton.configure(relief="raised")
            self.ExitButton.configure(text='''EXIT TO MAIN MENU''')
   
            self.NextButton = tk.Button(top)
            self.NextButton.place(relx=0.567, rely=0.688, height=22, width=189)
            self.NextButton.configure(activebackground="#ececec")
            self.NextButton.configure(activeforeground="#000000")
            self.NextButton.configure(background="#d9d9d9")
            self.NextButton.configure(font="-family {Roboto} -size 13")
            self.NextButton.configure(foreground="#000000")
            self.NextButton.configure(highlightbackground="#d9d9d9")
            self.NextButton.configure(highlightcolor="black")
            self.NextButton.configure(relief="raised")
            self.NextButton.configure(text='''NEXT ITEM''')
    
            self.Button1 = tk.Button(top)
            self.Button1.place(relx=0.567, rely=0.756, height=22, width=189)
            self.Button1.configure(activebackground="#ececec")
            self.Button1.configure(activeforeground="#000000")
            self.Button1.configure(background="#d9d9d9")
            self.Button1.configure(cursor="fleur")
            self.Button1.configure(font="-family {Roboto} -size 13")
            self.Button1.configure(foreground="#000000")
            self.Button1.configure(highlightbackground="#d9d9d9")
            self.Button1.configure(highlightcolor="black")
            self.Button1.configure(relief="raised")
            self.Button1.configure(text='''PREVIOUS ITEM''')
    
            self.CountLabel = ttk.Label(top)
            self.CountLabel.place(relx=0.561, rely=0.499, height=68, width=207)
            self.CountLabel.configure(background="#000000")
            self.CountLabel.configure(foreground="#000000")
            self.CountLabel.configure(font="-family {Roboto} -size 13")
            self.CountLabel.configure(relief="flat")
            self.CountLabel.configure(anchor='w')
            self.CountLabel.configure(justify='center')
            self.CountLabel.configure(text='''COUNT:''')
    
            self.Frame1 = tk.Frame(top)
            self.Frame1.place(relx=0.0, rely=0.0, relheight=0.056, relwidth=1.008)
            self.Frame1.configure(relief='groove')
            self.Frame1.configure(borderwidth="2")
            self.Frame1.configure(relief="groove")
            self.Frame1.configure(background="#d9d9d9")
    
            self.TLabel1 = ttk.Label(top)
            self.TLabel1.place(relx=0.666, rely=0.076, height=160, width=195)
            self.TLabel1.configure(background="#d9d9d9")
            self.TLabel1.configure(foreground="#000000")
            self.TLabel1.configure(font="TkDefaultFont")
            self.TLabel1.configure(relief="flat")
            self.TLabel1.configure(anchor='w')
            self.TLabel1.configure(justify='center')
            self.TLabel1.configure(text='''Image''')
            global _img0
            _img0 = tk.PhotoImage(file="sledge-distillery-2017-final-logo-12-1-17.png")
            self.TLabel1.configure(image=_img0)
    
            self.TLabel2 = ttk.Label(top)
            self.TLabel2.place(relx=0.044, rely=0.862, height=59, width=704)
            self.TLabel2.configure(background="#d9d9d9")
            self.TLabel2.configure(foreground="#000000")
            self.TLabel2.configure(font="-family {Roboto} -size 13")
            self.TLabel2.configure(relief="flat")
            self.TLabel2.configure(anchor='w')
            self.TLabel2.configure(justify='left')
            self.TLabel2.configure(text='''REPORT INVENTORY''')
    
            self.Label1 = tk.Label(top)
            self.Label1.place(relx=-0.368, rely=-0.696, height=994, width=984)
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(foreground="#000000")
            global _img1
            _img1 = tk.PhotoImage(file="s746342102120056129_p117_i4_w640.png")
            self.Label1.configure(image=_img1)
            self.Label1.configure(text='''Label''')
    
            self.TLabel3 = ttk.Label(top)
            self.TLabel3.place(relx=0.649, rely=0.408, height=20, width=222)
            self.TLabel3.configure(background="#000000")
            self.TLabel3.configure(foreground="#000000")
            self.TLabel3.configure(font="-family {Roboto} -size 13")
            self.TLabel3.configure(relief="flat")
            self.TLabel3.configure(anchor='w')
            self.TLabel3.configure(justify='center')
            self.TLabel3.configure(text='''Dubs Spirit 500 mL''')
   
if __name__ == '__main__':
    vp_start_gui()
