class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  
  def display_info(self):
    print(f"Name:{self.__name}\tAge:{self.__age}")

  def print_person(self):
    print(f"Имя:{self.__name}\tВозраст:{self.__age}")
  
  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, age):
    if 0 < age <110:
      self.__age = age
    else:
      print("Недопустимо")

  @property
  def name(self):
    return self.__name


  @name.setter
  def name(self, age):
      self.__name = name

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_info(self):
      super().display_info()
      print(f"Курс: {self.course}")


student = Student("Bob", 19, 2)
student.display_info()
tom = Person("Tom", 16)
tom.print_person()
tom.age = -3486123
