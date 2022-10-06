from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sqlite3
import ui

class LoginScreen:
    def __init__(self):
        super().__init__()

        self.state = 'login'

        self.image_frame = customtkinter.CTkFrame(width=643, height=429)
        self.image_frame.pack()

        self.splash = ImageTk.PhotoImage(Image.open("splash_screen_trimmed.jpg"))

        self.image_label = customtkinter.CTkLabel(
            self.image_frame, text_font=ui.Fonts.SMALLER_FONT, image=self.splash)
        self.image_label.pack()

        self.fields_container = customtkinter.CTkFrame()
        self.fields_container.place(anchor="nw", height=214, width=643, x=0, y=429)

        self.login_header = customtkinter.CTkLabel(
            self.fields_container, text="Login", text_font=ui.Fonts.HEADER_FONT, padx=0, pady=0)
        self.login_header.place(anchor="center", x=322, y=29)

        self.login_username = customtkinter.CTkLabel(
            self.fields_container, anchor="w", text="Username: ", text_font=ui.Fonts.SMALLER_FONT)
        self.login_username.place(anchor="center", x=205, y=76)

        self.login_password = customtkinter.CTkLabel(
            self.fields_container, anchor="w", text="Password: ", text_font=ui.Fonts.SMALLER_FONT)
        self.login_password.place(anchor="center", x=204, y=124)

        self.login_entry = customtkinter.CTkEntry(self.fields_container, width=230)
        self.login_entry.place(anchor="center", x=373, y=75)

        self.password_entry = customtkinter.CTkEntry(
            self.fields_container, width=230, show="*")
        self.password_entry.place(anchor="center", x=373, y=125)

        self.login_button = customtkinter.CTkButton(
            self.fields_container,
            text="Login",
            text_font=ui.Fonts.SMALLER_FONT,
            corner_radius=30,
            width=120,
            command=self.validate_database)
        self.login_button.place(anchor="center", x=249, y=175)

        self.register_button = customtkinter.CTkButton(
            self.fields_container,
            text="Register",
            text_font=ui.Fonts.SMALLER_FONT,
            corner_radius=30,
            width=120,
            command=self.register_button)
        self.register_button.place(anchor="center", x=395, y=175)

        # Validation Text
        self.validation_text = customtkinter.CTkLabel(
            self.fields_container, text="", text_font=ui.Fonts.EVEN_SMALLER_FONT)
        self.validation_text.place(anchor="center", x=545, y=175)

    def register_button(self):
        if self.state == 'register':
            conn = sqlite3.connect('customers.db')
            c = conn.cursor()

            new_details = [(str(self.login_entry.get()), str(self.password_entry.get()))]

            c.executemany("INSERT INTO customers VALUES (?, ?)", new_details)
            print(c.fetchall())

            conn.commit()
            conn.close()
            conn.close()

            self.login_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

            self.validation_text.configure(text_color=ui.Colours.SUCCESS, text="Thanks for registering!\nCome on in! :)")
        else:
            self.login_header.configure(text="Register")
            self.state = 'register'

    def validate_database(self):
        conn = sqlite3.connect('customers.db')
        c = conn.cursor()

        c.execute("SELECT * FROM customers")
        for index in c.fetchall():
            if index[0] == self.login_entry.get() and index[1] == self.password_entry.get():
                self.validation_text.configure(text_color=ui.Colours.SUCCESS, text="Correct!\nCome on in! :)")
                break
            else:
                self.validation_text.configure(text_color=ui.Colours.FAILURE, text="Incorrect Username\nand/or Password")

        conn.commit()
        conn.close()
        conn.close()
