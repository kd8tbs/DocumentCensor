import tkinter as tk

class TextBoxInput:
    def __init__(self, master):
        self.master = master
        self.master.title("TextBox Input")
        self.master.geometry('400x200')

        # TextBox Creation
        self.inputtxt = tk.Text(self.master, height=5, width=20)
        self.inputtxt.pack()

        # Button Creation
        tk.Button(self.master, text="Print", command=self.printInput).pack()

        # Label Creation
        self.lbl = tk.Label(self.master, text="")
        self.lbl.pack()

     # Function for getting Input from textbox and printing it
    def printInput(self):
        inp = self.inputtxt.get(1.0, "end-1c")
        self.shieldUp(inp)

    # Function for processing input and updating label text
    def shieldUp(self, inp):
        # Add your processing logic here
        self.lbl.config(text="Provided Input: " + inp)

    
def start():
    root = tk.Tk()
    TextBoxInput(root)
    root.mainloop()
