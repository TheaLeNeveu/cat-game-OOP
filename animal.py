class animal:
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour
        self. age = 1
        self.energy = 100

    def make_nosie():
        print("Animal made a noise")

class cat(animal):
    def make_nosie(self):
        print("Meow")

    def scratch(self):
        print("You have been scratched")

sid = cat("Sid", "Black")
sid.make_nosie