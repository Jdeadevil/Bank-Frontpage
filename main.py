import customtkinter
import login


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("643x643")
        self.resizable(False, False)
        self.title("Prosperity Finances Banking Group")

        login.LoginScreen()


if __name__ == "__main__":
    app = App()
    app.mainloop()