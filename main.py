import tkinter as tk

from functions.windowobject import windowobject



""" Create a new window object """
wo = windowobject()



""" Maximize window """
# window.state('zoomed')

""" widgets for project name """
# Label
label = tk.Label(wo.window, text="Enter config name: ", relief='flat')
label.grid(row='0', column='0', sticky='W', padx=20, pady=20, ipadx=10, ipady=5)

# Entry
project_name_entry = tk.Entry(wo.window)
project_name_entry.grid(row='0', column='1', ipadx=10, ipady=5)
try:
    project_name_entry.insert(0, f' {wo.name}')
except:
    pass


"""widgets for setting the source directory"""
# Label
label1 = tk.Label(wo.window, text="Choose source directory", relief='flat', bg='blue', fg='white')
# Button
choose_src_dir_button = tk.Button(wo.window, text='source', command=lambda:wo.set_dir_path('src', label1))

# Packs
choose_src_dir_button.grid(row='1', column='0',  sticky='W', padx='20', pady=5, ipadx=10, ipady=0)
label1.grid(row='1', column='1', sticky='W', padx='20', pady=5, ipadx=10, ipady=5)
try:
    label1.config(text=wo.source_dir)
except:
    pass


"""widgets for setting the destination directory"""
# Label
label2 = tk.Label(wo.window, text="Choose destination directory", relief='flat', bg='blue', fg='white')
# Button
choose_dst_dir_button = tk.Button(wo.window, text='destination', command=lambda:wo.set_dir_path('dst', label2))

# Packs
choose_dst_dir_button.grid(row='2', column='0',  sticky='W', padx='20', pady=5, ipadx=10, ipady=0)
label2.grid(row='2', column='1', sticky='W', padx='20', pady=5, ipadx=10, ipady=5)

try:
    if wo.destination_dir != "":
        label2.config(text=wo.destination_dir)
except:
    pass




""" This button is used to save the config file """
# Button
save_button = tk.Button(wo.window, text='save config', width=15, command=lambda: wo.save_config_file(project_name_entry))
save_button.grid(row='3', column='1', sticky='E', padx='20', pady=5, ipadx=10, ipady=0)


""" This button is used to run the export process """
# Button
run_button = tk.Button(wo.window, text='Export', width=15, command=lambda: wo.run_process())
run_button.grid(row='4', column='1', sticky='E', padx='20', pady=5, ipadx=10, ipady=0)



# Run window instance
wo.window.mainloop()