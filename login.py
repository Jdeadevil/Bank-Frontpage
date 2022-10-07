from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
import sqlite3
import ui

class LoginScreen:
    def __init__(self):
        super().__init__()

        self.state = 'login'

        # Image Frame 
        self.image_frame = customtkinter.CTkFrame(width=643, height=429)
        self.image_frame.grid(row=0, column=0, sticky="EW")

        # Image Frame > Image
        self.splash = ImageTk.PhotoImage(Image.open("splash_screen_trimmed.jpg"))
        self.image_label = customtkinter.CTkLabel(
            self.image_frame, text_font=ui.Fonts.SMALLER_FONT, image=self.splash)
        self.image_label.grid(row=0, column=0)

        # Fields Container 
        self.fields_container = customtkinter.CTkFrame(
            height=214, width=643)
        self.fields_container.grid(row=1, column=0)

        # Fields Container > Space 
        self.space = customtkinter.CTkFrame(
            self.fields_container, height=10, width=643, fg_color=ui.Colours.STANDARD_BG)
        self.space.grid(row=0, column=0)

        # Fields Container > Login Header 
        self.login_header = customtkinter.CTkLabel(
            self.fields_container, text="Login", text_font=ui.Fonts.HEADER_FONT, padx=0, pady=0)
        self.login_header.grid(row=1, column=0)

        # Fields Container > Space 
        self.space = customtkinter.CTkFrame(
            self.fields_container, height=12, width=643, fg_color=ui.Colours.STANDARD_BG)
        self.space.grid(row=2, column=0)

        # Fields Container > Fields 
        self.fields = customtkinter.CTkFrame(
            self.fields_container, height=78, width=354, fg_color=ui.Colours.STANDARD_BG)
        self.fields.grid(row=3, column=0)

        # Fields Container > Fields > Login Username 
        self.login_username = customtkinter.CTkLabel(
            self.fields, text="Username: ", text_font=ui.Fonts.SMALLER_FONT)
        self.login_username.grid(row=0, column=0, padx="10 0")

        # Fields Container > Fields > Space
        self.space = customtkinter.CTkFrame(
            self.fields, height=22, width=50, fg_color=ui.Colours.STANDARD_BG)
        self.space.grid(row=1, column=0)

        # Fields Container > Fields > Login Password 
        self.login_password = customtkinter.CTkLabel(
            self.fields, text="Password: ", text_font=ui.Fonts.SMALLER_FONT)
        self.login_password.grid(row=2, column=0, padx="10 0")

        # Fields Container > Fields > Username Entry 
        self.login_entry = customtkinter.CTkEntry(self.fields, width=230)
        self.login_entry.grid(row=0, column=1, padx="0 50")

        # Fields Container > Fields > Password Entry 
        self.password_entry = customtkinter.CTkEntry(
            self.fields, width=230, show="*")
        self.password_entry.grid(row=2, column=1, padx="0 50")

        # Fields Container > Space 
        self.space = customtkinter.CTkFrame(
            self.fields_container, height=22, width=643, fg_color=ui.Colours.STANDARD_BG)
        self.space.grid(row=4, column=0)

        # Fields Container > Buttons Frame 
        self.buttons_frame = customtkinter.CTkFrame(
            self.fields_container, height=28, width=226, fg_color=ui.Colours.STANDARD_BG)
        self.buttons_frame.grid(row=5, column=0)

        # Fields Container > Buttons Frame > Login 
        self.login_button = customtkinter.CTkButton(
            self.buttons_frame,
            text="Login",
            text_font=ui.Fonts.SMALLER_FONT,
            corner_radius=30,
            width=120,
            command=self.validate_database)
        self.login_button.grid(row=0, column=0, padx="0 28")

        # Fields Container > Buttons Frame > Register 
        self.register_button = customtkinter.CTkButton(
            self.buttons_frame,
            text="Register",
            text_font=ui.Fonts.SMALLER_FONT,
            corner_radius=30,
            width=120,
            command=self.register_button)
        self.register_button.grid(row=0, column=1)

        # Fields Container > Space
        self.space = customtkinter.CTkFrame(
            self.fields_container, height=32, width=643, fg_color=ui.Colours.STANDARD_BG)
        self.space.grid(row=6, column=0)

    def register_button(self):
        if self.state == 'register':
            conn = sqlite3.connect('customers.db')
            c = conn.cursor()

            new_details = [(str(self.login_entry.get()), str(self.password_entry.get()))]

            c.executemany("INSERT INTO customers VALUES (?, ?)", new_details)
            print(c.fetchall())

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Congratulations!",
                "Thanks for registering, you may now login with your provided details.")
            self.login_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
        else:
            self.login_header.configure(text="Register")
            self.state = 'register'

    def validate_database(self):
        conn = sqlite3.connect('customers.db')
        c = conn.cursor()

        c.execute("SELECT * FROM customers")
        for index in c.fetchall():
            if index[0] == self.login_entry.get() and index[1] == self.password_entry.get():
                messagebox.showinfo(
                    "Congratulations!",
                    f"You have now successfully logged in and can now use our services.")
                break
            else:
                messagebox.showinfo(
                    "Wrong information",
                    "Incorrect Username and/or Password")
                break

        conn.commit()
        conn.close()
        conn.close()
