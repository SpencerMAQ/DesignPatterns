class Dog():

    def __init__(self, name):
        self._name = name

    @staticmethod
    def speak():
        return "Woof!"

class Cat():

    def __init__(self, name):
        self._name = name

    @staticmethod
    def speak():
        return "Meow!"


def get_pet(pet='dog'):

    """The factory method"""

    # dict works by making the left side of '=' as the key
    # the right side becomes the value, which in this case
    # is a class object
    pets = dict(dog=Dog('Hope'), cat=Cat('Pikachu'))

    return pets[pet]

d = get_pet() # default arg = dog

print(d.speak())

c = get_pet('cat')

print(c.speak())

