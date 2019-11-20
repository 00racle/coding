class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet       #변수 앞에 __를 붙여서 비공새 속성으로 만듬

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아', 20, '서울시', 10000)
maria.pay(3000)
