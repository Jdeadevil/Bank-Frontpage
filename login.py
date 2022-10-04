from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sqlite3

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

HEADER_FONT = ("Calibri", 24, "bold")
SMALLER_FONT = ("Calibri", 12, "bold")
EVEN_SMALLER_FONT = ("Calibri", 9)


class LoginScreen:
    def __init__(self):
        super().__init__()

        self.image_frame = customtkinter.CTkFrame(width=643, height=429)
        self.image_frame.pack()

        self.splash = ImageTk.PhotoImage(Image.open("splash_screen_trimmed.jpg"))

        self.image_label = customtkinter.CTkLabel(
            self.image_frame, text_font=SMALLER_FONT, image=self.splash
        )
        self.image_label.place(anchor="center", x=643//2, y=429//2)

        self.login_frame = customtkinter.CTkFrame()
        self.login_frame.place(anchor="nw", height=214, width=643, x=0, y=429)

        self.login_header = customtkinter.CTkLabel(
            self.login_frame, text="Login", text_font=HEADER_FONT, padx=0, pady=0
        )
        self.login_header.place(anchor="center", x=322, y=29)

        self.login_username = customtkinter.CTkLabel(
            self.login_frame, anchor="w", text="Username: ", text_font=SMALLER_FONT
        )
        self.login_username.place(anchor="center", x=205, y=76)

        self.login_password = customtkinter.CTkLabel(
            self.login_frame, anchor="w", text="Password: ", text_font=SMALLER_FONT
        )
        self.login_password.place(anchor="center", x=204, y=124)

        self.login_entry = customtkinter.CTkEntry(self.login_frame, width=230)
        self.login_entry.place(anchor="center", x=373, y=75)

        self.password_entry = customtkinter.CTkEntry(
            self.login_frame, width=230, show="*"
        )
        self.password_entry.place(anchor="center", x=373, y=125)

        self.login_button = customtkinter.CTkButton(
            self.login_frame,
            text="Login",
            text_font=SMALLER_FONT,
            corner_radius=30,
            width=120,
            command=self.validate_database
        )
        self.login_button.place(anchor="center", x=249, y=175)

        self.register_button = customtkinter.CTkButton(
            self.login_frame,
            text="Register",
            text_font=SMALLER_FONT,
            corner_radius=30,
            width=120,
        )
        self.register_button.place(anchor="center", x=395, y=175)

        # Validation Text
        self.validation_text = customtkinter.CTkLabel(
            self.login_frame, text="", text_font=EVEN_SMALLER_FONT)
        self.validation_text.place(anchor="center", x=545, y=175)

    def validate_database(self):
        conn = sqlite3.connect('customers.db')
        c = conn.cursor()

        c.execute("SELECT * FROM customers")
        for index in c.fetchall():
            if index[0] == self.login_entry.get() and index[1] == self.password_entry.get():
                self.validation_text.configure(text_color='#118408', text="Correct!\nCome on in! :)")
                break
            else:
                self.validation_text.configure(text_color='#7c0000', text="Incorrect Username\nand/or Password")

        conn.commit()
        conn.close()
        conn.close()