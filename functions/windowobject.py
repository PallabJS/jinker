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
        self.window.title(" Jinker")
        self.window.geometry("600x300")

        # Instance reference properties
        self.name = ""
        self.source_dir = os.getcwd()
        self.destination_dir = ""

        # Load config file
        self.load_config()

    def set_name(self, value):
        """Sets the name of the project"""
        self.name = value

    def set_dir_path(self, dir_type, label):
        """Sets the source directory to copy files from"""
        if dir_type == "src":
            url = filedialog.askdirectory()
            if url != "":
                self.source_dir = url
            label.config(text=self.source_dir)

        if dir_type == "dst":
            url = filedialog.askdirectory()
            if url != "":
                self.destination_dir = url
            label.config(text=self.destination_dir)

    def save_config_file(self, name_entry):
        """save configuration file"""
        self.name = name_entry.get()
        fs = open('jinter_config.json', mode='w')
        config = {'name': self.name, 'source': self.source_dir,
                  'destination': self.destination_dir}
        fs.write(json.dumps(config, indent=4))

    def load_config(self):
        """Loads the main configuration from /jinter_config.json"""
        try:
            config_file = open('jinter_config.json', mode='r')
            config = json.loads(config_file.read())
            self.name = config['name']
            self.source_dir = config['source']
            self.destination_dir = config['destination']
            config_file.close()
        except Exception as e:
            print(e)

    def run_process(self, status_label, wo):
        """ This is the main process that executes copy files from source to the destination """
        # shutil.copytree(self.source_dir, self.destination_dir, symlinks=False, ignore=None, copy_function=shutil.copy, ignore_dangling_symlinks=False, dirs_exist_ok=True)

        # Files stats
        total_files = 0
        transferable_files = []

        status_label.config(text="Counting files")
        wo.window.update()

        for root, dirs, files in os.walk(self.source_dir):

            # shutil.copy("C:/Users/pjs/Desktop/jinker/jinker/main.py","C:/Users/pjs/Desktop/copytest")

            for name in files:

                file_from = f'{root}/{name}'
                file_to = root.replace(self.source_dir, self.destination_dir)

                test_pass = True
                ignores = [".git", "__pycache__", ".vscode", "nodemodules"]
                for teststring in ignores:
                    if file_from.find(teststring) != -1:
                        test_pass = False
                        break
                if not test_pass:
                    continue

                # Load files to be processed
                transferable_files.append({
                    "src": file_from,
                    "dst": file_to,
                })
                total_files += 1
                # print("Total files: ", total_files)
                status_label.config(text=f'Files: {total_files}')
                wo.window.update()

        status_label.config(text=f'Total files: {total_files}')
        wo.window.update()
        # transfer count
        count = 0

        # Give a break
        time.sleep(1)
        status_label.config(text="Starting transfer process")
        wo.window.update()
        time.sleep(2)

        for transfer in transferable_files:
            status_label.config(text=f'Copying file: {count} of {total_files}')
            wo.window.update()
            try:
                os.mkdir(transfer['dst'])
            except:
                pass
            shutil.copy(transfer['src'], transfer['dst'])
            count += 1
        status_label.config(text="Process Completed!")
        print("done")
