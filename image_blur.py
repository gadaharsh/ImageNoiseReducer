from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import cv2
import os


def imageblur():
    global root4
    global result_image
    global result_image_label
    global path4

    to_blur = cv2.imread(path4)
    # destination="D:\WriteUps&Theory\py_codes\OSPTL_MiniProject\WithoutNoise"

    # Choose directory to save
    path4_dir = filedialog.askdirectory(initialdir="..\OSPTL_MiniProject",
                                             title="Select A Directory To Save Image")

    path = path4_dir
    # Getting name of img file
    head, tail = os.path.split(path4)
    name, extension = tail.split(".")

    #blurred = cv2.fastNlMeansDenoisingColored(to_blur, None, 35, 30, 7, 21)
    #can change the kernel size as you want
    blurred = cv2.blur(to_blur, (10, 10))
    cv2.imwrite(os.path.join(path, name + "_blurred.png"), blurred)

    new_name = name + "_blurred.png"

    result_image = ImageTk.PhotoImage(Image.open(path + "/" + new_name))
    result_image_label = Label(blur_canvas, image=result_image)
    result_image_label.place(x=605, y=200)

def clear():

    blur_button.place_forget()
    select_entry.grid_forget()
    clear_button.place_forget()
    my_img_label.place_forget()
    result_image_label.place_forget()

def blur_fn():
    global blur_bg
    global back_image
    global about_bg
    global frame_left
    global blur_canvas

    root4 = Toplevel()
    root4.title(" Image Blur ")
    root4.iconbitmap("Recources/Photos.ico")
    #root4.geometry("1000x700")

    blur_bg = ImageTk.PhotoImage(Image.open("Recources/root4_bg.png"))

    blur_canvas = Canvas(root4, width=1000, height=700)
    blur_canvas.pack(fill="both", expand=True)
    blur_canvas.create_image(0, 0, image=blur_bg, anchor="nw")

    back_image = ImageTk.PhotoImage(Image.open("Recources/back.png"))
    back_button = Button(root4, image=back_image, borderwidth=0, command=root4.destroy)
    back_button.place(x=10, y=10)

    # Frame Creation

    frame_left = Frame(root4, width=421, height=400)
    frame_left.place(x=30, y=160)

    # File Selection In Frame
    select_button = Button(frame_left, text="Select an Image", command=open_file)
    select_button.grid(row=0, column=0)

    #root4.mainloop()

def open_file():
    global root4
    global my_img
    global my_img_label
    global select_entry
    global blur_img
    global clear_image
    global blur_button
    global clear_button
    global frame_left
    global path4

    path4 = filedialog.askopenfilename(initialdir="..\OSPTL_MiniProject", title="Select A File",
                                       filetypes=(("All files", "*.*"), (" png files", "*.png"),
                                                          ("jpg files", "*.jpg"),))

    # Selecting Entry widget :  Just for viewing the image location
    entry = StringVar()
    select_entry = Entry(frame_left, textvariable=entry, width=50, borderwidth=0)
    select_entry.grid(row=0, column=1)
    entry.set(path4)

    # Setting the image and its label
    my_img = ImageTk.PhotoImage(Image.open(path4))
    my_img_label = Label(blur_canvas, image=my_img)
    my_img_label.place(x=65, y=200)

    # Reduce Button
    blur_img = ImageTk.PhotoImage(Image.open("Recources/arrow.png"))
    blur_button = Button(blur_canvas, image=blur_img, borderwidth=0, command=imageblur)
    blur_button.place(x=480, y=350)

    # Clear Button
    clear_image = ImageTk.PhotoImage(Image.open("Recources/Clear.png"))
    clear_button = Button(blur_canvas, image=clear_image, command=clear, borderwidth=0)
    clear_button.place(x=470, y=160)
