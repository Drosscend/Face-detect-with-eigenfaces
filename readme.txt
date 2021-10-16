
Detector_Video.py : Ce fichier détecte les visages en utilisant des cascades de Haar. Il fonctionne bien avec plusieurs visages.

Face_Capture_With_Rotate.py : L'exécution de ce fichier va capturer 50 images d'une personne devant la caméra. Il s'assurera que les photos ne sont pas sombres et
et que le visage est droit.

Face_Rotate.py : Ce fichier montre la fonction de rotation. Assurez-vous de décommenter la ligne 153 dans NameFind.py. Cela montrera l'image en corrigeant le décalage.

NameFind.py : Ce fichier contient toutes les fonctions.

Trainer_All.py : Ce fichier va entraîner tous les algorithmes de reconnaissance en utilisant les images du dossier dataSet.

Recogniser_Video_EigenFace.py : Ce fichier va reconnaître les visages à partir de la caméra en utilisant l'algorithme Eigen face.


------------------FOLDERS -----------
dataSet --> Contains the images that will be used to train the recogniser.
Haar --> Contains Haar Cascades of OpenCV used in the applications
Recogniser --> Contains the saved XML files by reconisers