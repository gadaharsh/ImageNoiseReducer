from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import cv2
import os


def reduce_noise():
    global root1
    global result_image
    global result_image_label
    global path1

    noise_img = cv2.imread(path1)
    # destination="D:\WriteUps&Theory\py_codes\OSPTL_MiniProject\WithoutNoise"

    # Choose directory to save
    path1_dir = filedialog.askdirectory(initialdir="..\OSPTL_MiniProject",
                                             title="Select A Directory To Save Image")

    path = path1_dir
    # Getting name of img file
    head, tail = os.path.split(path1)
    name, extension = tail.split(".")

    denoise = cv2.fastNlMeansDenoisingColored(noise_img, None, 35, 30, 7, 21)
    cv2.imwrite(os.path.join(path, name + "_converted.png"), denoise)

    new_name = name + "_converted.png"

    result_image = ImageTk.PhotoImage(Image.open(path + "/" + new_name))
    result_image_label = Label(noise_canvas, image=result_image)
    result_image_label.place(x=605, y=200)
    # result_image_label.grid(row=1, column=0, pady=10)


def clear():

    reduce_button.place_forget()
    select_entry.grid_forget()
    clear_button.place_forget()
    my_img_label.place_forget()
    result_image_label.place_forget()

def noise():
    global noise_bg
    global back_image
    global about_bg
    global frame_left
    global noise_canvas

    root1 = Toplevel()
    root1.title(" Image Noise Reduction ")
    root1.iconbitmap("Recources/Photos.ico")
    #root4.geometry("1000x700")

    noise_bg = ImageTk.PhotoImage(Image.open("Recources/root1_bg.png"))

    noise_canvas = Canvas(root1, width=1000, height=700)
    noise_canvas.pack(fill="both", expand=True)
    noise_canvas.create_image(0, 0, image=noise_bg, anchor="nw")

    back_image = ImageTk.PhotoImage(Image.open("Recources/back.png"))
    back_button = Button(root1, image=back_image, borderwidth=0, command=root1.destroy)
    back_button.place(x=10, y=10)

    # Frame Creation

    frame_left = Frame(root1, width=421, height=400)
    frame_left.place(x=30, y=160)

    # File Selection In Frame
    select_button = Button(frame_left, text="Select an Image", command=open_file)
    select_button.grid(row=0, column=0)

    #root4.mainloop()

def open_file():
    global root1
    global my_img
    global my_img_label
    global select_entry
    global reduce_img
    global clear_image
    global reduce_button
    global clear_button
    global result_image_label
    global frame_left
    global path1

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
    my_img_label = Label(noise_canvas, image=my_img)
    my_img_label.place(x=65, y=200)

    # Reduce Button
    reduce_img = ImageTk.PhotoImage(Image.open("Recources/arrow.png"))
    reduce_button = Button(noise_canvas, image=reduce_img, borderwidth=0, command=reduce_noise)
    reduce_button.place(x=480, y=350)

    # Clear Button
    clear_image = ImageTk.PhotoImage(Image.open("Recources/Clear.png"))
    clear_button = Button(noise_canvas, image=clear_image, command=clear, borderwidth=0)
    clear_button.place(x=470, y=160)

