class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"


class Car:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def addPassenger(self, human):
        self.passengers.append(human)

    def info(self):
        print(f"Auto : {self.model}")
        if self.passengers:
            print("Зараз в авто їдуть:")
            for h in self.passengers:
                print(h)
        else:
            print("Пасажири відсутні")

    def remove(self, name):
        for h in self.passengers:
            if h.name == name:
                self.passengers.remove(h)


h1 = Human("Vasya")
h2 = Human("Petya")
h3 = Human("Kolya")
# print(h1)

car = Car("Tesla Model U13")

car.info()
print()

car.addPassenger(h1)
car.addPassenger(h2)
car.addPassenger(h3)

car.info()
print()

car.remove("Vasya")
car.info()
print()
