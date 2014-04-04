import config
import imp
import license_readers
import os

def getHandler(managerType):
    base_path = os.path.dirname(license_readers.__file__)
    path = os.path.join(base_path, "%s.py" % managerType)
    mod = __import__("license_readers.%s" % managerType)
    mod = imp.load_source('license_readers.%s'%(managerType), path)
    handlerClass = getattr(mod, "%sHandler" % managerType)
    return handlerClass

def main():
    for server in config.LICENSE_SERVERS:
        for managerType, port in server['managers']:
            handlerClass = getHandler(managerType)
            handler = handlerClass(server['address'], port)
            print handler.query()

if __name__ == '__main__':
    main()