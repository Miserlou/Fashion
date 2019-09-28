import importlib
import http.client

FASHION_GATEWAY_URL = '127.0.0.1'
FASHION_GATEWAY_PORT = '8080'
FASHION_TIMEOUT_SECONDS = 900

class Fashion:

    def hello(self):
        print('hello')

    @staticmethod
    def trigger(name):
        connection = http.client.HTTPSConnection("api.bitbucket.org", timeout=FASHION_TIMEOUT_SECONDS)
        connection.request('GET', '/2.0/repositories')
        response = connection.getresponse()
        content = response.read().decode('utf-8')
        print(content[:100], '...')
        print(name)

    @staticmethod
    def create_named_function(name):
        #return lambda: print("Hello, " + name + "!")
        return lambda: Fashion.trigger(name)

##
# We use PEP562 to create our named functions at import time.
# We have to do this after the Fashion class is created, and we can't do an import,
# which is why the Fashion class lives in this file.
##

def __getattr__(name):
    """
    We don't need to manually check for it's prexistence in dir(Fashion) because it will already raise an ImportError if it exist
    """

    return Fashion.create_named_function(name)
