import base

class FlexLMHandler(base.BaseHandler):
    def __init__(self, server, port):
        base.BaseHandler.__init__(self, 'lmutil', server, port)
        self._args = ['lmstat', '-a', '-c']

    def query(self):
        address = "%s@%s" % (self._port, self._server)
        args = [self.executable] + self._args + [address]
        return self._execute(args)
        