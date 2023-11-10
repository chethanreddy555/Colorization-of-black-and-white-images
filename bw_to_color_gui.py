from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Dialog Widget")
        self.minsize(500, 500)  # Adjusted the window size to show the image better

        self.labelFrame = ttk.LabelFrame(self, text='Input Image')
        self.labelFrame.grid(column=0, row=1, padx=3, pady=3)

        self.labelFrame1 = ttk.LabelFrame(self, text='Path')
        self.labelFrame1.grid(column=0, row=3, padx=3, pady=3)

        self.labelFrame2 = ttk.LabelFrame(self, text='Image')
        self.labelFrame2.grid(column=0, row=4, padx=3, pady=3)

        self.labelFrame3 = ttk.LabelFrame(self, text='Run')
        self.labelFrame3.grid(column=0, row=5, padx=3, pady=3)

        self.filename = None  # Added a variable to store the selected filename
        self.colorized_tk = None  # Added to store the colorized image Tkinter PhotoImage

        self.button()

    def button(self):
        self.button = ttk.Button(self.labelFrame, text='Browse File', width=50, command=self.fileDialog)
        self.button.grid(column=0, row=1)

        self.button1 = ttk.Button(self.labelFrame3, text='Run Program', width=50, command=self.runPro)
        self.button1.grid(column=0, row=1)

    def runPro(self):
        if self.filename is not None:
            colorized = self.colorizeImage(self.filename)

            # Show the colorized image in the GUI
            colorized_pil = Image.fromarray(colorized)
            self.colorized_tk = ImageTk.PhotoImage(colorized_pil)
            if hasattr(self, 'colorized_label'):
                self.colorized_label.grid_forget()  # Remove the previous image
            self.colorized_label = ttk.Label(self.labelFrame2, image=self.colorized_tk)
            self.colorized_label.image = self.colorized_tk
            self.colorized_label.grid(column=0, row=0)  # Adjusted the row to 0

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir='/', title='Select file',
                                                   filetype=(('jpeg', '*.jpg'), ('All Files', '*.*')))
        if self.filename:
            self.e1 = ttk.Entry(self.labelFrame1, width=50)
            self.e1.insert(0, self.filename)
            self.e1.grid(row=2, column=0, columnspan=50)
            self.runPro()  # Automatically run the colorization process after selecting the file

    def colorizeImage(self, filename):
        # Open and read the image using OpenCV
        original_image = cv2.imread(filename)

        # Convert the image to RGB format as OpenCV reads images in BGR format
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

        # Colorize the image (replace this with your colorization process)
        # For example, you can use a pre-trained model or any custom colorization method here.
        # In this example, we'll just create a grayscale version of the image.
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)
        colorized = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)

        return colorized


if __name__ == '__main__':
    root = Root()
    root.mainloop()
