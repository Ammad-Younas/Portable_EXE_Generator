import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
root = Tk()

root.geometry("900x630+220+10")
root.resizable(False, False)
root.title("EXE file Generator by | C-S")
root.iconbitmap("icon/logo.ico")


def generate_exe():
    if app_name_entry.get() == "":
        messagebox.showwarning("Warning!", "Enter App Name...!")
    elif len(folder_path_text.get('1.0', END)) <= 1:
        messagebox.showwarning("Warning!", "Select Folder...!")
    elif len(file_path_text.get('1.0', END)) <= 1:
        messagebox.showwarning("Warning!", "Select Main File...!")
    elif len(icon_path_text.get('1.0', END)) <= 1:
        messagebox.showwarning("Warning!", "Select Icon File...!")
    else:
        config = "Setup="+new_file_path+".vbs\nTempMode\nSilent=1\nOverwrite=1"
        create_config = open("cyber-spider.conf", "w")
        created_config = create_config.write(config)
        create_config.close()

        creating_main_batch_file = new_file_path+".bat"

        if new_file_path.endswith(".py") or new_file_path.endswith(".pyw"):
            bat = "@echo off\ncls\npython "+new_file_path
        elif new_file_path.endswith(".exe"):
            bat = "@echo off\ncls\n"+new_file_path
        else:
            pass

        opening_creating_main_batch_file = open(creating_main_batch_file, "w")
        created = opening_creating_main_batch_file.write(bat)
        opening_creating_main_batch_file.close()
        
        os.system('move "'+creating_main_batch_file+'" "'+folderpath+'\\"')

        vbs = new_file_path+".vbs"
        vbs_script = 'Set shell = CreateObject ("Wscript.Shell")\n'+'shell.Run("'+creating_main_batch_file+'")'+', 0, True'
        open_vbs = open(vbs, "w")
        new_vbs = open_vbs.write(vbs_script)
        open_vbs.close()

        os.system('move "'+vbs+'" "'+folderpath+'\\"')

        app_name = app_name_entry.get()

        os.system('cyber-spider.exe a -x -r -ep1 -inul -ibck -y -sfx -iicon"'+icon_path+'" -z"cyber-spider.conf" '+app_name+' "'+folderpath+'\\"')


        del_bat = "del.bat"
        new_bat = "@echo off\ncls\n"+folderpath[0]+":\ncd "+'"'+folderpath+'"\ndel '+creating_main_batch_file+"\ndel "+vbs+"\nmd EXE\ndel del.bat"
        opening = open(del_bat, "w")
        writing = opening.write(new_bat)
        opening.close()
        os.system('copy "'+del_bat+'" "'+folderpath+'\\"')
        os.system(del_bat)
        os.system('xcopy /c '+'"'+app_name+'.exe" '+'"'+folderpath+'"\\EXE')
        os.remove(app_name+'.exe')
        os.remove(del_bat)


        messagebox.showinfo("Info!", "Sucessfully EXE Created!")
        generate.config(state=DISABLED)
        output_path_text.config(state=NORMAL)
        output_path_text.insert('1.0', folderpath+"/EXE/"+app_name_entry.get()+".exe")
        output_path_text.config(state=DISABLED)



def save_name():
    if app_name_entry.get()  == "":
        messagebox.showwarning("Warning!", "Enter App Name...!")
    else:
        app_name_entry.config(state=DISABLED)
        save.config(state=DISABLED)



def clear_pro():
    app_name_entry.config(state=NORMAL)
    save.config(state=NORMAL)
    app_name_entry.delete(0, END)
    folder_path_text.config(state=NORMAL)
    folder_path_text.delete('1.0', END)
    folder_path_text.config(state=DISABLED)
    browse_button_for_folder.config(state=NORMAL)
    file_path_text.config(state=NORMAL)
    file_path_text.delete('1.0', END)
    file_path_text.config(state=DISABLED)
    browse_button_for_file.config(state=NORMAL)
    icon_path_text.config(state=NORMAL)
    icon_path_text.delete('1.0', END)
    icon_path_text.config(state=DISABLED)
    browse_button_for_icon_file.config(state=NORMAL)
    output_path_text.config(state=NORMAL)
    output_path_text.delete('1.0', END)
    output_path_text.config(state=DISABLED)
    generate.config(state=NORMAL)




def exit_appp():
    root.destroy()



def select_folder():
    global folderpath
    folder = filedialog.askdirectory(title="Select Main Folder")
    if folder:
        folderpath = str(folder)
        folder_path_text.config(state=NORMAL)
        folder_path_text.insert('1.0', folderpath)
        folder_path_text.config(state=DISABLED)
        browse_button_for_folder.config(state=DISABLED)


def select_file():
    global file_path
    global new_file_path
    file = filedialog.askopenfile(mode='r', filetypes=[('All Files', '*.py *.pyw *.exe')])
    if file:
        file_path = os.path.abspath(file.name)
        new_file_path = os.path.split(file_path)[1]
        file_path_text.config(state=NORMAL)
        file_path_text.insert('1.0', file_path)
        file_path_text.config(state=DISABLED)
        browse_button_for_file.config(state=DISABLED)
    else:
        file_path_text.config(state=NORMAL)
        file_path_text.delete('1.0', END)
        file_path_text.config(state=DISABLED)


def icon_file():
    global icon_path
    ico = filedialog.askopenfile(mode='r', filetypes=[('Icon File', '*.ico*')])
    if ico:
        icon_path = os.path.abspath(ico.name)
        icon_path_text.config(state=NORMAL)
        icon_path_text.insert('1.0', icon_path)
        icon_path_text.config(state=DISABLED)
        browse_button_for_icon_file.config(state=DISABLED)
    else:
        icon_path_text.config(state=NORMAL)
        icon_path_text.delete('1.0', END)
        icon_path_text.config(state=DISABLED)
    


