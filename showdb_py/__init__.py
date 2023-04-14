__author__ = "show-nosql.com / Showdown76#0001"
__version__ = '0.2'
__about__ = 'For ShowNoSQL'

import requests, time
_user = ''
_password = ''

def checkIfLogged() -> bool:
    return _user == '' or _password == ''


def getDb() -> dict:
    if checkIfLogged(): return print('! Not logged. Check your variable for details.')
    resp = requests.get(f'https://show-nosql.com/api/db?user={_user}&password={_password}')
    if resp.status_code != 200:
        print(resp.text)
        return
    return resp.json()

def optionsDb() -> dict:
    if checkIfLogged(): return print('! Not logged. Check your variable for details.')
    resp = requests.options(f'https://show-nosql.com/api/db?user={_user}&password={_password}')
    if resp.status_code != 200:
        print(resp.text)
        return
    return resp.json()

def setDb(data) -> None:
    if checkIfLogged(): return print('! Not logged. Check your variable for details.')
    resp = requests.post(f'https://show-nosql.com/api/db?user={_user}&password={_password}', json=data)
    if resp.status_code != 200:
        print(resp.text)
        return
    return


class Mapping(dict):
    def __setitem__(self, key, item):
        self.__dict__ = getDb()
        self.__dict__[key] = item
        setDb(self.__dict__)

    def __getitem__(self, key):
        self.__dict__ = getDb()
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        self.__dict__ = getDb()
        return len(self.__dict__)

    def __delitem__(self, key):
        self.__dict__ = getDb()
        del self.__dict__[key]
        setDb(self.__dict__)

    def clear(self):
        self.__dict__ = getDb()
        setDb({})
        return self.__dict__.clear()

    def copy(self):
        self.__dict__ = getDb()
        new_mapping = Mapping()
        for (item, value) in self.__dict__.items():
            new_mapping[item] = value
        return new_mapping

    def has_key(self, k):
        self.__dict__ = getDb()
        return k in self.__dict__

    def api_post(self) -> None:
        return setDb(self.__dict__)
    
    def api_reload(self) -> None:
        self.__dict__ = getDb()
        return
    
    def api_details(self) -> dict:
        return optionsDb()
    
    def update(self, *args, **kwargs):
        self.__dict__ = getDb()
        self.__dict__.update(*args, **kwargs)
        return setDb(self.__dict__)

    def keys(self):
        self.__dict__ = getDb()
        return self.__dict__.keys()

    def values(self):
        self.__dict__ = getDb()
        return self.__dict__.values()

    def items(self):
        self.__dict__ = getDb()
        return self.__dict__.items()

    def pop(self, *args):
        self.__dict__ = getDb()
        cd = self.__dict__.copy()
        for arg in args:
            if arg in cd:
                del cd[arg]
        setDb(self.__dict__)
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        self.__dict__ = getDb()
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

def connect(user: str, password: str, enable_stdout_logs: bool=True) -> Mapping:
    global _user, _password
    if enable_stdout_logs: print('[ShowNoSQL] Connecting...')
    req = requests.get(f'https://show-nosql.com/api/db?user={user}&password={password}')
    if req.status_code != 200:
        print(req.text)
        return {"not_logged": {'json_error': req.text}}
    if enable_stdout_logs: print('[ShowNoSQL] Connected')
    _user = user
    _password = password
    mapping = Mapping()
    mapping.update(req.json())
    if enable_stdout_logs: print('[ShowNoSQL] Ready')
    return mapping

