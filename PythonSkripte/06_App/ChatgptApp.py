"""
Diese App ist eine einfache Kivy-App, die eine Kamera öffnet und das Bild in einem Image-Widget anzeigt.
Es gibt einen Button, um die Kamera zu starten und zu stoppen.
"""


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        
        # verknuepfe die Klasse mit der "Elternklasse" BoxLayout from MainWindow(BoxLayout) und
        # initialisiere die Elternklasse mit den Argumenten, die der Klasse uebergeben werden
        super(MainWindow, self).__init__(**kwargs)


        """
        Hier wird die App initialisiert. 
        Es wird initialisiert, dass die Kamera ausgeschaltet ist.
        Es wird Image() erstellt, um das Kamerabild spaeter als "Image Widget" darzustellen.
        Es wird ein Image-Widget erstellt, um das Kamerabild anzuzeigen.

        Es wird ein Button erstellt und an eine Maus Interaktion gebunden 
        (bind on release) und dann hinzugefuegt (add widget)

        Am Anfang wird unser indikator "pause" oder "keine pause" auf False gesetzt.  
        """        
        self.capture = None
        self.image = Image()
        self.add_widget(self.image)

        self.control_button = Button(text='Start', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5})
        self.control_button.bind(on_release=self.control_camera)
        self.add_widget(self.control_button)

        self.end_button = Button(text='End App', size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5})
        self.end_button.bind(on_release=self.stop_App)
        self.add_widget(self.end_button)

        self.paused = False


    def stop_App(self, *args):
        # hier wird die App beendet
        App.get_running_app().stop()


    def control_camera(self, *args):
        """
        Diese Funktion wird immer aufgerufen, wenn ein BIND event (also ein klick auf den button)
        stattfindet.
        Diese Funktion is am start self.capture=None, sodass die Kamera beim Klick auf den Button
        gestartet wird.
        Danach wird immer zwischen self.paused =True und False hin und her geschaltet und
        self.capture is not None da die Kamera schon gestartet wurde."""

        if self.capture is None:
            self.start_camera()
        elif self.paused:
            self.resume_camera()
        else:
            self.pause_camera()

    def start_camera(self):
        # das kennen wir bereits
        self.capture = cv2.VideoCapture(0)

        # hier setzen wir eine Update Rate von 30 fps fuer die App
        Clock.schedule_interval(self.update_frame, 1.0 / 30.0)

        # hier aendern wir den Text des Buttons
        self.control_button.text = 'Pause'

    def pause_camera(self):
        self.paused = True
        self.control_button.text = 'Resume'

    def resume_camera(self):
        self.paused = False
        self.control_button.text = 'Pause'

    def update_frame(self, *args):
        # das kennen wir bereits
        if not self.paused:
            kamera_an, frame = self.capture.read()

            if kamera_an:
                # benutze "Textures" in Kivy um das Bild anzuzeigen
                texture = self.frame_to_texture(frame)
                self.image.texture = texture

    def frame_to_texture(self, frame):
        # Diese Funktion konvertiert das Bild in ein Texture Objekt, das von Kivy verwendet werden kann.
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
        flipped_frame = cv2.flip(frame, 0)
        texture.blit_buffer(flipped_frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        return texture

    def on_stop(self):
        if self.capture:
            self.capture.release()


class MyApp(App):
    # build the app and run permanently
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
