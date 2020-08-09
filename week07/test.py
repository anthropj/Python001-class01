from abc import ABCMeta, abstractclassmethod
class Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self, name, type_, size, character):
        self.name = name
        self.type = type_
        self.size = size
        self.character = character

    @property
    def is_ferocious(self) -> bool:
        return self.size != '小' and self.type == '食肉'\
            and self.character == '凶猛'


class Cat(Animal):
    meow = True

    def __init__(self, name, type_, size, character):
        super().__init__(name, type_, size, character)
        self.nice_as_pet = True


class Zoo():
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        for item in self.__animals:
            if animal.__class__.__name__ == item.__class__.__name__:
                return False
        self.__animals.append(animal)
        return True

    def __getattr__(self,animal):
        for item in self.__animals:
            if item.__class__.__name__ == animal:
                return True
        return False

if __name__ == '__main__':
    z = Zoo('时间动物园')

    cat1 = Cat('大花猫','食肉','小','温顺')
    z.add_animal(cat1)

    have_cat = getattr(z,'Cat')