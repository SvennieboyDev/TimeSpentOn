#Gestart op 22 oktober 2024

import kivy
import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

class StartWindow(MDScreen):
    pass

class MainWindow(MDScreen):
    pass

class WindowManager(MDScreenManager):
    pass

class TimeSpentOn(MDApp):
    def build(self):
        self.title = "Time Spent On"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"

        kv = Builder.load_file("timespenton.kv")
        return kv

if __name__ == "__main__":
    TimeSpentOn().run()