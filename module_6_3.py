class Vehicle:
    __COLOR_VARIANST = ['blue', 'red', 'green', 'black', 'while']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.model = model
        self.set_color(color)
        self.engine_power = engine_power

    def set_color(self, color):
        if color.upper() in [c.upper() for c in self.__COLOR_VARIANST]:
            self.color = color
        else:
            print(f'Нельзя сменить цвет на {color}')

    def print_info(self):
        print(f'Модель: {self.model}')
        print(f'Мощность двигателя: {self.engine_power}')
        print(f'Цвет: {self.color}')
        print(f'Владелец: {self.owner}')

class Sedan(Vehicle):
    __passenger_limit = 5
    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


vehicle1 = Sedan('Fedos', 'Toyota Marl 2', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
