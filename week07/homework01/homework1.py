from abc import ABCMeta, abstractmethod
from AnimalProperty import *


# 動物園
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    # 新增動物
    def add_animal(self, aniaml):
        aniaml_id = id(aniaml)
        if aniaml_id in self.animals:
            aniamlType = aniaml.__class__.__name__
            print(f"has {aniamlType} is {aniaml_id} name {aniaml.name}")
        else:
            self.animals[aniaml_id] = aniaml

    # 是否有某一類動物
    def has_animal(self, animal_name):
        for _, animals in list(self.animals.items()):
            if animals.__class__.__name__.lower() == animal_name.lower():
                return True

        return False


# 動物
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, feeding, size, temperament):
        self.feeding = feeding
        self.size = size
        self.temperament = temperament

    # 是否属于凶猛动物
    @property
    def is_ferocious(self):

        if (self.size >= AnimalSize.Medium) and \
                (self.feeding == AnimalFeeding.Meat) and \
                (self.temperament == AnimalTemperament.Ferocious):
            return True
        else:
            return False


# 貓
class Cat(Animal):
    def __init__(self, name, type, size, temperament):
        super().__init__(type, size, temperament)
        self.name = name

    def meow(self):
        print("meow ~~ meow ~~ ")

    @property
    def is_pet(self):
        return False if self.temperament == AnimalTemperament.Ferocious else True


# 狗
class Dog(Animal):
    def __init__(self, name, type, size, temperament):
        super().__init__(type, size, temperament)
        self.name = name

    def woof(self):
        print("woof ! woof !")


if __name__ == "__main__":
    # 实例化动物园
    z = Zoo('时间动物园')

    # 实例化 猫1
    cat1 = Cat('大花猫 1', AnimalFeeding.Meat, AnimalSize.Medium, AnimalTemperament.Tame)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 重複加入提示
    z.add_animal(cat1)

    # 实例化 猫1
    cat2 = Cat('小花猫 2', AnimalFeeding.Meat, AnimalSize.Small, AnimalTemperament.Tame)
    # 增加一只猫到动物园
    z.add_animal(cat2)

    # 实例化 狗1
    dog1 = Dog('小白狗', AnimalFeeding.Meat, AnimalSize.Small, AnimalTemperament.Tame)
    # 增加一只猫到动物园
    z.add_animal(dog1)

    # 动物园是否有猫这种动物
    print(f"動物園是否有貓: {z.has_animal('cat')}")
    print(f"動物園是否有狗: {z.has_animal('dog')}")
