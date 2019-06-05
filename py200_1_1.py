# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Метелев А.А.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class Glass:
    def __init__(self, capacity_volume, occupied_volume):

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Вы ввели не цифровое значение")
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Вы ввели не цифровое значение")

        if occupied_volume > capacity_volume:
            raise ValueError("Вы ввели значение наполнения стакана больше, чем объем стакана")
        if capacity_volume < 0:
            raise ValueError("Вы ввели значение наполнения стакана меньше 0")
        """print(dir(self))"""
        self.capacity_volume = capacity_volume
        """print(dir(self))"""
        self.occupied_volume = occupied_volume
        """print(dir(self))"""


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.


#if __name__ == "__main__":
#    Glass1 = Glass(200, 200)
#    print(Glass1.capacity_volume, Glass1.occupied_volume)
#    Glass1 = Glass(100, 100)
#    print(Glass1.capacity_volume, Glass1.occupied_volume)
#    Glass2 = Glass(250, 250)
#    print(Glass2.capacity_volume, Glass2.occupied_volume)
#    Glass2 = Glass(150, 150)
#    print(Glass2.capacity_volume, Glass2.occupied_volume)


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class GlassDefaultArg:
    def __init__(self, occupied_volume=0):

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Вы ввели не цифровое значение")

        if occupied_volume < 0:
            raise ValueError("Вы ввели значение наполнения стакана меньше 0")

        self.occupied_volume = occupied_volume


#if __name__ == "__main__":
#    Glass3 = GlassDefaultArg(0)
#    print(Glass3.occupied_volume)
#    Glass4 = GlassDefaultArg(200)
#    print(Glass4.occupied_volume)


# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?
  

class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):

        # if occupied_volume is None:
        #     self.occupied_volume = []

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        """Изменяется для всех объектов класса, это нарушает принцип ООП"""
        self.occupied_volume.append(capacity_volume)


#if __name__ == "__main__":
#    glass1 = GlassDefaultListArg(100)
#    print(glass1.occupied_volume)
#    glass2 = GlassDefaultListArg(200)
#    print(glass2.occupied_volume)
#    glass3 = GlassDefaultListArg(300)
#    print(glass3.occupied_volume)
#    print(f'Glass 1: {glass1.occupied_volume}')
#    print(f'Glass 2: {glass2.occupied_volume}')
#    print(f'Glass 3: {glass3.occupied_volume}')


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.


class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Вы ввели не цифровое значение")
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Вы ввели не цифровое значение")

        if occupied_volume > capacity_volume:
            raise ValueError("Вы ввели значение наполнения стакана больше, чем объем стакана")
        if capacity_volume < 0:
            raise ValueError("Вы ввели значение наполнения стакана меньше 0")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def add_water(self, add_volume):

        if not isinstance(add_volume, (int, float)):
            raise TypeError("Вы ввели не цифровое значение")

        if self.occupied_volume + add_volume > self.capacity_volume:
            self.occupied_volume = self.capacity_volume
            raise ValueError("Ваш стакан полон")

        self.occupied_volume += add_volume

    def remove(self, remove_volume):

        if not isinstance(remove_volume, (int, float)):
            raise TypeError("Вы ввели не цифровое значение")

        if self.occupied_volume - remove_volume <= 0:
                 self.occupied_volume = 0
                 raise ValueError("Ваш стакан пуст")

        self.occupied_volume -= remove_volume


#if __name__ == "__main__":
#    glass1 = GlassAddRemove(100, 50)
#    print(glass1.capacity_volume, glass1.occupied_volume)
#    glass1.add_water(30)
#    print(glass1.capacity_volume, glass1.occupied_volume)
#    glass1.remove(70)
#    print(glass1.capacity_volume, glass1.occupied_volume)


# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.


#if __name__ == "__main__":
#    glass1 = GlassAddRemove(100, 50)
#    glass2 = GlassAddRemove(200, 100)
#    glass3 = GlassAddRemove(300, 150)
#    print(dir(glass1))
#    print(dir(glass2))
#    print(dir(glass3))
#    print(dir(GlassAddRemove))
#    print(type(glass1))
#    print(type(glass2))
#    print(type(glass3))
#    print(type(GlassAddRemove))


# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.
#    По мере прохождения строк кода в __init__ создаются новые переменные(атрибуты) класса


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

#if __name__ == "__main__":
#    glass1 = Glass(100, 100)
#    glass2 = Glass(200, 100)
#    glass3 = Glass(300, 100)
#    print(id(glass1))
#    print(id(glass2))
#    print(id(glass3))
#    print(hex(id(glass1)))
#    print(hex(id(glass2)))
#    print(hex(id(glass1)))

# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     Да, верно, не обязательно использовать self
#     - соглашения о стиле кодирования
#     Нет, нужно использовать self
#    Запустите код.


class d:
    def __init__(f, a=2):
        f.a = a

    def print_me(p):
        print(p.a)


#d.print_me(d())


# 10. Исправьте
class A:
    def __init__(self, a):

        if not 10 < a < 50:
            raise ValueError()

        self.a = a

# Объясните так реализовывать __init__ нельзя?
# __init__ необходим для объявления атрибутов класса, а не для работы как классическая функция
        
        
        
# 11. Циклическая зависимость (стр. 39-44)
# 
import weakref

class Node:
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.__prev_node = prev_node
        self.__next_node = next_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node

    @property
    def prev_node(self):
        return self.__prev_node() if self.__prev_node is not None else None

    @prev_node.setter
    def prev_node(self, prev_node):
        self.__prev_node = weakref.ref(prev_node) if self.__prev_node is not None else None

    def __str__(self):
        return Node(self.data)
        
    def __repr__(self):
        return f'Node(self.data!r)'



class LinkedList:



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        
       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...