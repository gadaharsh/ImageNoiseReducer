if __name__ == '__main__':
    from tkinter import *
    from open_about import *
    from image_noise_reduction import *
    from image_rotate import *
    from image_flip import *
    from image_blur import *

    home = Tk()
    home.title(" Home : Image Noise Reduction ")
    home.iconbitmap("Recources/Photos.ico")
    home.geometry("1000x700")

    # Create A Canvas
    home_canvas = Canvas(home, width=1000, height=700)
    home_canvas.pack(fill="both", expand=True)

    # Put Image on home canvas
    home_bg = ImageTk.PhotoImage(Image.open("Recources/Home.png"))
    home_canvas.create_image(0, 0, image=home_bg, anchor="nw")

    # Put image noise reduction button
    home_noise = ImageTk.PhotoImage(Image.open("Recources/noise_reduce.png"))
    home_noise_button = Button(home, image=home_noise, borderwidth=0, command=noise)
    home_noise_button.place(x=135, y=195)

    # About Button
    about = ImageTk.PhotoImage(Image.open("Recources/About.png"))
    about_button = Button(home, image=about, borderwidth=0, command=open_about_window)
    about_button_win = home_canvas.create_window(920, 40, anchor="ne", window=about_button)

    # Additional Features

    #Image Rotate
    rotate = ImageTk.PhotoImage(Image.open("Recources/rotate.png"))
    rotate_button = Button(home, image=rotate, borderwidth=0, command=rotate_fn)
    rotate_button.place(x=105, y=445)

    # Image Flip
    flip = ImageTk.PhotoImage(Image.open("Recources/flip.png"))
    flip_button = Button(home, image=flip, borderwidth=0, command=flip_fn)
    flip_button.place(x=405, y=445)

    # Image Blur
    blur = ImageTk.PhotoImage(Image.open("Recources/blur.png"))
    blur_button = Button(home, image=blur, borderwidth=0, command=blur_fn)
    blur_button.place(x=705, y=445)


    home.mainloop()

