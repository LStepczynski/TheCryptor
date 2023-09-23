import tkinter as tk
from theCryptor import TheCryptor
from threading import Thread
import keyboard as kb
import pyperclip
from time import sleep

class ControlPanel():
    def __init__(self) -> None:
        self.bind1 = TheCryptor.text_to_binary
        self.bind2 = TheCryptor.binary_to_text
        self.t1 = Thread(target=self.key_strokes)
        self.t2 = Thread(target=self.control_panel)
        self.t1.start()
        self.t2.start()

    def set_value(self, variable, value):
        setattr(self, variable, value)


    def key_strokes(self):
        while True:
            if kb.is_pressed('ctrl') and kb.is_pressed(';'):
                print(self.bind1)
                clipboard = pyperclip.paste()
                clipboard = self.bind1(clipboard)
                pyperclip.copy(clipboard)
                sleep(1)
            if kb.is_pressed('ctrl') and kb.is_pressed("'"):
                clipboard = pyperclip.paste()
                clipboard = self.bind2(clipboard)
                pyperclip.copy(clipboard)
                sleep(1)


    def control_panel(self):
        self.root = tk.Tk()
        self.root.geometry('600x400')

        self.main_label = tk.Label(self.root, text='TheCryptor', font=('', 35))
        self.main_label.pack(pady=15)

        self.title_separator = tk.Canvas(self.root, width=600, height=30)
        self.title_separator.pack()
        self.title_separator.create_line(0, 5, 600, 5, fill="#000000", width=5)
        self.title_separator.create_line(0, 25, 600, 25, fill="#000000", width=5)

        self.settings1_label = tk.Label(self.root, text='Keybind 1 settings', font=('', 25))
        self.settings1_label.pack()

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
        self.encoding_menu.add_command(label='Text to Binary', command=lambda: self.set_value("bind1", TheCryptor.text_to_binary))
        self.encoding_menu.add_command(label='Text to Hex', command=lambda: self.set_value("bind1", TheCryptor.text_to_hex))
        self.encoding_menu.add_command(label='Binary to Text', command=lambda: self.set_value("bind1", TheCryptor.binary_to_text))
        self.encoding_menu.add_command(label='Binary to Hex', command=lambda: self.set_value("bind1", TheCryptor.binary_to_hex))
        self.encoding_menu.add_command(label='Hex to Text', command=lambda: self.set_value("bind1", TheCryptor.hex_to_text))
        self.encoding_menu.add_command(label='Hex to Binary', command=lambda: self.set_value("bind1", TheCryptor.hex_to_binary))

        self.encoding.config(menu=self.encoding_menu)

        self.setting_separator = tk.Canvas(self.root, width=600, height=5)
        self.setting_separator.pack(pady=10)
        self.setting_separator.create_line(0, 5, 600, 5, fill="#000000", width=5)

        self.settings2_label = tk.Label(self.root, text='Keybind 1 settings', font=('', 25))
        self.settings2_label.pack()

        self.settings2 = tk.Frame(width=600)
        self.settings2.pack()

        self.decoding_label = tk.Label(self.settings2, text="Mode:", font=('', 15))
        self.decoding_label.grid(row=0, column=0)

        self.decoding = tk.Menubutton(self.settings2, 
                                              text="Set Mode", 
                                              relief="raised",
                                              font=('', 15))
        self.decoding.grid(row=0, column=1)

        self.decoding_menu = tk.Menu(self.decoding, tearoff=0)
        self.decoding_menu.add_command(label='Text to Binary', command=lambda: self.set_value("bind2", TheCryptor.text_to_binary))
        self.decoding_menu.add_command(label='Text to Hex', command=lambda: self.set_value("bind2", TheCryptor.text_to_hex))
        self.decoding_menu.add_command(label='Binary to Text', command=lambda: self.set_value("bind2", TheCryptor.binary_to_text))
        self.decoding_menu.add_command(label='Binary to Hex', command=lambda: self.set_value("bind2", TheCryptor.binary_to_hex))
        self.decoding_menu.add_command(label='Hex to Text', command=lambda: self.set_value("bind2", TheCryptor.hex_to_text))
        self.decoding_menu.add_command(label='Hex to Binary', command=lambda: self.set_value("bind2", TheCryptor.hex_to_binary))

        self.decoding.config(menu=self.decoding_menu)

        self.root.mainloop()
        