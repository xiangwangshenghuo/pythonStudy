class Person(object):
    eye = 2
    hand = 2
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')

    @classmethod
    def eat(cls):
        print('eat')




if __name__ == "__main__":
    person = Person('cai')
    print(Person.__dict__)
    print(person.__dict__)
    print(person.__module__)
    print(Person.__bases__)

