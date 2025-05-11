class Søsterjonas:
    def __init__(self, name, pin):
        self.name= name
        self.pin= pin
        

    def feet(self):
        print("kult")
        return "rått"
        


jonas= Søsterjonas(input("sign: " ),input("pin: "))
komp= jonas.feet()
print(f" brukernavn er: {jonas.name}")
print(f" Pin er: {jonas.pin}")