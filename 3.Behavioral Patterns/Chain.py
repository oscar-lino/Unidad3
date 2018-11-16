#Chain.py
class Handler:
    def __init__(self, successor):
        self._succesor = successor

    def handle(self, request):
        handle = self._handle(request)

        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass!")

class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0< request <= 10:
            print("Request {} handled in handler 1".format(request))
            return True

class Default(Handler):
    def _handle(self, request):
        print("End of chain, no handler for{}".format(request))
        return True

class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, request):
        for request in request:
            self.handler.handle(request)

c = Client()

requests = [2, 5, 30]

c.delegate(requests)
