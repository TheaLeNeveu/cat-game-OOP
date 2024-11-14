class vehicle:
    def __init__(self, name, speed, size):
        self.name = name
        self.speed = speed
        self.size = size

    def switch_on(self):
        print("Switching on")

    def drive(self):
        print("Driving")

    def fix(self):
        print("Fixing")

class car(vehicle):
    def switch_on(self):
        print("Turn key")

    def drive(self):
        print("Hands on wheel")

    def fix(self):
        print("Hood up")

    def switch_off(self):
        print("Take out key")

class motorbike(vehicle):
    def switch_on(self):
        print("Kick up stand")

    def drive(self):
        print("Hands on handlebars")

    def fix(self):
        print("Check tires")

    def switch_off(self):
        print("Kick down stand")