"""
First class
"""
class Car:
    acceleration = 10

    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.in_motion = False
        self.speed = 0

    def drive(self):
        self.in_motion = True

    def accelerate(self):
        self.speed += self.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0

if __name__ == '__main__':
    my_kia = Car('EL39200')
    print(my_kia.speed)
    my_kia.accelerate()
    print(my_kia.speed)