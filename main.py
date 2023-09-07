import customtkinter as ctk
# from tkinter import *

# intializing the app
ctk.set_default_color_theme ("blue")
ctk.set_appearance_mode ("light")

# Initializing the ctk app obj
app = ctk.CTk ()
app.geometry("600x520")
app.title ("Helium Notes")

if __name__ == '__main__':
    app.mainloop ()

