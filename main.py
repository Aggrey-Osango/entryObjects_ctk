import customtkinter as ctk
# from tkinter import *
import tkinter as tk

# Intializing the app
ctk.set_default_color_theme ("blue")
ctk.set_appearance_mode ("light")

# Initializing the ctk app obj
app = ctk.CTk ()
app.geometry("600x520")
app.title ("Helium Notes")


frame = ctk.CTkFrame (master = app, width = 590, height = 510, corner_radius = 10,)
frame.pack (padx=10, pady=10)

# Entry obj
user_id = (ctk.CTkEntry
           (master = frame, corner_radius = 10, placeholder_text = "User Name."))

user_password = (ctk.CTkEntry
                 (master = frame, corner_radius = 10, show="*"))

uid = "aggrey"
upwd = "1234"
text_var = tk.StringVar()

def check_user():
    uname = user_id.get ()
    user_pwd = user_password.get ()
    if (uname == uid) and (user_pwd == upwd):
        text_var.set("User Connected")
        print ( f"User Name: {uname}\nPassword: {user_pwd}" )
    else:
        text_var.set("Wrong User ID or Password")
        print("Wrong User Id or Password, Confirm your entry and try again")
        print ( f"User Name: {uname}\nPassword: {user_pwd}" )

btn_01 = ctk.CTkButton (master = frame, text = "Submit", command = check_user)
msg_lbl = ctk.CTkLabel (master = frame, textvariable=text_var)



user_id.place(relx=0.5, rely=0.4, anchor = tk.CENTER)
user_password.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
btn_01.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
msg_lbl.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

if __name__ == '__main__':
    app.mainloop ()