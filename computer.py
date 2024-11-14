class device:
    def __init__(self, height, width, name):
        self. height = height
        self. width = width
        self. name = name

    def power_on(self):
        print("Device is turning on")

class computer(device):
    def power_on(self):
        print("Power on")

    def power_off(self):
        print("Power off")

    def restart(self):
        print("Restart")