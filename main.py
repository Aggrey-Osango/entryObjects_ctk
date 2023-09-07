import customtkinter as ctk
# from tkinter import *
import tkinter as tk


# Intializing the app
ctk.set_default_color_theme ("blue")
ctk.set_appearance_mode ("light")

app_geometry = "600x520"

radius = [1,2,3,4,5,6,7,8,9,10]
rect_width, rect_height = 170, 35
framex, framey = 590, 510

corner_r, padding = 10, 10


#Initializing the ctk app obj
app = ctk.CTk ()
app.geometry(app_geometry)
app.title ("Helium Notes")

text_var = tk.StringVar()

frame =\
    ctk.CTkFrame (master = app, width = framex, height = framey, corner_radius = corner_r)

frame.pack (padx=padding, pady=padding)

# Entry obj
user_id =\
    ctk.CTkEntry (master = frame, width  = rect_width, height = rect_height, corner_radius = corner_r,
                  placeholder_text = "User Name.")

user_password =\
    ctk.CTkEntry (master = frame, width = rect_width, height = rect_height, corner_radius = corner_r, show="*")



def check_user():
    uname = user_id.get ()
    user_pwd = user_password.get ()

    if (uname == "aggrey") and (user_pwd == "1234"):
        text_var.set("User Connected")
        print ( f"User Name: {uname}\nPassword: {user_pwd}" )
    else:
        text_var.set("Wrong User ID or Password")
        print("Wrong User Id or Password, Confirm your entry and try again")
        print ( f"User Name: {uname}\nPassword: {user_pwd}" )

btn_01 = ctk.CTkButton (master = frame,
                        width  = rect_width,
                        height = rect_height,
                        text = "Submit", command = check_user)

msg_lbl = ctk.CTkLabel (master = frame, textvariable=text_var)


# binding widgets to the frame and the app window
user_id.place(relx=0.5, rely=0.4, anchor = tk.CENTER)

user_password.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

btn_01.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

msg_lbl.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

if __name__ == '__main__':
    app.mainloop ()