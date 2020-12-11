
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

from juustodiileri.utils.session import get_session
from juustodiileri.widgets.login import LoginScreen
from juustodiileri.widgets.logged_in import LoggedInScreen


class NavigationDrawerContents(BoxLayout):
    pass


class MainScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        manager = ScreenManager()
        if get_session() is None:
            manager.add_widget(LoginScreen(name='login'))
            manager.add_widget(LoggedInScreen(name='logged_in'))
            manager.current = 'login'
        else:
            manager.add_widget(LoggedInScreen(name='logged_in'))
            manager.add_widget(LoginScreen(name='login'))
            manager.current = 'logged_in'

        return manager
