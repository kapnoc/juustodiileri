
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition
import requests

from juustodiileri import config
from juustodiileri.utils.session import save_session


class LoginScreen(Screen):

    def login(self, username, password):
        session = requests.Session()
        res = session.post(
            f"{config.API_URL}/user/login/",
            data={
                'username': username,
                'password': password,
            }
        )
        try:
            res_json = res.json()
        except ValueError:
            print(res.text)
            return
        if res_json['success'] == True:
            save_session(session)
            self.manager.transition = CardTransition(direction='down')
            self.manager.current = 'logged_in'
