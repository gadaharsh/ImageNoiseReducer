if __name__ == '__main__':
    from tkinter import *
    from PIL import ImageTk, Image
    from tkinter import filedialog
    from tkinter.font import Font
    from tkinter import messagebox
    import cv2
    import os
    from open_about import *

    # Root Window
    root = Tk()
    root.title(" Image Noise Reduction ")
    root.iconbitmap("Recources/Photos.ico")
    root.geometry("1000x700")

    image = Image.open("Recources/latest_bg.png")
    image = image.resize((1000, 700), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(image)

    # Create A Canvas
    canvas = Canvas(root, width=1000, height=700)

    canvas.pack(fill="both", expand=True)

    # Set bg-image in canvas
    canvas.create_image(0, 0, image=bg, anchor="nw")




    # Reduce Noise Function
    def reduce_noise():
        global result_image
        global result_image_label

        noise_img = cv2.imread(root.filename)
        #destination="D:\WriteUps&Theory\py_codes\OSPTL_MiniProject\WithoutNoise"

        # Choose directory to save
        root.directory = filedialog.askdirectory(initialdir="..\OSPTL_MiniProject", title="Select A Directory To Save Image")

        path = root.directory
        # Getting name of img file
        head, tail = os.path.split(root.filename)
        name, extension = tail.split(".")

        denoise = cv2.fastNlMeansDenoisingColored(noise_img, None, 35, 30, 7, 21)
        cv2.imwrite(os.path.join(path, name+"_converted.png"), denoise)

        new_name = name+"_converted.png"

        result_image = ImageTk.PhotoImage(Image.open(path+"/"+new_name))
        result_image_label = Label(root, image=result_image)
        result_image_label.place(x=605, y=200)
        #result_image_label.grid(row=1, column=0, pady=10)



    # Select file function
    def open_file():

        global my_img
        global my_img_label
        global select_entry
        global reduce_img
        global clear_image
        global reduce_button
        global clear_button
        global result_image_label

        root.filename = filedialog.askopenfilename(initialdir="..\OSPTL_MiniProject", title="Select A File",
                                                   filetypes=(("All files", "*.*"), (" png files", "*.png"),
                                                              ("jpg files", "*.jpg"),))

        # Selecting Entry widget :  Just for viewing the image location
        entry = StringVar()
        select_entry = Entry(frame_left, textvariable=entry, width=50, borderwidth=0)
        select_entry.grid(row=0, column=1)
        entry.set(root.filename)

        # Setting the image and its label
        my_img = ImageTk.PhotoImage(Image.open(root.filename))
        my_img_label = Label(root, image=my_img)
        my_img_label.place(x=65, y=200)


        # Reduce Button
        reduce_img = ImageTk.PhotoImage(Image.open("Recources/arrow.png"))
        reduce_button = Button(root, image=reduce_img, borderwidth=0, command=reduce_noise)
        reduce_button.place(x=480, y=350)

        # Clear Button
        clear_image = ImageTk.PhotoImage(Image.open("Recources/Clear.png"))
        clear_button = Button(root, image=clear_image, command=clear, borderwidth=0)
        clear_button.place(x=470, y=160)

        # result_image_top = ImageTk.PhotoImage(Image.open("Recources/ResultImage.png"))
        # result_image_top_label = Label(root, image=result_image_top, borderwidth=0)
        # result_image_top_label.place(x=670, y=150)



    # Clear function
    def clear():
        reduce_button.place_forget()
        select_entry.grid_forget()
        clear_button.place_forget()
        my_img_label.place_forget()
        result_image_label.place_forget()


    # Frame Creation
    #frame_left = Frame (root, width=421, height=30)
    frame_left = Frame(root, width=421, height=400)
    frame_left.place(x=30, y=160)

    # File Selection In Frame
    select_button = Button (frame_left, text="Select an Image", command=open_file)
    select_button.grid(row=0, column=0)



    # About Button and Additional func in Frame_top
    #frame_top = Frame(root, height=65, width=110)
    #frame_top.place(x=710, y=40)

    about = ImageTk.PhotoImage(Image.open("Recources/About.png"))
    about_button = Button(root, image=about, borderwidth=0, command=open_about_window)
    about_button_win = canvas.create_window(920, 40, anchor="ne", window=about_button)
    #about_button.grid(row=0, column=1,padx=20)

    plus = ImageTk.PhotoImage(Image.open("Recources/plus.png"))
    plus_button = Button(root, image=plus, borderwidth=0)
    plus_button_win = canvas.create_window(760, 40, anchor="ne", window=plus_button)
    #plus_button.grid(row=0, column=0,padx=20)


    root.mainloop()