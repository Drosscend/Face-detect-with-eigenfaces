# IL EST UTILISÉ POUR CAPTURER ET STOCKER LES PHOTOS AFIN D'ENTRAÎNER LES SYSTÈMES DE RECONNAISSANCE FACIALE. DES
# AJOUTS SPÉCIAUX SONT FAITS POUR SAUVEGARDER LES IMAGES UNIQUEMENT AVEC UN ÉCLAIRAGE CORRECT ET DES TÊTES INCLINÉES
# CORRECTES

import cv2  # Importing the opencv
import numpy as np  # Import Numarical Python
import NameFind  # Import NameFind function


def capture(cap):
    WHITE = [255, 255, 255]

    #   import the Haar cascades for face ditection
    face_cascade = cv2.CascadeClassifier(
        '../Haar/haarcascade_frontalcatface.xml')  # Classifier "frontal-face" Haar Cascade

    ID = NameFind.AddName()
    Count = 0

    while Count < 50:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the Camera to grayScale
        if np.average(gray) > 110:  # Testing the brightness of the image
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Detect the faces and store the positions
            for (x, y, w, h) in faces:  # Frames  LOCATION X, Y  WIDTH, HEIGHT
                FaceImage = gray[y - int(h / 2): y + int(h * 1.5),
                            x - int(x / 2): x + int(w * 1.5)]  # The Face is isolated and cropped
                Img = (NameFind.DetectEyes(FaceImage))
                cv2.putText(gray, "FACE DETECTED", (x + int((w / 2)), y - 5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)

                if Img is not None:
                    frame = Img  # Show the detected faces
                else:
                    frame = gray[y: y + h, x: x + w]
                cv2.imwrite("dataSet/User." + str(ID) + "." + str(Count) + ".jpg", frame)
                cv2.waitKey(300)
                cv2.imshow("CAPTURED PHOTO", frame)  # show the captured image
                Count = Count + 1
        cv2.putText(gray, "Photo restante a etre prise :" + str(Count) + "/50", (10, 10), cv2.FONT_HERSHEY_DUPLEX,
                    .4,
                    WHITE)
        cv2.putText(gray, "Appuyer sur \"q\" pour quitter le programme", (10, 30), cv2.FONT_HERSHEY_DUPLEX, .4,
                    WHITE)
        cv2.imshow('Système de reconnaissance des visages Capture des visages', gray)  # Show the video
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print('La capture du visage du sujet est terminé')
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture(cv2.VideoCapture(1))
