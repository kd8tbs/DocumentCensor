import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
from Main import shield
import os

class docxRedactor:
    def __init__(self, master):
        self.master = master
        self.master.title("DocuShield")
        self.master.geometry('400x250')

        # Instructions Label
        tk.Label(self.master, text="Enter the file path of the docx to redact:").pack()

        # TextBox Creation
        self.inputtxt = tk.Text(self.master, height=1, width=50)
        self.inputtxt.pack()

        # Button Creation
        tk.Button(self.master, text="Select docx", command=self.select_file).pack()

        # Label Creation
        self.lbl = tk.Label(self.master, text="")
        self.lbl.pack()

        # Progress Bar
        self.progress = tk.DoubleVar()
        self.progressbar = tk.ttk.Progressbar(self.master, orient="horizontal", length=200, mode="determinate", variable=self.progress)
        self.progressbar.pack()
        
        # Shield Button
        tk.Button(self.master, text="Shield", command=self.process_docx).pack()

    def select_file(self):
        filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select docx file", filetypes=(("docx files", "*.docx"), ("All files", "*.*")))
        self.inputtxt.delete('1.0', tk.END)
        self.inputtxt.insert(tk.END, filepath)

    def process_docx(self):
        filepath = self.inputtxt.get('1.0', tk.END).strip()

        if not os.path.exists(filepath):
            self.lbl.config(text="Error: File does not exist.")
            return

        if not filepath.endswith('.docx'):
            self.lbl.config(text="Error: File is not a docx.")
            return
	    
        output_path = filepath.replace(".docx", "-Shielded.docx")
        print(output_path)

        shield(filepath, output_path)
        # Add your docx redaction processing logic here
        # You can use self.progress.set() to update the progress bar

        self.lbl.config(text="docx successfully redacted.")

def start():
    root = tk.Tk()
    docxRedactor(root)
    root.mainloop()
    
if __name__ == '__main__':
   start()