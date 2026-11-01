import random
class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.car = car
        self.job = job
        self.house = House()
        self.money = 1000

    def work(self):
        if self.job is not None:
            if self.car is not None:
                print("Я поїхав на роботу")
            else:
                print("Я пішов на роботу")
            print(f"Я працюю : {self.job.name}, заробив сьогодні {self.job.salary}$")
            self.money += self.job.salary

    def shopping(self):
        print("Шопінг:")
        money = random.randint(20, 30)
        food = random.randint(5, 10)
        if self.car is None:
            print("Я пішов в магазин пішки")
        else:
            if self.car.drive(random.randint(10, 20)):
                pass
            else:
                print("Я пішов в магазин пішки")
        print(f"Я витратив {money}$, придбав {food} продуктів")
        self.money -= money
        self.house.food += food

    def eat(self):
        eat = random.randint(2,5)
        if self.house.food - eat > 0:
            print(f"Я смачно поїв {eat} продуктів")
            self.house.food -= eat
            self.house.pollution += random.randint(1,5)
        else:
            print(f"Я хотів зїсти {eat} продуктів, але їх немає")
            self.shopping()

    def chill(self):
        money = random.randint(10, 20)
        if self.money - money > 10:
            print(f"Я гарно відпочив, і витратив {money}$")
            self.money -= money
            self.house.pollution += random.randint(1, 5)
        else:
            print("Я відпочиваю вдома, немає грошей")

    def cleaning(self):
        print("Прибирання:")
        rnd = random.randint(1,2)
        if rnd == 1:
            print("Я поганяв пилюку")
            self.house.pollution -= 2
        else:
            print("Я виконав генеральне прибирання")
            self.house.pollution -= 5

        if self.house.pollution < 0:
            self.house.pollution = 0
    def info(self):
        pass

    def live(self):
        pass

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60   # litr
        self.state = 100 # %

    def add_fuel(self):
        pass

    def drive(self, length):
        rashod = length * 0.1
        if self.fuel - rashod > 0:
            print(f"Я проїхав {length} км, втратив {rashod} л пального")
            self.fuel -= rashod
            self.state -= length * 0.01
            return True
        else:
            print("Подорож не можлива, немає пального")
            return False

    def __str__(self):
        pass

class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f"Будинок: Їжа - {self.food}, забрудненність - {self.pollution}"

class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        pass



human = Human("Vasya", job=Job("Programmer", 100), car=Car("Audi Q5"))
# human.work()
# human.shopping()
# human.eat()
print(human.house)
human.cleaning()