"""Примеры по созданию и использованию классов в питоне
Всё есть объект!
"""

class FirstClass:                   #когда интерпретатор достигнет инструкции class, он начнёт создавать объект класса с именем (ссылкой на объект)FirstClass
    def set_data(self, value):      #интерпретатор определяет метод класса (поведение по умолчанию для экземпляров)
        self.data = value           #экземпляр или контекст(self ссылка на объект) с переменной data должен будет получить значение через аргумент

    def display(self):              #def это операция присваивания переменной display к объекту функции в области видимости class
        print(self.data)            #и тем самым становясь атрибутом у объекта класса (FirstClass.display)

class SecondClass(FirstClass):      #наследует set_data
    def display(self):              #изменяет display
        print('current value = "%s"' % self.data)

"""Иногда такая замена атрибутов за счет их переопределения ниже в дереве классов называется перегрузкой."""
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other


class Test:
    pass



if __name__ == '__main__':
    x = FirstClass()        #x,y отдельные пространства имён
    y = FirstClass()        #создаются объекты экземпляров (из объекта класса FirstClass), а x и y это ссылки на них
                            #на данный момент имеются три связаных пространства имён
                            #атрибут data обнаруживается в объекте экземпляра, а set_data и display в классе
    #z = ThirdClass(55)
    #z.set_data(55)
    #z.display()
    #print(z)
    Test.name = "bob"
    Test.age = 40
    print(Test.age, Test.name)

    z = Test()
    a = Test()
    z.name="ava"
    print(z.name, Test.name)
    print(dir(ThirdClass))
    print(ThirdClass.__dict__.keys())
    print(Test.__dict__.keys())
    print(z.__dict__.keys())
    print(a.__dict__.keys())
    print(a.__class__)
    print(z.__class__)
    #z = SecondClass()
    #z.set_data(555)
    #z.display()


    #FirstClass.set_data(y, "Hi")
    #FirstClass.display(y)

    #x.set_data(5)
    #x.display()
    #x.data = "Hi"
    #x.display()
    #print(x)
    #print(FirstClass)


    #print(type(FirstClass))
    #print(type(x))


"""Ни x, ни y не имеют собственного атрибута setdata и display, поэтому, чтобы отыскать его, интерпретатор следует по ссылке от экземпляра к классу.
В этом заключается суть наследования в языке Python: механизм наследования привлекается в момент разрешения имени атрибута,
 и вся его работа заключается лишь в поиске имен в связанных объектах"""


