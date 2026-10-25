
class Student:
    count = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Student.count += 1

    def setAge(self, age):
        if age > 100:
            return
        self.age = age

    def info(self):
        print(f"Ім'я : {self.name}, вік : {self.age}, зріст : {self.height}")

    def grow(self, deltaHeight=1):
        if self.height + deltaHeight > 200:
            return
        self.height += deltaHeight

print(Student.count)

st1 = Student("Vasya", 15, 160)
st1.setAge(17)
st1.grow(5)

st1.info() # info(st1)
print(Student.count)


st2 = Student("Petya", 16, 150)
st2.info()
print(Student.count)