#!/bin/env python3

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class NavigationDrawerContents(BoxLayout):
    pass


class MainScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        return MainScreen()


MainApp().run()
