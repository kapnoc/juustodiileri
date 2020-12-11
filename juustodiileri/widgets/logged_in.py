
from kivy.uix.screenmanager import Screen, CardTransition
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import OneLineListItem

from juustodiileri.utils.session import save_session


class NavigationDrawerContent(BoxLayout):
    pass


class LoggedInScreen(Screen):
    def disconnect(self, disconnect_list_item):
        save_session(None)
        self.ids.md_list.remove_widget(disconnect_list_item)
        self.manager.transition = CardTransition(direction='up')
        self.manager.current = 'login'

    def on_enter(self):
        self.ids.md_list.add_widget(
            OneLineListItem(text='Disconnect', on_press=self.disconnect)
        )
