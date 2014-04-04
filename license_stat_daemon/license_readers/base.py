import datetime
import os
import subprocess

class LicenseServer(object):
    def __init__(self, address, name=None, handlers=[]):
        self._address = address
        self._name = name
        self._handlers = handlers
        if self._name == None:
            self._name == self._address
   
    @property
    def features(self):
        features = []
        for h in self._handlers:
            features.extend(h.features)
        return features

class BaseHandler(object):
    BIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'bin'))
    def __init__(self, binary, server, port):
        self._features = []
        self._type = None
        self._binary = binary
        self._server = server
        self._port = port
        self._args = []
        pass

    @property
    def features(self):
        return self._features
    
    @property 
    def executable(self):
        return os.path.join(self.BIN_DIR, self._binary)

    def query(self):
        address = "%s@%s" % (self._port, self._server)
        args = [self.executable] + self._args + [address]
        return self._execute(args)

    def _execute(self, args):
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        return p.communicate()

class Feature(object):
    def __init__(self, name, checkouts=[]):
        self._name = name
        self._checkouts = checkouts
        self._available = 0
        self._total = 0
        pass

    @property
    def available(self):
        pass


class Checkout(object):
    def __init__(self, user, machine, date=None):
        self._user = user
        self._machine = machine
        self._date = date
        pass


def main():
    handler = BaseHandler('lmutil.bat', 'lalic01.zoicstudios.com', 27001)
    stdout, null =  handler.query()
    for l in stdout.splitlines():
        print l

    pass

if __name__ == '__main__':
    main()


