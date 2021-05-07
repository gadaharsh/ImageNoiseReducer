from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import cv2
import os

def rotate_right():
    global root2
    global path2
    global result_image
    global result_image_label

    to_rotate= cv2.imread(path2)

    path2_dir = filedialog.askdirectory(initialdir="..\OSPTL_MiniProject",
                                        title="Select A Directory To Save Image")

    path = path2_dir

    # Getting name of img file
    head, tail = os.path.split(path2)
    name, extension = tail.split(".")

    right_rotated = cv2.rotate(to_rotate, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(path, name + "_right_rotated.png"), right_rotated)

    new_name = name + "_right_rotated.png"

    result_image = ImageTk.PhotoImage(Image.open(path + "/" + new_name))
    result_image_label = Label(rotate_canvas, image=result_image)
    result_image_label.place(x=605, y=200)
    messagebox.showinfo("Image Rotate", "Successful Save and Right Rotation of Image!")

def rotate_left():
    global root2
    global path2
    global result_image
    global result_image_label

    to_rotate = cv2.imread(path2)

    path2_dir = filedialog.askdirectory(initialdir="..\OSPTL_MiniProject",
                                        title="Select A Directory To Save Image")

    path = path2_dir

    # Getting name of img file
    head, tail = os.path.split(path2)
    name, extension = tail.split(".")

    left_rotated = cv2.rotate(to_rotate, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(os.path.join(path, name + "_left_rotated.png"), left_rotated)

    new_name = name + "_left_rotated.png"

    result_image = ImageTk.PhotoImage(Image.open(path + "/" + new_name))
    result_image_label = Label(rotate_canvas, image=result_image)
    result_image_label.place(x=605, y=200)
    messagebox.showinfo("Image Rotate", "Successful Save and Left Rotation of Image!")

def clear():
    rotate_left_button.place_forget()
    rotate_right_button.place_forget()
    select_entry.grid_forget()
    clear_button.place_forget()
    my_img_label.place_forget()
    result_image_label.place_forget()

def rotate_fn():
    global rotate_bg
    global back_image
    global about_bg
    global frame_left
    global rotate_canvas

    root2 = Toplevel()
    root2.title(" Image Rotation ")
    root2.iconbitmap("Recources/Photos.ico")

    rotate_bg = ImageTk.PhotoImage(Image.open("Recources/root2_bg.png"))

    rotate_canvas = Canvas(root2, width=1000, height=700)
    rotate_canvas.pack(fill="both", expand=True)
    rotate_canvas.create_image(0, 0, image=rotate_bg, anchor="nw")

    back_image = ImageTk.PhotoImage(Image.open("Recources/back.png"))
    back_button = Button(root2, image=back_image, borderwidth=0, command=root2.destroy)
    back_button.place(x=10, y=10)

    # Frame Creation

    frame_left = Frame(root2, width=421, height=400)
    frame_left.place(x=30, y=160)

    # File Selection In Frame
    select_button = Button(frame_left, text="Select an Image", command=open_file)
    select_button.grid(row=0, column=0)

    root2.mainloop()

def open_file():
    global root2
    global my_img
    global my_img_label
    global select_entry
    global clear_image
    global clear_button
    global frame_left
    global path2
    global rotate_right_img
    global rotate_left_img
    global rotate_right_button
    global rotate_left_button


    path2 = filedialog.askopenfilename(initialdir="..\OSPTL_MiniProject", title="Select A File",
                                       filetypes=(("All files", "*.*"), (" png files", "*.png"),
                                                          ("jpg files", "*.jpg"),))

    # Selecting Entry widget :  Just for viewing the image location
    entry = StringVar()
    select_entry = Entry(frame_left, textvariable=entry, width=50, borderwidth=0)
    select_entry.grid(row=0, column=1)
    entry.set(path2)

    # Setting the image and its label
    my_img = ImageTk.PhotoImage(Image.open(path2))
    my_img_label = Label(rotate_canvas, image=my_img)
    my_img_label.place(x=65, y=200)

    # Convert Button1-clockwise rotate
    rotate_right_img = ImageTk.PhotoImage(Image.open("Recources/rotate_right.png"))
    rotate_right_button = Button(rotate_canvas, image=rotate_right_img, borderwidth=0, command=rotate_right)
    rotate_right_button.place(x=480, y=300)

    # Convert Button2-anticlockwise rotate
    rotate_left_img = ImageTk.PhotoImage(Image.open("Recources/rotate_left.png"))
    rotate_left_button = Button(rotate_canvas, image=rotate_left_img, borderwidth=0, command=rotate_left)
    rotate_left_button.place(x=480, y=470)

    # Clear Button
    clear_image = ImageTk.PhotoImage(Image.open("Recources/Clear.png"))
    clear_button = Button(rotate_canvas, image=clear_image, command=clear, borderwidth=0)
    clear_button.place(x=470, y=160)