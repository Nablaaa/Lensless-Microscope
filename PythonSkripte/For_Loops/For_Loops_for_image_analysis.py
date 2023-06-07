"""
Wilkommen zu einem kleinen Tutorial ueber einige hilfreiche Funktionen
in Python. Dieses Skript dient als kleine Hilfestellung, um die anderen
Programme besser zu verstehen. Es ist nicht notwendig, dass Sie dieses
Skript durcharbeiten, aber es kann sehr hilfreich sein.


In diesem Programm soll gezeigt werden:
- welche funktionen man in einer for-Schleife nutzen kann und warum
  man das machen sollte

- diese Funktionen sind:
    - range()
    - np.arange()
    - np.linspace()
    - enumerate()
    - np.unique()
    - zip()
    - sorted()
    - reversed()
    - break
    - continue

aber es gibt auch noch mehr

Fuehlen Sie sich wie immer frei, alle Einstellung zu veraendern und zu sehen was 
passiert.

Viel Spass beim ausprobieren!


dataset: https://www.epfl.ch/labs/cvlab/data/data-em/
(Ich empfehle nur die subgroup vom test datensatz herunterzuladen, da dieser
kleiner ist und schneller heruntergeladen werden kann)
"""
import os


# zeige jetzigen path
print(os.getcwd())

# Ordner mit den Bildern
raw_pfad = "PythonSkripte/For_Loops/Beispielbilder/raw/"
label_pfad = "PythonSkripte/For_Loops/Beispielbilder/label/"

# finde alle namen der bilder im ordner
raw_bildnamen = os.listdir(raw_pfad)
label_bildnamen = os.listdir(label_pfad)

print(raw_bildnamen)
print(label_bildnamen)





# importiere die bilder
import cv2


for i, (raw, label) in enumerate(zip(sorted(raw_bildnamen), sorted(label_bildnamen))):
    print(raw, label)
    raw_img = cv2.imread(raw_pfad + raw)
    label_img = cv2.imread(label_pfad + label)

    # zeige die bilder
    cv2.imshow("raw von bild " + str(i), raw_img)
    cv2.imshow("label von bild " + str(i), label_img)

    # show raw in blue channel and label in green channel in the same image
    raw_img[:,:,0] = 0
    raw_img[:,:,2] = 0
    label_img[:,:,1] = 0
    label_img[:,:,2] = 0
    cv2.imshow("raw_label von bild " + str(i), raw_img + label_img)


# warte auf eine taste
cv2.waitKey(0)

# schliesse alle fenster
cv2.destroyAllWindows()

