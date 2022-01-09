# import libraries for create a interface
import tkinter as tk
from tkinter import *
import cv2
from Face_Capture_With_Rotate import capture as capture_face
from Trainer_All import init as init_trainer
from Recogniser_Video_EigonFace import init as init_video


def open_window_1():
    capture_face(cv2.VideoCapture(1))


def open_window_2():
    init_trainer()


def open_window_3():
    init_video()


def create_window():
    # create a window
    window = tk.Tk()
    window.title("TKINTER")
    window.geometry("800x400")
    window.resizable(width=False, height=False)
    window.configure(background='#ffffff')

    # Create a title label and add it at the to of the window
    title_label = Label(window, text="Eigenface : Programme de reconnaissance faciale", font=("Arial", 20),
                        bg='#ffffff')
    title_label.pack(side=TOP, fill=X)

    # Create 3 buttons and add it athe center of the window
    button_1 = Button(window, text="Capturer un visage", font=("Arial", 15), bg='#d9d9d9',
                      command=open_window_1)
    button_1.pack(side=TOP, fill=X, padx=130, pady=20, ipadx=50, ipady=10)
    button_2 = Button(window, text="Entrener l'application", font=("Arial", 15), bg='#d9d9d9',
                      command=open_window_2)
    button_2.pack(side=TOP, fill=X, padx=130, pady=20, ipadx=50, ipady=10)
    button_3 = Button(window, text="Reconnaitre une personne ou plusieurs", font=("Arial", 15),
                      bg='#d9d9d9', command=open_window_3)
    button_3.pack(side=TOP, fill=X, padx=130, pady=20, ipadx=50, ipady=10)

    # create a quit button and add it at the bottom of the window
    quit_button = Button(window, text="Quitter", font=("Arial", 15), bg='#d9d9d9', command=window.destroy)
    quit_button.pack(side=BOTTOM, fill=X, padx=130, pady=20, ipadx=50, ipady=10)

    window.mainloop()


# create a main window
if __name__ == '__main__':
    create_window()