title_label  = Label(root, text="EXE Generator App", font=("impact", 30), bg="#023548", fg="white")
title_label.place(x=0, y=0, relwidth=1)


main_frame = Frame(root, bd=2, relief=RIDGE, bg='White')
main_frame.place(x=25, y=70, width=850, height=295)

import_label = Label(main_frame, text="Import Data", font=("impact", 20), bg='#043256', fg='White')
import_label.place(x=0, y=0, relwidth=1)


#  ======================= App Name =============================

app_name_label = Label(main_frame, text="Enter Your App Name: ", font=("Cambria", 15, "bold"), bg="white", fg="black")
app_name_label.place(x=10, y=65)

app_name_entry = Entry(main_frame, bd=2, relief=RIDGE, font=("times new roman", 20), bg="white")
app_name_entry.place(x=300, y=65, width=400, height=40)

save = Button(main_frame, text="Save Name", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=save_name)
save.place(x=720, y=65, width=105)

# ===============================================================


# ======================= Selection of Main/Working Folder =====================

select_folder_label = Label(main_frame, text="Select Main/Working Folder: ", font=("Cambria", 15, "bold"), bg="white", fg="black")
select_folder_label.place(x=10, y=125)


folder_path_text = Text(main_frame, font=("times new roman", 10), wrap=NONE, bd=2, relief=RIDGE, state=DISABLED)
folder_path_text.place(x=300, y=120, width=400, height=40)

scroolbar_for_select_folder = Scrollbar(folder_path_text, orient=HORIZONTAL, cursor="hand2")
scroolbar_for_select_folder.pack(side=BOTTOM, fill=X)

folder_path_text.config(xscrollcommand=scroolbar_for_select_folder.set)

scroolbar_for_select_folder.config(command=folder_path_text.xview)


browse_button_for_folder = Button(main_frame, text="BROWSE", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=select_folder)
browse_button_for_folder.place(x=720, y=120)


#  ==============================================================================

# ======================= Selection of Main File =====================

select_file_label = Label(main_frame, text="Select Main File: ", font=("Cambria", 15, "bold"), bg="white", fg="black")
select_file_label.place(x=10, y=185)

file_path_text = Text(main_frame, font=("times new roman", 10), wrap=NONE, bd=2, relief=RIDGE, state=DISABLED)
file_path_text.place(x=300, y=180, width=400, height=40)

scroolbar_for_select_file = Scrollbar(file_path_text, orient=HORIZONTAL, cursor="hand2")
scroolbar_for_select_file.pack(side=BOTTOM, fill=X)

file_path_text.config(xscrollcommand=scroolbar_for_select_file.set)

scroolbar_for_select_file.config(command=file_path_text.xview)

browse_button_for_file = Button(main_frame, text="BROWSE", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=select_file)
browse_button_for_file.place(x=720, y=180)

#  ==============================================================================

# ======================= Selection of icon file for exe =====================


select_icon_label = Label(main_frame, text="Select Icon for EXE: ", font=("Cambria", 15, "bold"), bg="white", fg="black")
select_icon_label.place(x=10, y=250)

icon_path_text = Text(main_frame, font=("times new roman", 10), wrap=NONE, bd=2, relief=RIDGE, state=DISABLED)
icon_path_text.place(x=300, y=240, width=400, height=40)

scroolbar_for_icon_file = Scrollbar(icon_path_text, orient=HORIZONTAL, cursor="hand2")
scroolbar_for_icon_file.pack(side=BOTTOM, fill=X)

icon_path_text.config(xscrollcommand=scroolbar_for_icon_file.set)

scroolbar_for_icon_file.config(command=icon_path_text.xview)

browse_button_for_icon_file = Button(main_frame, text="BROWSE", font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=icon_file)
browse_button_for_icon_file.place(x=720, y=240)

#  ==============================================================================


# ======================= Buttons =====================

buttons_frame = Frame(root, bg='White', bd=2, relief=RIDGE)
buttons_frame.place(x=25, y=510, width=850, height=110)

action_label = Label(buttons_frame, text="Action Area", font=("impact", 20), bg='#043256', fg='White')
action_label.place(x=0, y=0, relwidth=1)

generate = Button(buttons_frame, text="Generate EXE", font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2", command=generate_exe)
generate.place(x=20, y=55)

clear_btn = Button(buttons_frame, text="Clear Fields", font=("times new roman", 15, "bold"), bg="#262626", fg="white", cursor="hand2", command=clear_pro)
clear_btn.place(x=362, y=55)

exit_app = Button(buttons_frame, text="Exit App", font=("times new roman", 15, "bold"), bg="#134899", fg="white", cursor="hand2", command=exit_appp)
exit_app.place(x=730, y=55)


# ======================= Output File Location =====================

output_frame = Frame(root, bg='White', bd=2, relief=RIDGE)
output_frame.place(x=25, y=380, width=850, height=110)

output_label = Label(output_frame, text="Generated EXE Location", font=("impact", 20), bg='#043256', fg='White')
output_label.place(x=0, y=0, relwidth=1)


output_path_text = Text(output_frame, font=("times new roman", 15), wrap=NONE, bd=2, relief=RIDGE, state=DISABLED)
output_path_text.place(x=25, y=50, width=800, height=45)

scroolbar_for_output = Scrollbar(output_path_text, orient=HORIZONTAL, cursor="hand2")
scroolbar_for_output.pack(side=BOTTOM, fill=X)

output_path_text.config(xscrollcommand=scroolbar_for_output.set)

scroolbar_for_output.config(command=output_path_text.xview)

root.mainloop()
