"""
Wilkommen zum zweiten Programm auf dem Weg zu einem funktionsfaehigem 
linsenlosen Mikroskop fuer unter 10 Euro.

Falls Sie Probleme mit diesem Programm haben sollten, schauen Sie sich bitte
die vorherigen Programme an oder besuchen Sie die Tutorials auf YouTube.

In diesem Programm soll gezeigt werden:
- wie man ein selbst geschriebenes Modul in sein Programm 
  benutzerfreundlich importiert
- wie dieses Modul augerufen wird und sich somit viele Zeilen Programmcode 
  gespart werden koennen

Fuehlen Sie sich wie immer frei, alle Einstellung zu veraendern und zu sehen was 
passiert.


Viel Spass beim ausprobieren!
"""

# importiere das Modul was sich im SELBEN Ordner befindet
# importiere es mit einem viel kuerzeren Namen (kM statt KameraModul)
import KameraModul as kM


##########################################
# Einstellungen

kamera = 2
wCam, hCam = 640, 480 


laufzeit_videoansicht = 5 # sekunden

Speicherort = "Experiment-01"
gif_name = "05_BenutzeKameramodul"

anzahl_Bilder = 30	

# Kameraeinstellungen
Helligkeit = 30
Kontrast = 40
Saettigung = 70
Hue = 0 # spiegelt sozusagen die Hauptfarbe wieder (auch negative Werte)
Gain=0
Belichtung=0
Weissabgl = 0

##########################################

# initialisiere die Kamera als variable "meine_Kamera" indem die Kamera zu einem
# Objekt aus dem KameraModul kM gemacht wird.

# ruft das KameraModul (kM) auf und geht in class Kameramodul
meine_Kamera = kM.Kameramodul(kamera, wCam, hCam)



# nun hat die Variable "meine_Kamera" die Funktionen:
# 'kameraeinstellungen', 'videoansicht' und 'videoaufnahme'
# die ueber 'meine_Kamera.Funktionsname' aufgerufen werden koennen

meine_Kamera.kameraeinstellungen(Helligkeit, Kontrast, 
							Saettigung, Hue, Gain,
							Belichtung,Weissabgl)
	
	
# starte die Videoansicht
meine_Kamera.videoansicht(laufzeit_videoansicht)	

# speichere das Video
meine_Kamera.videoaufnahme(Speicherort, gif_name, anzahl_Bilder)













































