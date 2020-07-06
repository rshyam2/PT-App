#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import json
import Calculations as cl
import os
    
class StartUp():
    
    def __init__(self, parent):
        self.parent = parent
        self.weekdays = ['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self._name = tk.StringVar()
        self._age = tk.IntVar()
        self._height = tk.IntVar()
        self._weight = tk.DoubleVar()
        self._gender = tk.StringVar()
        self._gweight = tk.IntVar()
        self.c_goals = tk.StringVar()
        self.skinfold = tk.IntVar()
        
        self.monday = tk.StringVar()
        self.tuesday = tk.StringVar()
        self.wednesday = tk.StringVar()
        self.thursday = tk.StringVar()
        self.friday = tk.StringVar()
        self.saturday = tk.StringVar()
        self.sunday = tk.StringVar()
        self.target = tk.StringVar()
        self.old_client
        self.get_bfp
        mainframe = tk.Frame(self.parent,bg='firebrick4')
        mainframe.grid(column=0, row=0, sticky=tk.N, padx=10, pady=10)
        # Adding widgets to the frame
        title = tk.Label(mainframe, text='Welcome, what do you want to do?', font='tahoma', bg='firebrick4', fg='khaki3')
        guide = tk.Label(mainframe, text="Type the Client's name with no gaps", font='tahoma', bg='firebrick4', fg='khaki3')
        guide.grid(columnspan=10, row=1, pady=5, padx=5)
        title.grid(columnspan=10, row=0, pady=5, padx=5)
        self.open_entry = tk.Entry(mainframe, textvariable=self.target, font='tahoma')
        self.open_entry.grid(columnspan=7, row=2, sticky=tk.W+tk.E, padx=5)
        old = tk.Button(mainframe, text='Open', command=lambda:[self.check_input(), self.open_entry.delete(0, tk.END)], bg='sienna3')
        old.grid(column=7, columnspan=4, row=2, sticky=tk.W+tk.E, pady=5, padx=5)
        new = tk.Button(mainframe, text='New Client/Edit Existing', command=lambda:[self.new_client()], bg='sienna3', font='tahoma')
        new.grid(columnspan=10, row=3, sticky=tk.W+tk.E, pady=5, padx=5)
    # Function Checks validity of file, If it exists it opens it, otherwise an error.
    def check_input(self):
        OpenFile = self.open_entry.get() + '.json'
        directory = './samples/'
        filepath = os.path.join(directory, OpenFile) 
        if os.path.isfile(filepath) == True:
            self.old_client()
        else:
            messagebox.showerror('Error', "There is no Client with that name...")         
    def old_client(self):
        master = tk.Toplevel(bg='grey9')
        master.title('Client View')
        master.grid()
        # Frame of vital info
        v_frame = tk.Frame(master,bg='gray15')
        v_frame.grid(column=0, row=0, sticky=tk.W+tk.E)
        # Frame of Exercise routine
        self.e_frame = tk.Frame(master,bg='grey18')
        self.e_frame.grid(column=0, row=1, sticky=tk.S)
        # First Row of Vital Info
        label1 = ['Name', 'Age', 'Height', 'Weight', 'Gender', 'Fat %', 'Lean Mass', 'Goal Weight', 'BMI']
        for label in label1:
            tk.Label(v_frame, text=label, bg='gray15', fg='SpringGreen4',font='tahoma').grid(column=label1.index(label), row=0, padx=5, sticky=tk.W+tk.E)
        # Reading from the json file   
        directory = './samples/' + self.open_entry.get() + '.json'
        file = open(directory, 'r')
        data = json.load(file)
        file.close()
        #closing the file
        mass = round((int(data['Weight'])*(data['BodyFat']/100)),2)
        lean = int(data['Weight']) - mass
        # Filling the Labels with real value
        ClientName = tk.Label(v_frame, text=data['Name'], bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=0, row=1, padx=5)
        CLientAge = tk.Label(v_frame, text=data['Age'], bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=1, row=1, padx=5)
        ClientH = tk.Label(v_frame, text=data['Height'], bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=2, row=1, padx=5)
        ClientW = tk.Label(v_frame, text=data['Weight'], bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=3, row=1, padx=5)
        ClientS = tk.Label(v_frame, text=data['Gender'], bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=4, row=1, padx=5)
        ClientFat = tk.Label(v_frame, text=data['BodyFat'], bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=5, row=1, padx=5)
        ClientLbm = tk.Label(v_frame, text=lean, bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=6, row=1, padx=5)
        ClientGw = tk.Label(v_frame, text=data['GoalWeight'], bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=7, row=1, padx=5)
        ClientBMI = tk.Label(v_frame, text=data['BMI'], bg='gray15', fg='OliveDrab1', font='tahoma').grid(column=8, row=1, padx=5)
        # Last Row
        block = 'Client Goals ------'
        cl_goal = tk.Label(v_frame, text=block,bg='gray15',fg='SpringGreen4',font='tahoma').grid(columnspan=5,row=2,padx=5,sticky=tk.W)
        ClientGoal = tk.Label(v_frame, text=data['ClientGoal'], bg='gray15', fg='OliveDrab1', font='tahoma')
        ClientGoal.grid(columnspan=5, row=3, padx=5, sticky=tk.W)
        # Exercise Routine Column
        for day in self.weekdays:
            tk.Label(self.e_frame, text=day, bg='gray18', fg='SpringGreen4', font='gothic').grid(column=self.weekdays.index(day), row=0)            
        mday = tk.Listbox(self.e_frame, bg='gray22', fg='OliveDrab1', font='gothic')
        mday.grid(column=0, row=1)
        tday = tk.Listbox(self.e_frame, bg='gray22', fg='OliveDrab1', font='gothic')
        tday.grid(column=1, row=1)
        wday = tk.Listbox(self.e_frame, bg='gray22', fg='OliveDrab1', font='gothic')
        wday.grid(column=2, row=1)
        thday = tk.Listbox(self.e_frame, bg='gray22', fg='OliveDrab1', font='gothic')
        thday.grid(column=3, row=1)
        fday = tk.Listbox(self.e_frame, bg='gray22', fg='OliveDrab1', font='gothic')
        fday.grid(column=4, row=1)
        stday = tk.Listbox(self.e_frame, bg='gray22', fg='OliveDrab1', font='gothic')
        stday.grid(column=5, row=1)
        sday = tk.Listbox(self.e_frame, bg='gray22', fg='OliveDrab1', font='gothic')
        sday.grid(column=6, row=1)
        # Getting the values from each weekday
        MON = data['Monday'].split(", ")
        for ex in MON:
            mday.insert(tk.END, ex)
        TUE = data['Tuesday'].split(", ")
        for ex in TUE:
            tday.insert(tk.END, ex)
        WED = data['Wednesday'].split(", ")
        for ex in WED:
            wday.insert(tk.END, ex)
        THU = data['Thursday'].split(", ")
        for ex in THU:
            thday.insert(tk.END, ex)
        FRI = data['Friday'].split(", ")
        for ex in FRI:
            fday.insert(tk.END, ex)
        SAT = data['Saturday'].split(", ")
        for ex in SAT:
            stday.insert(tk.END, ex)
        SUN = data['Sunday'].split(", ")
        for ex in SUN:
            sday.insert(tk.END, ex)
        
    def new_client(self):
        frame = tk.Toplevel(bg='firebrick4')
        frame.grid()
        frame.title('New Client')
        # make Questionnaire
        c_info = ['Client Name', 'Age', 'Height(inch)', 'Weight', 'Gender']
        for label in c_info:
            tk.Label(frame, text=label, bg='firebrick4', fg='khaki3', font='tahoma').grid(column=c_info.index(label), row=0, padx=5, sticky=tk.W)
        # Making Entry boxes
        n_entry = tk.Entry(frame, textvariable=self._name, width=15, font='tahoma')
        n_entry.grid(column=0, row=1, padx=5)
        age_entry = tk.Entry(frame, textvariable=self._age, width=5, font='tahoma')
        age_entry.grid(column=1, row=1, padx=5, sticky=tk.W)
        h_entry = tk.Entry(frame, textvariable=self._height, width=15, font='tahoma')
        h_entry.grid(column=2, row=1, padx=5, sticky=tk.W)
        w_entry = tk.Entry(frame, textvariable=self._weight, width=8, font='tahoma')
        w_entry.grid(column=3, row=1, padx=5)
        g_entry = tk.Entry(frame, textvariable=self._gender, width=5, font='tahoma')
        g_entry.grid(column=4, row=1, padx=5)
        # Skinfold entry
        skin_label = tk.Label(frame, text="Skinfold(mm)", bg='firebrick4', fg='khaki3', font='tahoma')
        skin_label.grid(column=5, columnspan=2, row=0, padx=5, sticky=tk.W)
        skin_entry = tk.Entry(frame, textvariable=self.skinfold, width=15, font='tahoma')
        skin_entry.grid(column=5, columnspan=2, row=1, padx=5, sticky=tk.W)
        # Client Goal weight
        goalw_label = tk.Label(frame, text="Goal Weight", bg='firebrick4', fg='khaki3', font='tahoma')
        goalw_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=(5, 0))
        goalw_entry = tk.Entry(frame, textvariable=self._gweight, width=10, font='tahoma')
        goalw_entry.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        # Client Goals
        goal_label = tk.Label(frame, text="Client's Goals", bg='firebrick4', fg='khaki3', font='tahoma')
        goal_label.grid(column=1, columnspan=4, row=2, sticky=tk.W, padx=5, pady=(5, 0))
        client_goal = tk.Entry(frame, textvariable=self.c_goals, font='tahoma')
        client_goal.grid(column=1, columnspan=5, row=3, sticky=tk.W+tk.E, padx=5, pady=5)
        # Making weekday entry titles
        for days in self.weekdays:
            tk.Label(frame, text=days, bg='firebrick4', fg='khaki3', font='tahoma').grid(column=0, row=(4+self.weekdays.index(days)))
        # Weekday Entries
        mon_entry = tk.Entry(frame, textvariable=self.monday, font='tahoma')
        mon_entry.grid(column=1, columnspan=5, row=4, sticky=tk.W+tk.E)
        tue_entry = tk.Entry(frame, textvariable=self.tuesday, font='tahoma')
        tue_entry.grid(column=1, columnspan=5, row=5, sticky=tk.W+tk.E)
        wed_entry = tk.Entry(frame, textvariable=self.wednesday, font='tahoma')
        wed_entry.grid(column=1, columnspan=5, row=6, sticky=tk.W+tk.E)
        thu_entry = tk.Entry(frame, textvariable=self.thursday, font='tahoma')
        thu_entry.grid(column=1, columnspan=5, row=7, sticky=tk.W+tk.E)
        fri_entry = tk.Entry(frame, textvariable=self.friday, font='tahoma')
        fri_entry.grid(column=1, columnspan=5, row=8, sticky=tk.W+tk.E)
        sat_entry = tk.Entry(frame, textvariable=self.saturday, font='tahoma')
        sat_entry.grid(column=1, columnspan=5, row=9, sticky=tk.W+tk.E)
        sun_entry = tk.Entry(frame, textvariable=self.sunday, font='tahoma')
        sun_entry.grid(column=1, columnspan=5, row=10, sticky=tk.W+tk.E)
        # making a function to clear entryboxes
        def clear_boxes(boxes):
            for box in boxes:
                box.delete(0, tk.END)
        ToPurge = [n_entry,age_entry,h_entry,w_entry,g_entry,goalw_entry,client_goal,mon_entry,
                            tue_entry,wed_entry,thu_entry,fri_entry,sat_entry,sun_entry,skin_entry]
        # Assigning function before call in submit button
        def submit_client():
            try:
                _bfp = self.get_bfp(int(age_entry.get()), int(skin_entry.get()), g_entry.get())
                Bmi = cl.bmi(int(w_entry.get()), int(h_entry.get()))
            except ValueError:
                messagebox.showerror("Error", "Values may have been NULL")
                Bmi = 0
                _bfp = 0
            # Dumping Data to JSON file
            payload = {'Name':n_entry.get(), 'Age':age_entry.get(), 'Height':h_entry.get(), 'Weight':w_entry.get(),
                       'Gender':g_entry.get(), 'GoalWeight':goalw_entry.get(),'ClientGoal':client_goal.get(), 'BodyFat':round(_bfp, 3),
                       'Monday':mon_entry.get(), 'Tuesday':tue_entry.get(), 'Wednesday':wed_entry.get(), 'Thursday':thu_entry.get(),
                       'Friday':fri_entry.get(), 'Saturday':sat_entry.get(), 'Sunday':sun_entry.get(), 'BMI':Bmi}
            filename = n_entry.get() + '.json'
            directory = './samples/'
            _path = (directory +  filename)
            if not os.path.isdir(directory):
                os.mkdir(directory)
            
            if os.path.isfile(_path) == True:
                with open(_path, 'w+') as writefile:
                    json.dump(payload, writefile, indent=1)
                messagebox.showinfo('Confirmation', "CLient File has been updated!")
            else:
                with open(_path, 'a+') as writefile:
                    json.dump(payload, writefile, indent=1)
                messagebox.showinfo('Confirmation', "Client has been created!")
        # Making the submit button
        sub_button = tk.Button(frame, text='Submit!', bg='sienna3',font='tahoma', command=lambda:[submit_client(),clear_boxes(ToPurge)])
        sub_button.grid(columnspan=8, row=11, pady=(10, 5))
        # Get Body Fat %
    def get_bfp(self, age, skinfold, gender):
        if gender == 'M' or gender == 'Male':
            body_fat = cl.Calc(age, skinfold)
            return body_fat.male_fatp()
        else:
            body_fat = cl.Calc(age, skinfold)
            return body_fat.female_fatp()
            
if __name__ == '__main__':
    sub = tk.Tk()
    sub.config(bg='firebrick4')
    sub.title('PT App Login')
    Window = StartUp(sub)
    sub.eval('tk::PlaceWindow . center')
    sub.mainloop()