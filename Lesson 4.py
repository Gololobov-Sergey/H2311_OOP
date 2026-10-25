import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.energy = 50
        self.progress = 10
        self.alive = True
        self.money = 50

    def study(self):
        print("Я пішов навчатися до IT STEP Academy")
        self.progress += random.randint(0, 6) - 1
        self.gladness += random.randint(0, 4) - 3
        self.energy -= random.randint(1, 3)


    def chill(self):
        print("Я пішов з друзяками гулять")
        self.progress -= 1
        self.gladness += random.randint(2, 4)
        self.energy -= 4

    def sleep(self):
        print("Я пішов спати")
        self.gladness += random.randint(1, 2)
        self.energy += 4

    def eat(self):
        print("Чіпси, кола - поїсти по приколу!")
        self.gladness += random.randint(1, 3)
        self.energy += 5

    def info(self):
        print(f"Навченість  : {self.progress}")
        print(f"Задоволення : {self.gladness}")
        print(f"Енергія     : {self.energy}")

    def is_alive(self):
        if self.progress <= 0:
            print("В мене в голові одне сміття")
            self.alive = False
        if self.energy <= 0:
            print("Я зовсім знесилений")
            self.alive = False
        if self.gladness <= 0:
            print("В мене дипресія")
            self.alive = False
        if self.progress > 100:
            print("Ура! Я став академіком")
            self.alive = False

    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)

        # # ======= v 1.0 ============
        # self.eat()
        # self.study()
        # self.chill()
        # self.sleep()
        # # ==========================

        # ======= v 2.0 ============
        func = [self.sleep, self.study, self.chill, self.eat]
        random.choice(func)()
        # ==========================


        self.info()
        self.is_alive()
        print()


student = Student("Vasya")
# for day in range(1, 366):
#     if student.alive:
#         student.live(day)

day = 1
while student.alive:
    student.live(day)
    day += 1

