class Human:
    def __init__(self, height):
        self.__height = height


    def set_height(self, height):
        if height > 200:
            return
        self.__height = height

    def info(self):
        print("H", self.__height)

    def hello(self):
        print("Hello")

    def _hello(self):
        print("_Hello")

    def __hello(self):
        print("__Hello")

class Student(Human):
    def __init__(self, height, progress):
        super().__init__(height)
        self.__progress = progress

    def info(self):
        super().info()
        print("P", self.__progress)



class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128
    def calculate(self):
        print("I`m calculating....")

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4K"
    def display(self):
        print("I`m displaing screen... ")


class SmartPhone(Computer, Display):
    def info(self):
        print(self.memory)
        print(self.resolution)


s = SmartPhone()
s.calculate()
s.display()
s.info()


# h = Human(170)
# h.set_height(175)
# h.info()
#
# s = Student(170, 100)
# s.info()