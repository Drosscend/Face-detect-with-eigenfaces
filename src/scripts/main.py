from tkinter import *
import cv2
import Face_Capture_With_Rotate
import Trainer_All
import Recogniser_Video_EigonFace


def detect(video):
    Face_Capture_With_Rotate.capture(video)


def train():
    Trainer_All.init()


def recogniser():
    Recogniser_Video_EigonFace.init()


if __name__ == "__main__":
    root = Tk()
    root.title('Programme EigonFace')
    root.resizable(width=False, height=False)
    cap = cv2.VideoCapture(1)

    bouton1 = Button(root, text='Capturer les photos', command=lambda: detect(cap))
    bouton1.pack(side=LEFT, padx=5, pady=5)
    bouton2 = Button(root, text='Entrainer le programme', command=lambda: train())
    bouton2.pack(side=LEFT, padx=5, pady=5)
    bouton3 = Button(root, text='Detection', command=lambda: recogniser())
    bouton3.pack(side=LEFT, padx=5, pady=5)

    bouton4 = Button(root, text='Quitter', command=root.quit)
    bouton4.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
