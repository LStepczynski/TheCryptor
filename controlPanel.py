import tkinter as tk
from theCryptor import TheCryptor
from threading import Thread
import keyboard as kb
import pyperclip
from time import sleep

class ControlPanel():
    def __init__(self) -> None:
        self.bind = TheCryptor.text_to_binary
        self.args = None
        self.t1 = Thread(target=self.key_strokes)
        self.t2 = Thread(target=self.control_panel)
        self.t1.start()
        self.t2.start()

    def set_value(self, variable, value, name, entry_state=tk.DISABLED, args=None):
        """Variable = variable name, value = function assigned to the variable, name = text of the menu button, cipher arguments"""
        setattr(self, variable, value)
        self.args = args
        self.encoding.config(text=name)
        self.key_input.config(state=entry_state)


    def key_strokes(self):
        while True:
            if kb.is_pressed('ctrl') and kb.is_pressed('['):
                self.args[1] = self.key_var.get()
                if self.args[1] == '':
                    self.args[1] = 'default'
                clipboard = pyperclip.paste()
                clipboard = self.bind(clipboard, self.args)
                pyperclip.copy(clipboard)
                sleep(0.2)


    def control_panel(self):
        self.root = tk.Tk()
        self.root.geometry('600x280')

        self.key_var = tk.StringVar()

        self.main_label = tk.Label(self.root, text='TheCryptor', font=('', 35))
        self.main_label.pack(pady=15)

        self.title_separator = tk.Canvas(self.root, width=600, height=30)
        self.title_separator.pack()
        self.title_separator.create_line(0, 5, 600, 5, fill="#000000", width=5)
        self.title_separator.create_line(0, 25, 600, 25, fill="#000000", width=5)

        self.settings_label = tk.Label(self.root, text='Keybind settings', font=('', 25))
        self.settings_label.pack()

        self.settings1 = tk.Frame(width=600)
        self.settings1.pack()

        self.encoding_label = tk.Label(self.settings1, text="Mode:", font=('', 15))
        self.encoding_label.grid(row=0, column=0)

        self.encoding = tk.Menubutton(self.settings1, 
                                              text="Set Mode", 
                                              relief="raised",
                                              font=('', 15))
        self.encoding.grid(row=0, column=1)

        self.encoding_menu = tk.Menu(self.encoding, tearoff=0)
        self.encoding_menu.add_command(label='Text to Binary', command=lambda: self.set_value("bind", TheCryptor.text_to_binary, 'Text to Binary'))
        self.encoding_menu.add_command(label='Binary to Text', command=lambda: self.set_value("bind", TheCryptor.binary_to_text, 'Binary to Text'))
        self.encoding_menu.add_command(label='XOr', command=lambda: self.set_value("bind", TheCryptor.cipher, 'XOr', tk.NORMAL, [TheCryptor.xor, self.key_var.get()]))
        self.encoding_menu.add_command(label='XAnd', command=lambda: self.set_value("bind", TheCryptor.cipher, 'XAnd', tk.NORMAL, [TheCryptor.xand, self.key_var.get()]))

        self.encoding.config(menu=self.encoding_menu)

        self.setting_separator = tk.Canvas(self.root, width=600, height=5)
        self.setting_separator.pack(pady=10)
        self.setting_separator.create_line(0, 5, 600, 5, fill="#000000", width=5)

        self.key_settings = tk.Frame(width=600)
        self.key_settings.pack()

        self.key_label = tk.Label(self.key_settings, text='Cipher Key: ', font=('',20))
        self.key_label.grid(row=0, column=0)

        self.key_input = tk.Entry(self.key_settings, textvariable=self.key_var, font=('',20), width=15)
        self.key_input.grid(row=0, column=1)

        self.root.mainloop()
    