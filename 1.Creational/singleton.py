class Borg:
    """Borg pattern making the class attributes global"""
    _shared_data = {} #Attribute dictionary
    def __init__(self):
        self.__dict__ = self._shared_data # Make it attribute dictonary

class Singleton(Borg): #inherits from the Borg class
    """This class now shares all its attributes among its various instances"""
    #This essenstially makes the singleton objects an objects an object-oriented global variable
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) # Update the attributes dictionary by inserting a new key-value pair
    def __str__(self):
        return str(self._shared_data)  #Returns the attribute dictionary for printing
#Let's create a singleton object and add our forst acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

y = Singleton(SNMP="Simple Network Management Protocol")
print(y)

z = Singleton(SMTP="Simple Mail Transfer Protocol")
print(z)

