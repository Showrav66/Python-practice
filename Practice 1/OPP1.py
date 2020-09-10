class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is:", self.cpu, self.ram)


com1 = Computer('i3', 4)
com2 = Computer('i5', 8)
com3 = Computer('i7', 16)
com4 = Computer('i9', 32)

com1.config()
com2.config()
com3.config()
com4.config()
