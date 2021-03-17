import os
import shutil
import tkinter as tk
from tkinter.filedialog import askopenfile, askdirectory
import json
import time

from tkinter import filedialog



class windowobject(tk.Tk):
    def __init__(self):
        # object constructor
        self.window = tk.Tk()
        self.window.title("First App")
        self.window.geometry("500x300")

        # Instance reference properties
        self.name=""
        self.source_dir = os.getcwd()
        self.destination_dir = ""

        # Load config file
        self.load_config()
    

    def set_name(self, value):
        """Sets the name of the project"""
        self.name = value


    def set_dir_path(self, dir_type, label):
        """Sets the source directory to copy files from"""
        if dir_type=="src":
            self.source_dir = filedialog.askdirectory()
            label.config(text=self.source_dir)
        if dir_type == "dst":
            self.destination_dir = filedialog.askdirectory()
            label.config(text=self.destination_dir)


    def save_config_file(self, name_entry):
        """save configuration file"""
        self.name = name_entry.get()
        fs = open(f'{self.source_dir}/jinter_config.json', mode='w')
        config = {'name': self.name,'source': self.source_dir, 'destination': self.destination_dir}
        fs.write(json.dumps(config, indent=4))


    def load_config(self):
        """Saves the main configgurations files in the c://jinter_config"""
        try:
            config_file = open(f'{self.source_dir}/jinter_config.json', mode='r')
            config = json.loads(config_file.read())
            self.name=config['name']
            self.source_dir = config['source']
            self.destination_dir = config['destination']
            config_file.close()
        except Exception as e:
            print(e)


    def run_process(self):
        """ This is the main process that executes copy files from source to the destination """
        # shutil.copytree(self.source_dir, self.destination_dir, symlinks=False, ignore=None, copy_function=shutil.copy, ignore_dangling_symlinks=False, dirs_exist_ok=True)

        # Files stats
        total_files = 0
        transferable_files = []

        for root, dirs, files in os.walk(self.source_dir):
            # print("root: ", root)
            # print("dirs: ", dirs)
            # print("files: ", files)
            # print('\n')

            # shutil.copy("C:/Users/pjs/Desktop/jinker/jinker/main.py","C:/Users/pjs/Desktop/copytest")
            
            for name in files:
                time.sleep(1)
                print("sss: ", root, name)
                file_from = os.path.join(root, name)
                file_to = root.replace(self.source_dir, self.destination_dir)

                # Load files to be processed
                transferable_files.append({
                    "src": file_from,
                    "dst": file_to,
                })
                
                total_files+=1
                os.system('cls')
                print("Total files: ", total_files)

        # transfer count
        count = 0
        for transfer in transferable_files:
            time.sleep(1)
            try:
                os.mkdir(transfer['dst'])
            except:
                pass
            shutil.copy(transfer['src'], transfer['dst'])
            os.system('cls')
            count+=1
            print("Processed: ", count)
        print('--- Process Completed ----')


# x = windowobject()