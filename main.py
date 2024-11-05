class cat:
    def __innit__(self, name, colour):
        #The constructor will creat a cat for us in vade. To create a catm we need name and colour.
        #self is the cat that we are creating.
        self.name = name
        self.colour = colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5
    
    def train(self):
        print(f"{self.name} is training")
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1

    def feed(self):
        print(f"{self.name} is eating")
        sel.energy += 10
        self.weight += 1
        self.age += 0.1

#We will now make 2 cats.
sid = cat("Sid", "Black")
mista = cat("Mista", "White")

name = input("Enter cat name: ")
colour = input("Enter cat colour: ")

while True:
    action = input("""
    What would you like to do?
    1. Train
    2. Feed
    3. Play
    4. Sleep
    """)
    if action == "1":
        cat.train()
    elif action == "2":
        cat.feed()