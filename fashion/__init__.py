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
        response.raise_for_status()
        return response.text

    @staticmethod
    def async_trigger(name, body=None, callback_url=None, callback_function=None):
        """ """

        headers = {}
        if callback_url:
            headers['X-Callback-Url'] = callback_url
        if callback_function:
            headers['X-Callback-Url'] = GATEWAY_URL + ":" + str(GATEWAY_PORT) + f"/function/{name}"

        fashion_endpoint = GATEWAY_URL + ":" + str(GATEWAY_PORT) + f"/async-function/{name}"
        response = requests.post(fashion_endpoint, data=body, timeout=TIMEOUT_SECONDS, headers=headers)
        response.raise_for_status()
        return response.headers['X-Call-Id']

    @staticmethod
    def create_named_function(name, body=None):
        """ """

        if "async_" in name:
            def async_named_trigger(body, callback_url=None, callback_function=None):
                return Fashion.async_trigger(name.replace('async_', ''), body, callback_url, callback_function)
            return async_named_trigger
        else:
            def named_trigger(body):
                return Fashion.trigger(name, body)
            return named_trigger

    # OpenFaaS utilities
    @staticmethod
    def system_functions():
        """ """
        fashion_endpoint = GATEWAY_URL + ":" + str(GATEWAY_PORT) + f"/system/functions"
        response = requests.get(fashion_endpoint, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def system_alert(data):
        """ XXX UNTESTED XXX """
        fashion_endpoint = GATEWAY_URL + ":" + str(GATEWAY_PORT) + f"/system/alert"
        response = requests.post(fashion_endpoint, data=data, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        return response.json()

##
# Convenience methods
##

def trigger(name, body):
    return Fashion().trigger(name, body)

def async_trigger(name, body):
    return Fashion().async_trigger(name, body)

def system_functions():
    return Fashion().system_functions()

def system_alert():
    return Fashion().system_alert()

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
