from tkinter import *
from PIL import ImageTk, Image


# Function open_about
def open_about_window():
    global back_image
    global about_bg

    # About Window
    about_window = Toplevel()
    about_window.title(" About ")
    about_window.iconbitmap("Recources/Photos.ico")


    about_bg = ImageTk.PhotoImage(Image.open("Recources/about_window.png"))

    # Create A Canvas
    about_canvas = Canvas(about_window, width=500, height=300)
    about_canvas.pack(fill="both", expand=True)
    about_canvas.create_image(0, 0, image=about_bg, anchor="nw")


    back_image= ImageTk.PhotoImage(Image.open("Recources/back.png"))

    back_button=Button(about_window, image=back_image, borderwidth=0, command=about_window.destroy)
    back_button.place(x=10, y=10)

    about_window.mainloop()