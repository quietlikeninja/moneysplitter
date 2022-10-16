import numpy as np
import tkinter
import tkinter.messagebox

def calculateSplit(pay):
    splurge = np.round(float(pay) * 0.075, 2)
    smile = np.round(float(pay) * 0.1, 2)
    fire = np.round(float(pay) * 0.15, 2)
    return splurge, smile, fire

class MoneySplitterGUI: # define a ProgramGUI class
    def __init__(self): 
        self.splurge = 0
        self.smile = 0
        self.fire = 0
        self.main = tkinter.Tk()
        self.main.title('Money Splitter')

        # create Frame widgets
        self.input = tkinter.Frame(self.main, padx=8, pady=4)
        self.resultsSplurge = tkinter.Frame(self.main, padx=8, pady=4)
        self.resultsSmile = tkinter.Frame(self.main, padx=8, pady=4)
        self.resultsFire = tkinter.Frame(self.main, padx=8, pady=4)
        self.buttons = tkinter.Frame(self.main, padx=8, pady=4)

        # create and pack the pay entry widget
        self.payPrompt = tkinter.Label(self.input, width=25, justify='right', text='How much were you paid? ')
        self.pay = tkinter.Entry(self.input, width=7)
        self.payPrompt.pack(side='left')
        self.pay.pack(side='right')

        # create and pack the results widget
        self.splurgeResult = tkinter.Label(self.resultsSplurge, text=f'Splurge: ${self.splurge}')
        self.splurgeResult.pack(side='left')
        self.smileResult = tkinter.Label(self.resultsSmile, text=f'Smile: ${self.smile}')
        self.smileResult.pack(side='left')
        self.fireResult = tkinter.Label(self.resultsFire, text=f'Fire: ${self.fire}')
        self.fireResult.pack(side='left')

        # create and pack the button widgets
        self.splitButton = tkinter.Button(self.buttons, text='Split Pay', command=self.showResult)
        self.resetButton = tkinter.Button(self.buttons, text='Reset', command=self.resetForm)

        self.splitButton.pack(side='left')
        self.resetButton.pack(side='left')

        # pack Frame widgets
        self.input.pack(anchor='w')
        self.resultsSplurge.pack(anchor='w')
        self.resultsSmile.pack(anchor='w')
        self.resultsFire.pack(anchor='w')
        self.buttons.pack()

        self.pay.focus_set()

        tkinter.mainloop()

    def showResult(self):
        try:
            if float(self.pay.get()) <= 0:
                raise ValueError
            else:
                self.splurge, self.smile, self.fire = calculateSplit(self.pay.get())
                self.changeText()
                #tkinter.messagebox.showinfo('Results', f"""Splurge: ${self.splurge}\n Smile: ${self.smile}\nFire: ${self.fire}""")
        except ValueError:
            tkinter.messagebox.showerror('Invalid Input', f'Enter positive numbers only')     

    def resetForm(self):
        self.splurge = 0
        self.smile = 0
        self.fire = 0
        self.changeText()
        self.pay.delete(0, tkinter.END)
        self.pay.focus_set()

    def changeText(self):
        self.splurgeResult['text'] = f'Splurge: ${self.splurge}'
        self.smileResult['text'] = f'Smile: ${self.smile}'
        self.fireResult['text'] = f'Fire: ${self.fire}'

gui = MoneySplitterGUI() # create a ProgramGUI object