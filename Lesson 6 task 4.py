class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name}  started'

    def stop(self):
        return f'{self.name}  stopped'

    def turn_right(self):
        return f'{self.name}  turned right'

    def turn_left(self):
        return f'{self.name}  turned left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of the town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than it is allowed for a town car'
        else:
            return f'Speed of {self.name} is acceptable for a town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of the car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than it is allowed'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from a police department'
        else:
            return f'{self.name} is not from a police department'


audi = SportCar(100, 'Red', 'Audi', False)
bmw = TownCar(30, 'White', 'BMW', False)
nissan = WorkCar(70, 'Green', 'Nissan', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(nissan.turn_left())
print(f'When {bmw.turn_right()}, then {audi.stop()}')
print(f'{nissan.go()} with speed\n {nissan.show_speed()}')
print(f'{nissan.name} is {nissan.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {nissan.name}  a police car? {nissan.is_police}')
print(audi.show_speed())
print(bmw.show_speed())
print(ford.police())
print(ford.show_speed())