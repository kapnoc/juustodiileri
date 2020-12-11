
from kivy.storage.dictstore import DictStore
import pickle

from juustodiileri import config


def save_session(session):
    store = DictStore(config.STORE_PATH)
    store.put('session', serialized=pickle.dumps(session))


def get_session():
    store = DictStore(config.STORE_PATH)
    if store.exists('session'):
        serialized = store.get('session')['serialized']
        return pickle.loads(serialized)
    return None
