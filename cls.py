#Доброго времени суток.
#Домашнее задание к курсу 'Вход в язык"

#-*- coding: utf -8 -*-
# кодировка для распознания символов
from abc import ABC , abstractmethod
# Импорты всегда сверху
# Импортируем АБС класс и абстрактный метод
# Абстрактный метод обязательный для выполнения
# Абстрактный класс в моем понятии  унаследование главной функции но разными видами
# Например Супер(абстрактный) класс "Транспорт " главное действие 'движение' , но транспорты разные (машина, лодка , самолет )
# Поэтому наследуем только главное действие


'''class Kithen(ABC):
#Обьявляем класс (название)(наследуем классА АБС)
    @abstractmethod
    def kit_ob(self):
#Что такое сельф? Способ описания любого объекта (всегда идет первым)
        pass
#pass - данная функция не будет выполняться
class MyKit(Kithen):
#Обявим новый класс и наследуем от другого класса все что есть  
    def kit_ob(self):
#cоздадим новую функцию с аргументом сельф
        kitchen_cab = []
#Обявим что есть список в который будем добавлять 
        try:
#Попытаться сделать то-то , если есть исключение, то сделать вот это
            kitchen_cab.append(input())
#Добавим к списку методом аппенд и в аргументе укажем что ввод с клавиатуры что нужно добавить
            print('Добавил ')
#Выведем что все хорошо
            return kitchen_cab
#Вернем наш список
        except:
#Если что то не получилось покажем что то не так
            return('что не так')
ck = MyKit()
# Создаем экземпляр класса
print(ck.kit_ob())
# Выведем наш экземпляр и объекты
'''
class Room(ABC):
    @abstractmethod
    def Room_ob(self):
        pass
class MyRoom(Room):
    def Room_ob(self):
        MyRo = []
        try:
            MyRo.append(input())
            print('Готово')
            return MyRo
        except:
            ('Не готово')

 
MyR = MyRoom()
print(MyR.Room_ob())

