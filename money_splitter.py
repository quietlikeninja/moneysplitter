import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Model:
    def __init__(self, pay) -> None:
        self.pay = pay

    @property
    def pay(self):
        return self.__pay
    
    @pay.setter
    def pay(self, value):
        try:
            if float(value) <= 0:
                raise ValueError
            else:
                self.__pay = value
        except ValueError:
            raise ValueError(f'{value} is not a valid pay amount.\nEnter a vaild number without currency sign.')
    
    def split(self):
        self.splurge = np.round(float(self.pay) * 0.075, 2)
        self.smile = np.round(float(self.pay) * 0.1, 2)
        self.fire = np.round(float(self.pay) * 0.15, 2)
        return self.splurge, self.smile, self.fire

class View(ttk.Frame): # define a ProgramGUI class
    def __init__(self, parent): 
        super().__init__(parent)
        self.splurge_prefix = 'Splurge: $ '
        self.smile_prefix = 'Smile: $ '
        self.fire_prefix = 'Fire: $ '

        # create widgets
        # label - pay prompt
        self.label = ttk.Label(self, width=25, justify='right', text='How much were you paid? ')
        self.label.grid(row=1, column=0)

        # pay entry
        self.pay_var = tk.StringVar()
        self.pay_entry = ttk.Entry(self, textvariable=self.pay_var, width=7)
        self.pay_entry.grid(row=2, column=0, sticky=tk.NSEW)

        # label - results
        self.splurge_label = ttk.Label(self, text=f'{self.splurge_prefix} 0.00')
        self.splurge_label.grid(row=3, column=0, sticky=tk.W)
        self.smile_label = ttk.Label(self, text=f'{self.smile_prefix} 0.00')
        self.smile_label.grid(row=4, column=0, sticky=tk.W)
        self.fire_label = ttk.Label(self, text=f'{self.fire_prefix} 0.00')
        self.fire_label.grid(row=5, column=0, sticky=tk.W)

        # buttons
        self.split_button = ttk.Button(self, text='Split Pay', command=self.split_button_clicked)
        self.split_button.grid(row=1, column=1, padx=10)
        self.reset_button = ttk.Button(self, text='Reset', command=self.reset_button_clicked)
        self.reset_button.grid(row=2, column=1, padx=10)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def split_button_clicked(self):
        if self.controller:
            self.controller.split(self.pay_var.get())

    def show_error(self, message):
        messagebox.showerror('Invalid Input', message)

    def show_results(self, results):
        self.splurge_label['text'] = self.splurge_prefix + str(results[0])
        self.smile_label['text'] = self.smile_prefix + str(results[1])
        self.fire_label['text'] = self.fire_prefix + str(results[2])

    def reset_button_clicked(self):
        self.splurge_label['text'] = f'{self.splurge_prefix} 0.00'
        self.smile_label['text'] = f'{self.smile_prefix} 0.00'
        self.fire_label['text'] = f'{self.fire_prefix} 0.00'
        self.pay_var.set('')

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def split(self, pay):
        try:
            # save the model
            self.model.pay = pay

            # show results
            self.view.show_results(self.model.split())

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Money Splitter')

        window_width = 260
        window_height = 125

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)

        # create a model
        model = Model(1000)

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop() 