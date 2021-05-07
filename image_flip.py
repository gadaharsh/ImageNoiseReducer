from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import cv2
import os

def horizontalflip():
    global root3
    global path1
    global result_image
    global result_image_label

    to_flip = cv2.imread(path1)

    path2_dir = filedialog.askdirectory(initialdir="..\OSPTL_MiniProject",
                                        title="Select A Directory To Save Image")

    path = path2_dir

    # Getting name of img file
    head, tail = os.path.split(path1)
    name, extension = tail.split(".")

    # img_flip_ud = cv2.flip(img, 1)
    h_flipped = cv2.flip(to_flip, 1)
    cv2.imwrite(os.path.join(path, name + "_hflipped.png"), h_flipped)

    new_name = name + "_hflipped.png"

    result_image = ImageTk.PhotoImage(Image.open(path + "/" + new_name))
    result_image_label = Label(flip_canvas, image=result_image)
    result_image_label.place(x=605, y=200)

def verticalflip():
    global root3
    global path1
    global result_image
    global result_image_label

    to_flip = cv2.imread(path1)

    path2_dir = filedialog.askdirectory(initialdir="..\OSPTL_MiniProject",
                                        title="Select A Directory To Save Image")

    path = path2_dir

    # Getting name of img file
    head, tail = os.path.split(path1)
    name, extension = tail.split(".")

    # img_flip_ud = cv2.flip(img, 0)
    v_flipped = cv2.flip(to_flip, 0)

    cv2.imwrite(os.path.join(path, name + "_vflipped.png"), v_flipped)

    new_name = name + "_vflipped.png"

    result_image = ImageTk.PhotoImage(Image.open(path + "/" + new_name))
    result_image_label = Label(flip_canvas, image=result_image)
    result_image_label.place(x=605, y=200)


def clear():
    flip_h_button.place_forget()
    flip_v_button.place_forget()
    select_entry.grid_forget()
    clear_button.place_forget()
    my_img_label.place_forget()
    result_image_label.place_forget()

def flip_fn():
    global rotate_bg
    global back_image
    global about_bg
    global frame_left
    global flip_canvas

    root3 = Toplevel()
    root3.title(" Image Flip ")
    root3.iconbitmap("Recources/Photos.ico")

    flip_bg = ImageTk.PhotoImage(Image.open("Recources/root3_bg.png"))

    flip_canvas = Canvas(root3, width=1000, height=700)
    flip_canvas.pack(fill="both", expand=True)
    flip_canvas.create_image(0, 0, image=flip_bg, anchor="nw")

    back_image = ImageTk.PhotoImage(Image.open("Recources/back.png"))
    back_button = Button(root3, image=back_image, borderwidth=0, command=root3.destroy)
    back_button.place(x=10, y=10)

    # Frame Creation

    frame_left = Frame(root3, width=421, height=400)
    frame_left.place(x=30, y=160)

    # File Selection In Frame
    select_button = Button(frame_left, text="Select an Image", command=open_file)
    select_button.grid(row=0, column=0)

    root3.mainloop()

def open_file():
    global root3
    global my_img
    global my_img_label
    global select_entry
    global clear_image
    global clear_button
    global frame_left
    global path1
    global flip_h_img
    global flip_v_img
    global flip_h_button
    global flip_v_button


    path1 = filedialog.askopenfilename(initialdir="..\OSPTL_MiniProject", title="Select A File",
                                       filetypes=(("All files", "*.*"), (" png files", "*.png"),
                                                          ("jpg files", "*.jpg"),))

    # Selecting Entry widget :  Just for viewing the image location
    entry = StringVar()
    select_entry = Entry(frame_left, textvariable=entry, width=50, borderwidth=0)
    select_entry.grid(row=0, column=1)
    entry.set(path1)

    # Setting the image and its label
    my_img = ImageTk.PhotoImage(Image.open(path1))
    my_img_label = Label(flip_canvas, image=my_img)
    my_img_label.place(x=65, y=200)

    # Convert Button1-clockwise rotate
    flip_h_img = ImageTk.PhotoImage(Image.open("Recources/h_flip.png"))
    flip_h_button = Button(flip_canvas, image=flip_h_img, borderwidth=0, command=horizontalflip)
    flip_h_button.place(x=480, y=300)

    # Convert Button2-anticlockwise rotate
    flip_v_img = ImageTk.PhotoImage(Image.open("Recources/v_flip.png"))
    flip_v_button = Button(flip_canvas, image=flip_v_img, borderwidth=0, command=verticalflip)
    flip_v_button.place(x=480, y=470)

    # Clear Button
    clear_image = ImageTk.PhotoImage(Image.open("Recources/Clear.png"))
    clear_button = Button(flip_canvas, image=clear_image, command=clear, borderwidth=0)
    clear_button.place(x=470, y=160)