import importlib
import requests

GATEWAY_URL = 'http://127.0.0.1'
GATEWAY_PORT = 8080
TIMEOUT_SECONDS = 900

class Fashion:
    """ """

    @staticmethod
    def trigger(name, body=None):
        """ """

        fashion_endpoint = GATEWAY_URL + ":" + str(GATEWAY_PORT) + f"/function/{name}"
        response = requests.post(fashion_endpoint, data=body, timeout=TIMEOUT_SECONDS)
        return response.text

    @staticmethod
    def create_named_function(name, body=None):
        """ """
        def named_trigger(body):
            return Fashion.trigger(name, body)
        return named_trigger

##
# Convenience methods
##

def trigger(name, body):
    f = Fashion()
    return f.trigger(name, body)

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
