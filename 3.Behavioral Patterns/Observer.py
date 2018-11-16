#Observer.py
class Subject(object): #Represent what is being 'observed'

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append()

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observers in self._observers: 
            if modifier != observer:
                observer.update(self)

class Core(Subject):

    def __init__(self, name=""):
        Subject.__init__(self)
        self.name = name
        self.temp = 0

    def temp(self):
        return self._temp

    def temp(self, temp):
        self._temp = temp

class TempViewer:
    
    def update(self, subject):
        print("Temperature a viewer: {} has Temperature {}".format(subject.name, subject._temp))

#Let create cur subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

v1 = TempViewer()
v2 = TempViewer()

c1.attach(v1)
c1.attach(v2)

c1.temp = 80
c1.temp = 90





