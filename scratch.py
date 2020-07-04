import tkinter as tk
import json

def CreateNew():
    temp = tk.Tk()
    temp.title('Enter New Client')
    New = MakeNew(temp)
    temp.eval('tk::PlaceWindow . center')
    temp.mainloop()

def Workspace():
    root = tk.Tk()
    root.config(bg='grey9')
    root.title("Personal Trainer")
    App = Application(root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

class StartUp():
    def __init__(self, parent):    
        mainframe = tk.Frame(parent, bg='firebrick4')
        mainframe.grid(column=0, row=0, sticky=tk.N)
        # Adding widgets to the frame
        opening = tk.Label(mainframe, text='Welcome, what do you want to do?', font='tahoma', bg='firebrick4', fg='khaki3')
        guide = tk.Label(mainframe, text="Type the Client's name with no gaps", font='tahoma', bg='firebrick4', fg='khaki3')
        guide.grid(columnspan=10, row=1)
        opening.grid(columnspan=10, row=0, pady=5, padx=5)
        open_entry = tk.Entry(mainframe, textvariable=None)
        open_entry.grid(columnspan=7, row=2, sticky=tk.W+tk.E, padx=5)
        old = tk.Button(mainframe, text='Open', command=lambda:[parent.destroy(), Workspace()], bg='sienna3')
        old.grid(column=7, columnspan=4, row=2, sticky=tk.W+tk.E, pady=5, padx=5)
        new = tk.Button(mainframe, text='New Client', command=lambda:[parent.destroy(), CreateNew()], bg='sienna3', font='tahoma')
        new.grid(columnspan=10, row=3, sticky=tk.W+tk.E, pady=5, padx=5)


class MakeNew:
    
    def __init__(self, loader):
        menubutton = tk.Menubutton(loader, text = "File", relief='raised')
        menubutton.grid()
        menubutton.menu = tk.Menu(menubutton)
        menubutton["menu"]=menubutton.menu
        menubutton.menu.add_checkbutton(label = "New file")
        menubutton.menu.add_checkbutton(label = "Save")
        menubutton.menu.add_checkbutton(label = "Save as")
        menubutton.pack()
        
    def method(self):
        pass
    
class Application():
    def __init__(self, master):
        menubutton = tk.Menubutton(master, text = "File",font='gothic', bg='#86C232')
        menubutton.grid(column=0, row=0, sticky=tk.W+tk.E)
        menubutton.menu = tk.Menu(menubutton, bg='#86C232')
        menubutton["menu"]=menubutton.menu
        menubutton.menu.add_checkbutton(label = "New file")
        menubutton.menu.add_checkbutton(label = "Save")
        menubutton.menu.add_checkbutton(label = "Save as")
        # Frame of vital info
        v_frame = tk.Frame(master, bg='gray16')
        v_frame.grid(column=0, row=1, sticky=tk.W+tk.E)
        # Frame of Additional info
        a_frame = tk.Frame(v_frame)
        a_frame.grid(column=5, row=0, sticky=tk.E+tk.W+tk.N)
        # Frame of Exercise routine
        e_frame = tk.Frame(master, bg='grey18')
        e_frame.grid(column=0, row=2, sticky=tk.S)
        # First Row of Vital Info
        cl_name = tk.Label(v_frame, text='Name', bg='gray15', fg='#61892F',font='tahoma').grid(column=0, row=0, sticky=tk.W+tk.E)
        cl_age = tk.Label(v_frame, text='Age', bg='gray15', fg='#61892F',font='tahoma').grid(column=1, row=0, sticky=tk.W+tk.E)
        cl_height = tk.Label(v_frame, text='Height', bg='gray15', fg='#61892F',font='tahoma').grid(column=2, row=0, sticky=tk.W+tk.E)
        cl_weight = tk.Label(v_frame, text='Weight', bg='gray15', fg='#61892F',font='tahoma').grid(column=3, row=0, sticky=tk.W+tk.E)
        cl_sex = tk.Label(v_frame, text='Gender', bg='gray15', fg='#61892F',font='tahoma').grid(column=4, row=0, sticky=tk.W+tk.E)
        # Second Row of Vital Info
        cl_bfp = tk.Label(v_frame, text='Fat %', bg='gray15', fg='#61892F',font='tahoma').grid(column=0, row=1, sticky=tk.W+tk.E)
        cl_lbm = tk.Label(v_frame, text='Lean Mass', bg='gray15', fg='#61892F',font='tahoma').grid(column=1, row=1, sticky=tk.W+tk.E)
        cl_gw = tk.Label(v_frame, text='Goal Weight', bg='gray15', fg='#61892F',font='tahoma').grid(column=2, row=1, sticky=tk.W+tk.E)
        cl_bmi = tk.Label(v_frame, text='BMI', bg='gray15', fg='#61892F',font='tahoma').grid(column=3, row=1, sticky=tk.W+tk.E)
        # Last Row
        cl_goal = tk.Label(v_frame, text='Goals that the client put go here', bg='gray15', fg='#61892F',font='tahoma').grid(columnspan=5, row=2, sticky=tk.W+tk.E)
        # Additional Column
        atest = tk.Label(a_frame, text='Test', bg='gray22').grid(column=0, row=0)
        # Exercise Routine Column
        mday_label = tk.Label(e_frame, text='Monday', bg='gray18', fg='#61892F', font='gothic').grid(column=0, row=0)
        tday_label = tk.Label(e_frame, text='Tuesday', bg='gray18', fg='#61892F', font='gothic').grid(column=1, row=0)
        wday_label = tk.Label(e_frame, text='Wednesday', bg='gray18', fg='#61892F', font='gothic').grid(column=2, row=0)
        thday_label = tk.Label(e_frame, text='Thursday', bg='gray18', fg='#61892F', font='gothic').grid(column=3, row=0)
        fday_label = tk.Label(e_frame, text='Friday', bg='gray18', fg='#61892F', font='gothic').grid(column=4, row=0)
        saday_label = tk.Label(e_frame, text='Saturday', bg='gray18', fg='#61892F', font='gothic').grid(column=5, row=0)
        sday_label = tk.Label(e_frame, text='Sunday', bg='gray18', fg='#61892F', font='gothic').grid(column=6, row=0)
        mday = tk.Listbox(e_frame, bg='gray22').grid(column=0, row=1)
        tday = tk.Listbox(e_frame, bg='gray22').grid(column=1, row=1)
        wday = tk.Listbox(e_frame, bg='gray22').grid(column=2, row=1)
        thday = tk.Listbox(e_frame, bg='gray22').grid(column=3, row=1)
        fday = tk.Listbox(e_frame, bg='gray22').grid(column=4, row=1)
        stday = tk.Listbox(e_frame, bg='gray22').grid(column=5, row=1)
        sday = tk.Listbox(e_frame, bg='gray22').grid(column=6, row=1)
        
    def method(self):
        pass

if __name__ == '__main__':
    sub = tk.Tk()
    sub.config(bg='firebrick4')
    sub.title('PT App Login')
    Window = StartUp(sub)
    sub.eval('tk::PlaceWindow . center')
    sub.mainloop()
    
