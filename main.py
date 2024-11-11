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
        self.friendship = 0
    
    def train(self):
        if cat_attributes["energy"] < 7:
            print(name, "is too tired to train right now.")
        else:
            print(f"{self.name} is training")
            self.friendship += 10
            self.intelligence += 20
            self.energy"] -= 20
            cat_attributes["weight"] -= 5
            print(name, "gained 10 friendship points")
            print(name, "gained 20 intelligence points")
            print(name, "lost 20 energy points")
            print(name, "lost 5 weight points")

    def feed(self):
        print(f"{self.name} is eating")
        cat_attributes["friendship"] += 20
        cat_attributes["energy"] += 10
        cat_attributes["weight"] += 5
        print(name, "gained 20 friendship points")
        print(name, "gained 10 energy points")
        print(name, "gained 5 weight points")

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

options = [
    {
        "type": "list",
        "message": "What would you like to do?",
        "choices": ["Play with your cat", "Train your cat", "Feed your cat", "Let your cat sleep", "Show stats"]
    }
]

cat_attributes = {
    "friendship": 0,
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
ans = prompt(questions)
name = ans["name"]
colour = ans["colour"]

# start the while loop
while True:
    # Finish the string below
    option = prompt(options)[0]
    if option == "Play with your cat":
        if cat_attributes["energy"] < 5:
            print(name, "is too tired to play right now.")
        # change the cat's attributes here
        else:
            cat_attributes["friendship"] += 30
            cat_attributes["intelligence"] += 5
            cat_attributes["energy"] -= 10
            cat_attributes["weight"] -= 5
            print(name, "gained 10 friendship points")
            print(name, "gained 5 intelligence points")
            print(name, "lost 10 energy points")
            print(name, "lost 5 weight points")

    elif option == "Train your cat":
        

    elif option == "Feed your cat":
        

    elif option == "Let your cat sleep":
        cat_attributes["energy"] += 50
        cat_attributes["weight"] += 5
        print(name, "gained 50 energy points")
        print(name, "gained 5 weight points")

    elif option == "Show stats":
        print(cat_attributes)
    # elif ...
    else:
        pass

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        print(name, "died from exhaustion.")
    # elif ...
    