class Soda:
    def __init__(self, choise=None):
        self.choise = choise

    def sfow_my_drink(self):
        if self.choise:
            print(f'газировка и {self.choise}')

        else:
            print('Обычная газировка')

choise = Soda()
no_choise = Soda('Добавка')
choise.sfow_my_drink()
no_choise.sfow_my_drink()

