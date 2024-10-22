#Gestart op 22 oktober 2024

import kivy
import kivymd
from kivymd.app import App
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.widget import Widget
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class StartWindow(Screen):
    pass

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("timespenton.kv")

class TimeSpentOn(App):
    def build(self):
        self.title = "Time Spent On"
        return kv

if __name__ == "__main__":
    TimeSpentOn().run()