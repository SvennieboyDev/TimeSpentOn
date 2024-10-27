#Gestart op 27 oktober 2024

import kivy
import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

class MainWindow(MDScreen):
    pass

class WindowManager(MDScreenManager):
    pass

class TimeSpentOn(MDApp):
    def build(self):
        self.title = "Time Spent On"

        kv = Builder.load_file("timespenton.kv")
        return kv
    
if __name__ == "__main__":
    TimeSpentOn().run()