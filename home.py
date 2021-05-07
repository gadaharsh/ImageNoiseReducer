if __name__ == '__main__':
    from tkinter import *
    from open_about import *

    home = Tk()
    home.title(" Home : Image Noise Reduction ")
    home.iconbitmap("Recources/Photos.ico")
    home.geometry("1000x700")

    image = Image.open("Recources/Home.png")
    #image = image.resize((1000, 700), Image.ANTIALIAS)
    home_bg = ImageTk.PhotoImage(image)

    # Create A Canvas
    #home_canvas = Canvas(home, width=1000, height=700)

    #home_canvas.pack(fill="both", expand=True)

    # Set bg-image in canvas
    #home_canvas.create_image(0, 0, image=home_bg, anchor="nw")

